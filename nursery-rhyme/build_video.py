#!/usr/bin/env python3
"""Build a 30s toddler nursery-rhyme video from keyframes + TTS + melody."""

from __future__ import annotations

import asyncio
import math
import subprocess
import wave
from pathlib import Path

import edge_tts
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/workspace/nursery-rhyme")
ASSETS = Path("/opt/cursor/artifacts/assets")
AUDIO = ROOT / "audio"
LYRICS = ROOT / "lyrics"
CLIPS = ROOT / "clips"
OUT = Path("/opt/cursor/artifacts")
FPS = 30
DURATION = 30
W, H = 1920, 1080

LINES = [
    (0.0, 5.0, "Duckling, bunny, elephant too"),
    (5.0, 10.0, "Dancing in the meadow with you"),
    (10.0, 15.0, "Bounce and clap and shout with me"),
    (15.0, 20.0, "Friends forever — one, two, three!"),
    (20.0, 25.0, "Rainbow smiles for you and me"),
    (25.0, 30.0, "Happy friends — that's you and me!"),
]

IMAGE_SEQUENCE = [
    ASSETS / "nursery-hero.jpg",
    ASSETS / "nursery-sing.jpg",
    ASSETS / "nursery-dance.jpg",
    ASSETS / "nursery-sing.jpg",
    ASSETS / "nursery-dance.jpg",
    ASSETS / "nursery-finale.jpg",
]

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
VOICE = "en-US-AnaNeural"


def ensure_dirs() -> None:
    for p in (AUDIO, LYRICS, CLIPS, OUT, ROOT):
        p.mkdir(parents=True, exist_ok=True)


def run_ffmpeg(cmd: list[str]) -> None:
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr[-3000:] or result.stdout[-3000:])


def midi_to_hz(midi: float) -> float:
    return 440.0 * (2.0 ** ((midi - 69.0) / 12.0))


def synth_tone(
    freq: float,
    seconds: float,
    sr: int = 44100,
    amp: float = 0.22,
    wave_kind: str = "triangle",
) -> np.ndarray:
    n = int(sr * seconds)
    t = np.linspace(0.0, seconds, n, endpoint=False)
    phase = 2 * math.pi * freq * t
    if wave_kind == "triangle":
        sig = (2 / math.pi) * np.arcsin(np.sin(phase))
    else:
        sig = np.sin(phase)
    attack = min(0.02, seconds * 0.15)
    release = min(0.18, seconds * 0.45)
    env = np.ones(n)
    a_n = max(1, int(attack * sr))
    r_n = max(1, int(release * sr))
    env[:a_n] = np.linspace(0, 1, a_n)
    if r_n < n:
        env[-r_n:] = np.linspace(1, 0, r_n)
    return (sig * env * amp).astype(np.float32)


def write_wav(path: Path, samples: np.ndarray, sr: int = 44100) -> None:
    clipped = np.clip(samples, -1.0, 1.0)
    pcm = (clipped * 32767.0).astype(np.int16)
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(pcm.tobytes())


def make_melody(path: Path, sr: int = 44100) -> None:
    motif = [
        (72, 0.4),
        (74, 0.4),
        (76, 0.4),
        (79, 0.6),
        (76, 0.4),
        (74, 0.4),
        (72, 0.5),
        (67, 0.5),
        (69, 0.4),
        (72, 0.4),
        (74, 0.4),
        (76, 0.6),
        (74, 0.4),
        (72, 0.8),
        (72, 0.4),
    ]
    total = DURATION
    pad = (
        0.04
        * np.sin(2 * math.pi * midi_to_hz(60) * np.linspace(0, total, int(sr * total), False))
        * np.hanning(int(sr * total))
    ).astype(np.float32)
    melody = np.zeros(int(sr * total), dtype=np.float32)
    t = 0.0
    while t < total - 0.2:
        for midi, dur in motif:
            if t >= total:
                break
            note = synth_tone(midi_to_hz(midi), dur, sr=sr, amp=0.18, wave_kind="triangle")
            harm = synth_tone(midi_to_hz(midi + 7), dur, sr=sr, amp=0.07, wave_kind="sine")
            start = int(t * sr)
            end = min(len(melody), start + len(note))
            melody[start:end] += note[: end - start]
            melody[start:end] += harm[: end - start]
            t += dur + 0.05
        t += 0.15
    mix = melody + pad[: len(melody)]
    peak = np.max(np.abs(mix)) or 1.0
    mix = (mix / peak * 0.55).astype(np.float32)
    write_wav(path, mix, sr)


async def make_vocals(path: Path) -> None:
    wavs: list[tuple[float, Path]] = []
    for i, (start, _end, text) in enumerate(LINES):
        mp3 = AUDIO / f"line_{i}.mp3"
        wav = AUDIO / f"line_{i}.wav"
        if not mp3.exists():
            communicate = edge_tts.Communicate(text, VOICE, rate="-5%", pitch="+15Hz")
            await communicate.save(str(mp3))
        if not wav.exists():
            run_ffmpeg(
                ["ffmpeg", "-y", "-i", str(mp3), "-ar", "44100", "-ac", "1", str(wav)]
            )
        wavs.append((start, wav))

    inputs: list[str] = []
    filters: list[str] = []
    for i, (start, wav) in enumerate(wavs):
        inputs.extend(["-i", str(wav)])
        delay_ms = int(start * 1000)
        filters.append(f"[{i}]adelay={delay_ms}|{delay_ms},volume=1.35[v{i}]")
    mix_in = "".join(f"[v{i}]" for i in range(len(wavs)))
    filters.append(f"{mix_in}amix=inputs={len(wavs)}:duration=longest:normalize=0[out]")
    run_ffmpeg(
        [
            "ffmpeg",
            "-y",
            *inputs,
            "-filter_complex",
            ";".join(filters),
            "-map",
            "[out]",
            "-t",
            str(DURATION),
            "-ar",
            "44100",
            str(path),
        ]
    )


def mix_audio(melody: Path, vocals: Path, out: Path) -> None:
    run_ffmpeg(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(melody),
            "-i",
            str(vocals),
            "-filter_complex",
            "[0:a]volume=0.38[m];[1:a]volume=1.15,apad=whole_dur=30[v];"
            "[m][v]amix=inputs=2:duration=first:normalize=0[a]",
            "-map",
            "[a]",
            "-t",
            str(DURATION),
            "-ar",
            "44100",
            str(out),
        ]
    )


def fit_cover(img: Image.Image, tw: int, th: int) -> Image.Image:
    src = img.convert("RGB")
    scale = max(tw / src.width, th / src.height)
    nw, nh = int(src.width * scale), int(src.height * scale)
    src = src.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - tw) // 2
    top = (nh - th) // 2
    return src.crop((left, top, left + tw, top + th))


def render_lyric_card(text: str, out_path: Path, size: tuple[int, int] = (1600, 160)) -> None:
    card = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle(
        [0, 0, size[0] - 1, size[1] - 1],
        radius=40,
        fill=(255, 255, 255, 215),
    )
    colors = [
        (255, 92, 92),
        (255, 168, 38),
        (80, 190, 90),
        (64, 156, 255),
        (186, 110, 230),
        (255, 120, 180),
    ]
    font_size = 64
    while font_size > 36:
        font = ImageFont.truetype(FONT_PATH, font_size)
        bbox = draw.textbbox((0, 0), text, font=font)
        if bbox[2] - bbox[0] <= size[0] - 80:
            break
        font_size -= 2
    font = ImageFont.truetype(FONT_PATH, font_size)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size[0] - tw) // 2
    y = (size[1] - th) // 2 - 4
    cx = x
    for i, ch in enumerate(text):
        color = colors[i % len(colors)]
        draw.text((cx + 2, y + 2), ch, font=font, fill=(40, 40, 60, 90))
        draw.text((cx, y), ch, font=font, fill=color + (255,))
        cw = draw.textbbox((0, 0), ch, font=font)[2]
        cx += cw
    card.save(out_path)


def prepare_sources() -> list[Path]:
    """Upscale/cover-crop sources so zoompan has room to bounce gently."""
    prepared: list[Path] = []
    for i, src in enumerate(IMAGE_SEQUENCE):
        dst = CLIPS / f"src_{i}.png"
        fit_cover(Image.open(src), int(W * 1.18), int(H * 1.18)).save(dst)
        prepared.append(dst)
        render_lyric_card(LINES[i][2], LYRICS / f"lyric_{i}.png")
    return prepared


def make_segment(src: Path, lyric: Path, out: Path, seconds: float = 5.0) -> None:
    """Gentle zoom + bounce via zoompan, with lyric overlay."""
    frames = int(seconds * FPS)
    # zoom slowly from 1.0 toward 1.05; y bounces with sin
    # zoompan uses on-expression evaluated per frame
    z_expr = "min(zoom+0.00035,1.05)"
    x_expr = "iw/2-(iw/zoom/2)"
    y_expr = f"ih/2-(ih/zoom/2)+10*sin(2*PI*on/{FPS})"
    vf = (
        f"zoompan=z='{z_expr}':x='{x_expr}':y='{y_expr}':d={frames}:s={W}x{H}:fps={FPS},"
        f"format=rgba[bg];"
        f"[1:v]format=rgba[ly];"
        f"[bg][ly]overlay=(W-w)/2:H-h-70:format=auto,format=yuv420p"
    )
    run_ffmpeg(
        [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-i",
            str(src),
            "-i",
            str(lyric),
            "-filter_complex",
            vf,
            "-t",
            str(seconds),
            "-r",
            str(FPS),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-crf",
            "18",
            str(out),
        ]
    )


def concat_and_mux(segments: list[Path], audio: Path, out: Path) -> None:
    """Soft crossfade between segments; segment length chosen so final = 30s."""
    fade = 0.6
    # n*d - (n-1)*fade = 30  =>  d = (30 + (n-1)*fade) / n
    n = len(segments)
    seg_dur = (DURATION + (n - 1) * fade) / n  # 5.5s for n=6, fade=0.6
    inputs: list[str] = []
    for seg in segments:
        inputs.extend(["-i", str(seg)])
    inputs.extend(["-i", str(audio)])

    filters: list[str] = []
    offset = seg_dur - fade
    filters.append(
        f"[0:v][1:v]xfade=transition=fade:duration={fade}:offset={offset:.4f}[x1]"
    )
    prev = "x1"
    for i in range(2, n):
        offset = offset + seg_dur - fade
        filters.append(
            f"[{prev}][{i}:v]xfade=transition=fade:duration={fade}:offset={offset:.4f}[x{i}]"
        )
        prev = f"x{i}"
    audio_idx = n
    filters.append(f"[{prev}]format=yuv420p,fps={FPS}[vout]")
    fc = ";".join(filters)
    run_ffmpeg(
        [
            "ffmpeg",
            "-y",
            *inputs,
            "-filter_complex",
            fc,
            "-map",
            "[vout]",
            "-map",
            f"{audio_idx}:a",
            "-t",
            str(DURATION),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-crf",
            "18",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-shortest",
            "-movflags",
            "+faststart",
            str(out),
        ]
    )


async def main() -> None:
    ensure_dirs()
    print("1/5 Melody…")
    melody = AUDIO / "melody.wav"
    make_melody(melody)

    print("2/5 Vocals…")
    vocals = AUDIO / "vocals.wav"
    await make_vocals(vocals)

    print("3/5 Mix audio…")
    mixed = AUDIO / "mixed.wav"
    mix_audio(melody, vocals, mixed)

    print("4/5 Prepare sources + segments…")
    sources = prepare_sources()
    fade = 0.6
    n = len(sources)
    seg_dur = (DURATION + (n - 1) * fade) / n  # keeps final length at 30s with xfades
    segments: list[Path] = []
    for i, src in enumerate(sources):
        seg = CLIPS / f"seg_{i}.mp4"
        print(f"  segment {i + 1}/{len(sources)} ({seg_dur:.2f}s)")
        make_segment(src, LYRICS / f"lyric_{i}.png", seg, seg_dur)
        segments.append(seg)

    print("5/5 Concat + mux…")
    out = OUT / "friends-in-the-meadow.mp4"
    concat_and_mux(segments, mixed, out)
    # Probe
    probe = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration,size:stream=width,height,codec_type",
            "-of",
            "default=noprint_wrappers=1",
            str(out),
        ],
        capture_output=True,
        text=True,
    )
    print(probe.stdout)
    print(f"Done: {out}")


if __name__ == "__main__":
    asyncio.run(main())

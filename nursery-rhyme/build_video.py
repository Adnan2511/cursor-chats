#!/usr/bin/env python3
"""Build a 30s toddler nursery-rhyme video from keyframes + TTS + melody.

Formats:
  landscape  1920x1080 (16:9)
  reel       1080x1920 (9:16) — Instagram / TikTok / Shorts
"""

from __future__ import annotations

import argparse
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

LINES = [
    (0.0, 5.0, "Duckling, bunny, elephant too"),
    (5.0, 10.0, "Dancing in the meadow with you"),
    (10.0, 15.0, "Bounce and clap and shout with me"),
    (15.0, 20.0, "Friends forever — one, two, three!"),
    (20.0, 25.0, "Rainbow smiles for you and me"),
    (25.0, 30.0, "Happy friends — that's you and me!"),
]

LANDSCAPE_IMAGES = [
    ASSETS / "nursery-hero.jpg",
    ASSETS / "nursery-sing.jpg",
    ASSETS / "nursery-dance.jpg",
    ASSETS / "nursery-sing.jpg",
    ASSETS / "nursery-dance.jpg",
    ASSETS / "nursery-finale.jpg",
]

REEL_IMAGES = [
    ASSETS / "reel-hero.jpg",
    ASSETS / "reel-sing.jpg",
    ASSETS / "reel-dance.jpg",
    ASSETS / "reel-sing.jpg",
    ASSETS / "reel-dance.jpg",
    ASSETS / "reel-finale.jpg",
]

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
VOICE = "en-US-AnaNeural"

# Set by configure()
W = 1920
H = 1080
IMAGE_SEQUENCE: list[Path] = LANDSCAPE_IMAGES
OUTPUT_NAME = "friends-in-the-meadow.mp4"
LYRIC_CARD_SIZE = (1600, 160)
LYRIC_BOTTOM_PAD = 70
FORMAT_NAME = "landscape"


def configure(fmt: str) -> None:
    global W, H, IMAGE_SEQUENCE, OUTPUT_NAME, LYRIC_CARD_SIZE, LYRIC_BOTTOM_PAD, FORMAT_NAME
    FORMAT_NAME = fmt
    if fmt == "reel":
        W, H = 1080, 1920
        IMAGE_SEQUENCE = REEL_IMAGES
        OUTPUT_NAME = "friends-in-the-meadow-reel.mp4"
        LYRIC_CARD_SIZE = (980, 220)
        LYRIC_BOTTOM_PAD = 160  # above typical reel UI chrome
        CLIPS_DIR = ROOT / "clips_reel"
        LYRICS_DIR = ROOT / "lyrics_reel"
        globals()["CLIPS"] = CLIPS_DIR
        globals()["LYRICS"] = LYRICS_DIR
    else:
        W, H = 1920, 1080
        IMAGE_SEQUENCE = LANDSCAPE_IMAGES
        OUTPUT_NAME = "friends-in-the-meadow.mp4"
        LYRIC_CARD_SIZE = (1600, 160)
        LYRIC_BOTTOM_PAD = 70
        globals()["CLIPS"] = ROOT / "clips"
        globals()["LYRICS"] = ROOT / "lyrics"


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


def wrap_lyric(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        bbox = draw.textbbox((0, 0), trial, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [text]


def render_lyric_card(text: str, out_path: Path, size: tuple[int, int] | None = None) -> None:
    size = size or LYRIC_CARD_SIZE
    card = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle(
        [0, 0, size[0] - 1, size[1] - 1],
        radius=36,
        fill=(255, 255, 255, 220),
    )
    colors = [
        (255, 92, 92),
        (255, 168, 38),
        (80, 190, 90),
        (64, 156, 255),
        (186, 110, 230),
        (255, 120, 180),
    ]
    max_text_w = size[0] - 64
    font_size = 58 if FORMAT_NAME == "reel" else 64
    min_size = 34 if FORMAT_NAME == "reel" else 36
    lines: list[str] = [text]
    font = ImageFont.truetype(FONT_PATH, font_size)
    while font_size >= min_size:
        font = ImageFont.truetype(FONT_PATH, font_size)
        lines = wrap_lyric(text, font, max_text_w, draw)
        heights = []
        widths = []
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font)
            widths.append(bbox[2] - bbox[0])
            heights.append(bbox[3] - bbox[1])
        total_h = sum(heights) + (len(lines) - 1) * 10
        if max(widths, default=0) <= max_text_w and total_h <= size[1] - 40:
            break
        font_size -= 2

    line_gap = 10
    heights = []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        heights.append(bbox[3] - bbox[1])
    total_h = sum(heights) + (len(lines) - 1) * line_gap
    y = (size[1] - total_h) // 2 - 2
    char_i = 0
    for li, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        x = (size[0] - tw) // 2
        cx = x
        for ch in line:
            color = colors[char_i % len(colors)]
            draw.text((cx + 2, y + 2), ch, font=font, fill=(40, 40, 60, 90))
            draw.text((cx, y), ch, font=font, fill=color + (255,))
            cw = draw.textbbox((0, 0), ch, font=font)[2]
            cx += cw
            char_i += 1
        y += heights[li] + line_gap
    card.save(out_path)


def prepare_sources() -> list[Path]:
    """Upscale/cover-crop sources so zoompan has room to bounce gently."""
    prepared: list[Path] = []
    for i, src in enumerate(IMAGE_SEQUENCE):
        if not src.exists():
            raise FileNotFoundError(f"Missing keyframe: {src}")
        dst = CLIPS / f"src_{i}.png"
        fit_cover(Image.open(src), int(W * 1.18), int(H * 1.18)).save(dst)
        prepared.append(dst)
        render_lyric_card(LINES[i][2], LYRICS / f"lyric_{i}.png")
    return prepared


def make_segment(src: Path, lyric: Path, out: Path, seconds: float = 5.0) -> None:
    """Gentle zoom + bounce via zoompan, with lyric overlay."""
    frames = int(seconds * FPS)
    bounce = 14 if FORMAT_NAME == "reel" else 10
    z_expr = "min(zoom+0.00035,1.05)"
    x_expr = "iw/2-(iw/zoom/2)"
    y_expr = f"ih/2-(ih/zoom/2)+{bounce}*sin(2*PI*on/{FPS})"
    vf = (
        f"zoompan=z='{z_expr}':x='{x_expr}':y='{y_expr}':d={frames}:s={W}x{H}:fps={FPS},"
        f"format=rgba[bg];"
        f"[1:v]format=rgba[ly];"
        f"[bg][ly]overlay=(W-w)/2:H-h-{LYRIC_BOTTOM_PAD}:format=auto,format=yuv420p"
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
    n = len(segments)
    seg_dur = (DURATION + (n - 1) * fade) / n
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


async def main(fmt: str = "landscape", reuse_audio: bool = True) -> None:
    configure(fmt)
    ensure_dirs()
    print(f"Format: {FORMAT_NAME} ({W}x{H})")

    melody = AUDIO / "melody.wav"
    vocals = AUDIO / "vocals.wav"
    mixed = AUDIO / "mixed.wav"

    if reuse_audio and mixed.exists():
        print("1-3/5 Reusing existing mixed audio…")
    else:
        print("1/5 Melody…")
        make_melody(melody)
        print("2/5 Vocals…")
        await make_vocals(vocals)
        print("3/5 Mix audio…")
        mix_audio(melody, vocals, mixed)

    print("4/5 Prepare sources + segments…")
    sources = prepare_sources()
    fade = 0.6
    n = len(sources)
    seg_dur = (DURATION + (n - 1) * fade) / n
    segments: list[Path] = []
    for i, src in enumerate(sources):
        seg = CLIPS / f"seg_{i}.mp4"
        print(f"  segment {i + 1}/{len(sources)} ({seg_dur:.2f}s)")
        make_segment(src, LYRICS / f"lyric_{i}.png", seg, seg_dur)
        segments.append(seg)

    print("5/5 Concat + mux…")
    out = OUT / OUTPUT_NAME
    concat_and_mux(segments, mixed, out)
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
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--format",
        choices=("landscape", "reel"),
        default="landscape",
        help="landscape 16:9 or reel 9:16",
    )
    parser.add_argument(
        "--fresh-audio",
        action="store_true",
        help="Regenerate melody/vocals instead of reusing mixed.wav",
    )
    args = parser.parse_args()
    asyncio.run(main(fmt=args.format, reuse_audio=not args.fresh_audio))

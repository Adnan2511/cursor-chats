# Friends in the Meadow

A 30-second, 16:9 toddler nursery-rhyme video featuring three original characters:
a cheerful yellow duckling, a friendly floppy-eared bunny, and a smiling baby elephant.

## Lyrics

1. Duckling, bunny, elephant too  
2. Dancing in the meadow with you  
3. Bounce and clap and shout with me  
4. Friends forever — one, two, three!  
5. Rainbow smiles for you and me  
6. Happy friends — that's you and me!

## Rebuild

```bash
export PATH="$HOME/.local/bin:$PATH"
pip3 install --user edge-tts numpy pillow
python3 build_video.py
```

Output: `/opt/cursor/artifacts/friends-in-the-meadow.mp4`

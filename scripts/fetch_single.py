import sys, re
from pathlib import Path
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url):
    for pattern in [r'v=([\w-]{11})', r'youtu\.be/([\w-]{11})']:
        m = re.search(pattern, url)
        if m:
            return m.group(1)
    return None

def main():
    if len(sys.argv) < 2:
        print("Keine URL angegeben")
        return
    url = sys.argv[1].strip()
    video_id = extract_video_id(url)
    print(f"Video ID: {video_id}")
    if not video_id:
        print("Ungueltige URL")
        return
    print("Lade Transkript...")
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id)
        text = " ".join([x.text for x in transcript])
        print(f"Geladen: {len(text)} Zeichen")
    except Exception as e:
        print(f"FEHLER: {e}")
        return
    out = Path("knowledge/videos")
    out.mkdir(parents=True, exist_ok=True)
    f = out / f"video_{video_id}.txt"
    f.write_text(f"URL: {url}\nDatum: {datetime.now().strftime('%Y-%m-%d')}\n\n{text}", encoding="utf-8")
    print(f"Gespeichert: {f.name}")

if __name__ == "__main__":
    main()
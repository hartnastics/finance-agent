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
    print(f"URL: {url}")
    video_id = extract_video_id(url)
    print(f"Video ID: {video_id}")
    if not video_id:
        print("Ungueltige URL")
        return
    print("Versuche Transkript zu laden...")
    try:
        data = YouTubeTranscriptApi.get_transcript(video_id, languages=['de','en'])
        print(f"Transkript geladen: {len(data)} Segmente")
        text = " ".join([x['text'] for x in data])
        print(f"Text Laenge: {len(text)} Zeichen")
    except Exception as e:
        print(f"FEHLER beim Laden: {e}")
        return
    out = Path("knowledge/videos")
    out.mkdir(parents=True, exist_ok=True)
    f = out / f"video_{video_id}.txt"
    f.write_text(f"URL: {url}\n\n{text}", encoding="utf-8")
    print(f"Datei gespeichert: {f.name}")
    print(f"Dateipfad: {f.resolve()}")

if __name__ == "__main__":
    main()
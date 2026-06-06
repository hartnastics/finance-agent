import sys, re
from pathlib import Path
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def extract_video_id(url):
    for pattern in [r'v=([\w-]{11})', r'youtu\.be/([\w-]{11})', r'shorts/([\w-]{11})']:
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

    if not video_id:
        print(f"Ungueltige URL: {url}")
        return

    print(f"Lade Transkript fuer: {video_id}")

    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(
            video_id, languages=['de', 'en', 'de-DE', 'en-US', 'en-GB']
        )
        text = TextFormatter().format_transcript(transcript_list)
    except Exception as e:
        print(f"Kein Transkript verfuegbar: {e}")
        return

    output_dir = Path("knowledge/videos")
    output_dir.mkdir(parents=True, exist_ok=True)

    safe_id = re.sub(r"[^\w\s-]", "", video_id)
    fname = output_dir / f"video_{video_id}_{datetime.now().strftime('%Y-%m-%d')}.txt"

    fname.write_text(
        f"# Video: {video_id}\nURL: {url}\nDatum: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n{'='*60}\n\n{text}",
        encoding="utf-8"
    )
    print(f"Gespeichert: {fname.name}")
    words = len(text.split())
    print(f"Laenge: {words} Woerter")

if __name__ == "__main__":
    main()
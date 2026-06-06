import sys, re
from pathlib import Path
from datetime import datetime
import yt_dlp, webvtt

def extract_video_id(url):
    for pattern in [r'v=([\w-]{11})', r'youtu\.be/([\w-]{11})', r'shorts/([\w-]{11})']:
        m = re.search(pattern, url)
        if m: return m.group(1)
    return None

def main():
    if len(sys.argv) < 2:
        print("Keine URL angegeben"); return
    url = sys.argv[1]
    video_id = extract_video_id(url)
    if not video_id:
        print(f"Ungueltige URL: {url}"); return
    try:
        with yt_dlp.YoutubeDL({"quiet":True}) as ydl:
            info = ydl.extract_info(f"https://youtube.com/watch?v={video_id}", download=False)
        title   = info.get("title", video_id)
        channel = info.get("uploader", "Unbekannt")
    except Exception:
        title, channel = video_id, "Unbekannt"
    print(f"Lade: {title}")
    tmp = f"/tmp/single_{video_id}"
    ydl_opts = {"skip_download":True,"writeautomaticsub":True,"writesubtitles":True,
                "subtitleslangs":["de","en"],"subtitlesformat":"vtt","outtmpl":tmp,"quiet":True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"https://youtube.com/watch?v={video_id}"])
    transcript = None
    for lang in ["de","en"]:
        vtt_file = Path(f"{tmp}.{lang}.vtt")
        if not vtt_file.exists():
            matches = list(Path("/tmp").glob(f"single_{video_id}*.vtt"))
            if matches: vtt_file = matches[0]
            else: continue
        try:
            seen, captions = set(), []
            for c in webvtt.read(str(vtt_file)):
                t = c.text.replace("\n"," ").strip()
                if t and t not in seen:
                    seen.add(t); captions.append(t)
            vtt_file.unlink(missing_ok=True)
            transcript = " ".join(captions); break
        except Exception:
            vtt_file.unlink(missing_ok=True)
    if not transcript:
        print("Kein Transkript verfuegbar"); return
    output_dir = Path("knowledge/videos")
    output_dir.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^\w\s-]","",title)[:60].strip()
    fname = output_dir / f"{channel}_{video_id}_{safe}.txt"
    fname.write_text(
        f"# {title}\nKanal: {channel}\nURL: {url}\nDatum: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n{'='*60}\n\n{transcript}",
        encoding="utf-8")
    print(f"Gespeichert: {fname.name}")

if __name__ == "__main__":
    main()
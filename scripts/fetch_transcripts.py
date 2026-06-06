import os, json, re
from datetime import datetime
from pathlib import Path
import yaml, yt_dlp, webvtt

def get_channel_videos(channel_id, max_videos=3):
    ydl_opts = {"quiet":True, "extract_flat":True, "playlist_end":max_videos}
    url = f"https://www.youtube.com/channel/{channel_id}/videos"
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return [(v["id"], v["title"]) for v in info.get("entries",[]) if v]

def get_transcript(video_id):
    tmp = f"/tmp/transcript_{video_id}"
    ydl_opts = {
        "skip_download": True,
        "writeautomaticsub": True,
        "writesubtitles": True,
        "subtitleslangs": ["de","en"],
        "subtitlesformat": "vtt",
        "outtmpl": tmp,
        "quiet": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"https://youtube.com/watch?v={video_id}"])
    for lang in ["de","en"]:
        vtt_file = Path(f"{tmp}.{lang}.vtt")
        if not vtt_file.exists():
            matches = list(Path("/tmp").glob(f"transcript_{video_id}*.vtt"))
            if matches: vtt_file = matches[0]
            else: continue
        try:
            seen, captions = set(), []
            for c in webvtt.read(str(vtt_file)):
                t = c.text.replace("\n"," ").strip()
                if t and t not in seen:
                    seen.add(t); captions.append(t)
            vtt_file.unlink(missing_ok=True)
            return " ".join(captions)
        except Exception as e:
            print(f"  Fehler: {e}")
            vtt_file.unlink(missing_ok=True)
    return None

def already_downloaded(video_id, output_dir):
    return any(True for _ in Path(output_dir).rglob(f"*{video_id}*.txt"))

def main():
    with open("channels.yml") as f:
        config = yaml.safe_load(f)
    output_dir = "knowledge/videos"
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    downloaded, log = 0, []
    for channel in config.get("channels",[]):
        name, cid = channel["name"], channel["id"]
        print(f"\nKanal: {name}")
        try: videos = get_channel_videos(cid, config.get("max_videos_per_run",3))
        except Exception as e: print(f"  Fehler: {e}"); continue
        for video_id, title in videos:
            if already_downloaded(video_id, output_dir):
                print(f"  Bereits vorhanden: {title[:40]}"); continue
            print(f"  Lade: {title[:50]}...")
            transcript = get_transcript(video_id)
            if transcript:
                safe = re.sub(r"[^\w\s-]","",title)[:60].strip()
                fname = f"{output_dir}/{name}_{video_id}_{safe}.txt"
                with open(fname,"w",encoding="utf-8") as f:
                    f.write(f"# {title}\nKanal: {name}\nDatum: {datetime.now().strftime('%Y-%m-%d')}\n{'='*60}\n\n{transcript}")
                print(f"  Gespeichert!"); downloaded += 1
                log.append({"kanal":name,"titel":title})
    with open(f"knowledge/videos/_log_{datetime.now().strftime('%Y-%m-%d')}.json","w") as f:
        json.dump({"neue_videos":downloaded,"details":log},f,ensure_ascii=False,indent=2)
    print(f"\nFertig! {downloaded} neue Transkripte.")

if __name__ == "__main__":
    main()
import yt_dlp

video_url = "https://youtu.be/e6Po2lDHD1I?si=E3FsW_5Mey8GsFOB"

# Optional: Set download options
ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',  # Save file as video title
    'format': 'bestvideo/best',  # Best quality
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])


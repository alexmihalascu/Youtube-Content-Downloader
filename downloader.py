from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

def download_video(url, resolution, download_path):
    yt = YouTube(url)
    stream = yt.streams.filter(res=resolution, file_extension='mp4').first()
    if not stream:
        raise Exception(f"No video stream found with resolution {resolution}")
    video_path = stream.download(output_path=download_path)
    return video_path

def convert_to_mp3(video_path):
    video_clip = VideoFileClip(video_path)
    audio_path = video_path.replace(".mp4", ".mp3")
    video_clip.audio.write_audiofile(audio_path)
    video_clip.close()
    return audio_path

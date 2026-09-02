import subprocess
import os

def merge_audio_video(video_path: str, audio_path: str, output_path: str = "outputs/muxed_video.mp4") -> str:
    """
    Muxes the synchronized composite audio track with the base video file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-shortest",
        output_path
    ]
    
    subprocess.run(cmd, check=True)
    return output_path
import subprocess
import os

def apply_overlays_and_captions(
    video_path: str,
    logo_path: str,
    cta_path: str,
    subtitles_path: str,
    output_path: str = "outputs/final_enhanced_video.mp4"
) -> str:
    """
    Applies a brand logo, a CTA button overlay, and burned-in karaoke-style captions 
    using FFmpeg complex filter graphs.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    filter_complex = (
        "[1:v]scale=120:-1[logo];"
        "[2:v]scale=300:-1[cta];"
        "[0:v][logo]overlay=10:10[vid1];"
        "[vid1][cta]overlay=(W-w)/2:H-h-50[vid2];"
        f"[vid2]subtitles={subtitles_path}[outv]"
    )
    
    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-i", logo_path,
        "-i", cta_path,
        "-filter_complex", filter_complex,
        "-map", "[outv]",
        "-map", "0:a",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-c:a", "copy",
        output_path
    ]
    
    subprocess.run(cmd, check=True)
    return output_path
import subprocess
import os

def mix_audio_tracks(vo_path: str, bgm_path: str, output_path: str = "outputs/composite_audio.mp3") -> str:
    """
    Loops background music (BGM) to match the exact duration of the voiceover (VO) track,
    lowers BGM volume for ducking, and mixes them into a single audio file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    probe_cmd = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", vo_path
    ]
    vo_duration = float(subprocess.check_output(probe_cmd).decode().strip())
    
    filter_complex = (
        f"[1:a]aloop=loop=-1:size=2e+09,atrim=0:{vo_duration},volume=0.2[bgm_looped];"
        f"[0:a][bgm_looped]amix=inputs=2:duration=first:dropout_transition=2[out]"
    )
    
    cmd = [
        "ffmpeg", "-y",
        "-i", vo_path,
        "-i", bgm_path,
        "-filter_complex", filter_complex,
        "-map", "[out]",
        output_path
    ]
    
    subprocess.run(cmd, check=True)
    return output_path
from src.audio_mixer import mix_audio_tracks
from src.video_muxer import merge_audio_video
from src.video_enhancer import apply_overlays_and_captions

def main():
    print("Starting Automated Video Production Pipeline...")
    
    vo_file = "assets/audio/voiceover.mp3"
    bgm_file = "assets/audio/background_music.mp3"
    base_video = "assets/images/base_footage.mp4"
    logo_file = "assets/images/logo.png"
    cta_file = "assets/images/cta_button.png"
    subs_file = "assets/fonts/captions.ass"
    
    print("Step 1: Processing and mixing audio tracks...")
    composite_audio = mix_audio_tracks(vo_path=vo_file, bgm_path=bgm_file)
    
    print("Step 2: Muxing composite audio with base video...")
    temp_video = merge_audio_video(video_path=base_video, audio_path=composite_audio)
    
    print("Step 3: Injecting branding, CTA, and karaoke captions...")
    final_output = apply_overlays_and_captions(
        video_path=temp_video,
        logo_path=logo_file,
        cta_path=cta_file,
        subtitles_path=subs_file
    )
    
    print(f"Pipeline complete! Final video saved to: {final_output}")

if __name__ == "__main__":
    main()
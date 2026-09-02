# Video Automation Toolkit

A programmatic video production and editing pipeline built with Python and FFmpeg. This toolkit automates complex multimedia processing tasks—from dynamic audio length-matching to programmatic overlay injection and karaoke-style subtitle synchronization—ideal for scaled content creation and marketing automation.

## Project Structure

```text
video-automation-toolkit/
├── assets/
│   ├── fonts/
│   ├── images/
│   └── audio/
├── src/
│   ├── __init__.py
│   ├── audio_mixer.py     # Use Case 1: Loop BGM & mix with VO
│   ├── video_muxer.py     # Use Case 2: Merge audio track with base video
│   └── video_enhancer.py  # Use Case 3: Hooks, CTA, logo, & karaoke captions
├── outputs/
├── config.json            # Configuration parameters
├── main.py
├── requirements.txt
└── README.md
## Core Features

### 1. Intelligent Audio Looping & Mixing (`audio_mixer.py`)
Handles mismatched audio durations by automatically looping background music (BGM) to match the exact length of a voiceover (VO) track, applying ducking or volume balancing, and merging them into a single synchronized audio stream using FFmpeg filter graphs (`amix`, `aloop`, and duration truncation flags).

### 2. Audio-Video Muxing (`video_muxer.py`)
Synchronizes and binds the processed composite audio track (VO + BGM) with the primary video asset, executing precise stream mapping (`-map 0:v -map 1:a`) with container-level stream copying (`-c:v copy`).

### 3. Dynamic Overlay & Karaoke Caption Generation (`video_enhancer.py`)
Transforms raw video assets into engagement-optimized content by programmatically injecting opening hooks, graphic CTA button overlays via coordinate mapping, brand watermarks with transparency management, and synced karaoke-style subtitles using Advanced SubStation Alpha (ASS) specifications.

## Prerequisites

* **Python 3.10+**
* **FFmpeg** installed and accessible in your system's PATH.

Verify your FFmpeg installation:
```bash
ffmpeg -version

## Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/trongnguyenh/video-automation-toolkit.git](https://github.com/trongnguyenh/video-automation-toolkit.git)
   cd video-automation-toolkit

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
Configure your assets and settings in `config.json`, then run the main orchestration script:

```bash
python main.py

## License
Distributed under the MIT License. See `LICENSE` for more information.


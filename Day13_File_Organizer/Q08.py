# Write a program that separates video and audio files.

# Requirements:

# Move videos into Videos.

# Move audio files into Audio.

# Support multiple extensions for each category.


#------------------------------------------------------------------------------------------


from pathlib import Path
import shutil

# Specify the directory
directory = Path("MyFiles")
directory.mkdir(parents=True, exist_ok=True)

# Supported extensions
video_extensions = {".mp4", ".mkv", ".avi", ".mov", ".wmv"}
audio_extensions = {".mp3", ".wav", ".aac", ".flac", ".ogg"}

# Create destination folders
videos_folder = directory / "Videos"
audio_folder = directory / "Audio"

videos_folder.mkdir(exist_ok=True)
audio_folder.mkdir(exist_ok=True)

# Separate video and audio files
for file in directory.iterdir():

    if not file.is_file():
        continue

    extension = file.suffix.lower()

    if extension in video_extensions:
        shutil.move(str(file), str(videos_folder / file.name))
        print(f"Video moved: {file.name}")

    elif extension in audio_extensions:
        shutil.move(str(file), str(audio_folder / file.name))
        print(f"Audio moved: {file.name}")

print("Video and audio files organized successfully!")

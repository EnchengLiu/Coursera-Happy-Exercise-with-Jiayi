# Using FFmpeg to convert local files from M3U8 to MP4 format
# Please install FFmpeg(executable files) before running this script
# May need to check the path of /.ts files in the m3u8 file, if the path is not correct, please modify the path by connvert_m3u8_index_to_local_file.py

import os
import subprocess

def sanitize_filename(name: str) -> str:
    # Remove dots from the filename
    for char in ['.']:
        if char in name:
            name = name.split(char)[0]
    return name

def convert_m3u8_to_mp4(m3u8_path: str, output_dir: str):
    # Get the directory name and generate the output filename
    dir_name = os.path.basename(os.path.dirname(m3u8_path))
    output_name = sanitize_filename(m3u8_path) + '.mp4'
    output_file = os.path.join(output_dir, output_name)

    # Full path to ffmpeg executable
    ffmpeg_path = r'E:\Download\ffmpeg-7.0.2-essentials_build\ffmpeg-7.0.2-essentials_build\bin\ffmpeg.exe'  # Update this path to the location of ffmpeg.exe

    # Call FFmpeg command to convert M3U8 to MP4
    command = [
        ffmpeg_path,
        '-allowed_extensions', 'ALL',  # Allow all file extensions
        '-i', m3u8_path,
        '-c', 'copy',  # Directly copy the stream without re-encoding
        '-bsf:a', 'aac_adtstoasc',  # Convert audio format
        output_file
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Converted {m3u8_path} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert {m3u8_path}: {e}")

def traverse_and_convert(root_folder: str):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.m3u8'):
                m3u8_path = os.path.join(dirpath, filename)
                convert_m3u8_to_mp4(m3u8_path, root_folder)

def main():
    root_folder = r'F:\Download'
    traverse_and_convert(root_folder)

if __name__ == "__main__":
    main()
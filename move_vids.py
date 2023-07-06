import os
from tqdm import tqdm

# Source directory containing folders starting with '#'
source_dir = 'D:/TikTok_Videos'

# Destination directory to store the selected videos
destination_dir = 'D:/TikTok_Videos/data/videos'

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Get all subdirectories starting with '#'
subdirectories = [d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, d)) and d.startswith('#')]

# Iterate over each subdirectory
for subdirectory in tqdm(subdirectories, desc='Processing folders', unit='folder'):
    # Get the path of the subdirectory
    subdirectory_path = os.path.join(source_dir, subdirectory)
    
    # Get all video files in the subdirectory
    video_files = [f for f in os.listdir(subdirectory_path) if os.path.isfile(os.path.join(subdirectory_path, f)) and f.endswith('.mp4')]
    
    # Iterate over each video file
    for video_file in tqdm(video_files, desc=subdirectory, unit='video'):
        # Get the source path of the video file
        source_path = os.path.join(subdirectory_path, video_file)
        
        # Generate the destination path of the video file
        destination_path = os.path.join(destination_dir, video_file)
        
        # Check if the file already exists in the destination directory
        if not os.path.exists(destination_path):
            try:
                # Move the video file to the destination directory
                os.rename(source_path, destination_path)
            except Exception as e:
                # Print the error message and continue to the next file
                print(f"Error moving {video_file}: {str(e)}")
        else:
            print(f"Skipping {video_file} as it already exists in the destination directory")

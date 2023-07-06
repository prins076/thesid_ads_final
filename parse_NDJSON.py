import os
import json

directory_path = 'D:\TikTok_Videos'

# Iterate over each folder in the directory
for folder_name in os.listdir(directory_path):
    folder_path = os.path.join(directory_path, folder_name)

    # Check if the item in the directory is a folder
    if os.path.isdir(folder_path):
        ndjson_filename = os.path.join(folder_path, f'{folder_name}.ndjson')
        json_filename = os.path.join(folder_path, f'{folder_name}.json')

        data = []

        # Read the NDJSON file
        with open(ndjson_filename, 'r') as file:
            for line in file:
                video_metadata = json.loads(line)
                data.append(video_metadata)

        # Save data to JSON file
        with open(json_filename, 'w') as outfile:
            json.dump(data, outfile)

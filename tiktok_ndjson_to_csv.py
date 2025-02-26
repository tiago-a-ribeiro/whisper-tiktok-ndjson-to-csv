import os
import json
import csv

# Define the directories
json_folder = 'ndjsons'
csv_folder = 'csvs'

# Create the csvs folder if it doesn't exist
if not os.path.exists(csv_folder):
    os.makedirs(csv_folder)

# Loop through all JSON files in the json_folder
count = 0
for json_filename in os.listdir(json_folder):
    if json_filename.endswith('.ndjson'):
        json_path = os.path.join(json_folder, json_filename)
        

        # Read the JSON file
        csv_filename = json_filename.replace('.ndjson', '.csv')
        csv_path = os.path.join(csv_folder, csv_filename)

        with open(csv_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["id", "url", "whisper_text"])

            with open(json_path, 'r') as json_file:
                for line in json_file:
                    full_obj = line[10:]
                    

                    tiktok_text = full_obj.split('", "segments"')[0]
                    if tiktok_text[0] == " ":
                        tiktok_text = tiktok_text[1:]
                    audio_id = full_obj.split('{"audio_id": "video-downloader-tiktok-697cd5e77162569e501afeebf032bfb3')[1][:19]
                    
                    writer.writerow([audio_id, f"https://www.tiktok.com/@x/video/{audio_id}", tiktok_text])
        count += 1

import ctypes  # An included library with Python install.   
ctypes.windll.user32.MessageBoxW(0, f"{count} file{"s have" if count > 1 else " has"} been converted from NDJson to CSV.", "Tiktok Jsons to CSVs", 1)
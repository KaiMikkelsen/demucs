#!/bin/bash

# Define the path where the song files are located
data_path="../data/MUSDB18/test"
echo "separating tracks located in $data_path"

# Iterate through each .mp3 file in the data_path directory
for song_file in "$data_path"/*.mp4; do
  # Call demucs on each song file
  echo "$song_file"
  demucs "$song_file"
done

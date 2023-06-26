import os
import time

def save_transcription(transcription):
    """transcription => giving text
    saves it into a .txt file"""
    time_stamp = str(int(time.time()))
    file_name = f"{time_stamp}.txt"
    
    file_path = os.path.join("./")

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    path_file = os.path.join(file_path, file_name)

    with open(path_file, "w") as file:
        file.write(transcription)


import os
import shutil
import random

# Definieer de paden
SOURCE_DIR = "/Users/mariejatsun/Desktop/Soundwel Dataset - Audio and Spectrograms"
TRAIN_DIR = "/Users/mariejatsun/Desktop/Projectwerk/DATA/train"
TEST_DIR = "/Users/mariejatsun/Desktop/Projectwerk/DATA/test"

# Maak de doelmappen aan als ze niet bestaan
os.makedirs(TRAIN_DIR, exist_ok=True)
os.makedirs(TEST_DIR, exist_ok=True)

# Zoek alle .wav bestanden
wav_files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(".wav")]

# Controleer of er bestanden zijn
if not wav_files:
    print(f"Geen .wav bestanden gevonden in {SOURCE_DIR}")
    exit()

# Schud de bestanden willekeurig
random.shuffle(wav_files)

# Bereken het splitsingspunt (80%-20%)
split_index = int(0.8 * len(wav_files))
train_files = wav_files[:split_index]
test_files = wav_files[split_index:]

# Functie om bestanden te kopiëren
def copy_files(file_list, destination):
    for file in file_list:
        src_path = os.path.join(SOURCE_DIR, file)
        dest_path = os.path.join(destination, file)
        shutil.copy2(src_path, dest_path)

# Kopieer de bestanden
copy_files(train_files, TRAIN_DIR)
copy_files(test_files, TEST_DIR)

# Print het resultaat
print(f"Bestanden succesvol gesplitst: {len(train_files)} naar train, {len(test_files)} naar test.")

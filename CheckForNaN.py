import os
import json
import numpy as np

# Paden naar de train en test folders
TRAIN_DIR = "/Users/mariejatsun/Desktop/Projectwerk/DATA/train"
TEST_DIR = "/Users/mariejatsun/Desktop/Projectwerk/DATA/test"

def check_and_remove_nan_json(folder_path):
    """Controleert alle JSON-bestanden in de map op NaN-waarden en verwijdert ze samen met het bijbehorende WAV-bestand."""
    removed_count = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):  # Controleer alleen JSON-bestanden
            file_path = os.path.join(folder_path, filename)
            wav_file_path = os.path.join(folder_path, filename.replace(".json", ".wav"))
            
            try:
                with open(file_path, "r") as file:
                    data = json.load(file)
                
                # Controleer op NaN in JSON
                has_nan = any(
                    isinstance(value, list) and any(isinstance(x, float) and np.isnan(x) for x in value)
                    or (isinstance(value, float) and np.isnan(value))
                    for value in data.values()
                )
                
                if has_nan:
                    os.remove(file_path)  # Verwijder JSON
                    if os.path.exists(wav_file_path):
                        os.remove(wav_file_path)  # Verwijder bijbehorende WAV indien deze bestaat
                    removed_count += 1
                    print(f"🗑️ Verwijderd: {filename} en bijbehorende WAV")
            
            except json.JSONDecodeError:
                print(f"❌ Fout bij het lezen van {filename}: Ongeldige JSON")
            except Exception as e:
                print(f"❌ Onverwachte fout bij {filename}: {e}")
    return removed_count

def count_files(folder_path, extension):
    """Tel het aantal bestanden met een bepaalde extensie in een map."""
    return len([f for f in os.listdir(folder_path) if f.endswith(extension)])

# Controleer en verwijder foute bestanden
print("🔍 Controleren en verwijderen in TRAIN folder...")
removed_train = check_and_remove_nan_json(TRAIN_DIR)
print("🔍 Controleren en verwijderen in TEST folder...")
removed_test = check_and_remove_nan_json(TEST_DIR)

# Tel resterende bestanden
train_wav_count = count_files(TRAIN_DIR, ".wav")
train_json_count = count_files(TRAIN_DIR, ".json")
test_wav_count = count_files(TEST_DIR, ".wav")
test_json_count = count_files(TEST_DIR, ".json")

# Print eindresultaat
print("Verwijdering voltooid.")
print(f"TRAIN: {train_wav_count} WAV-bestanden, {train_json_count} JSON-bestanden")
print(f"TEST: {test_wav_count} WAV-bestanden, {test_json_count} JSON-bestanden")
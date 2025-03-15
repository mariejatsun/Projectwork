import os
import pandas as pd
import json

# Paden
EXCEL_FILE = "/Users/mariejatsun/Desktop/SoundwelDatasetKey.xlsx"
TEST_DIR = "/Users/mariejatsun/Desktop/Projectwerk/DATA/test"

# Lees de Excel in
df = pd.read_excel(EXCEL_FILE)

# Zorg ervoor dat kolomnamen correct zijn
REQUIRED_COLUMNS = ["Audio Filename", "Dur", "Valence"]
if not all(col in df.columns for col in REQUIRED_COLUMNS):
    raise ValueError(f"De Excel moet de volgende kolommen bevatten: {REQUIRED_COLUMNS}")

# Loop door de bestanden in de train-map
for filename in os.listdir(TEST_DIR):
    if filename.endswith(".wav"):
        base_name = os.path.splitext(filename)[0]  # Verwijder .wav
        json_filename = f"{base_name}.json"
        json_path = os.path.join(TEST_DIR, json_filename)

        # Zoek de metadata in de Excel
        row = df[df["Audio Filename"] == filename]
        if row.empty:
            print(f"Waarschuwing: Geen metadata gevonden voor {filename}")
            continue

        # Extract data
        duration = float(row["Dur"].values[0])  # Onset = 0, Offset = Duration
        cluster = row["Valence"].values[0]  # Pos of Neg

        # Maak JSON-structuur
        annotation = {
            "onset": [0],
            "offset": [duration],
            "cluster": [cluster]
        }

        # Sla de JSON op
        with open(json_path, "w") as json_file:
            json.dump(annotation, json_file, indent=4)

        print(f"JSON installed: {json_filename}")

print("all JSONs installed")

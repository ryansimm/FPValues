import json
from datetime import datetime
from pathlib import Path

import requests

URL = "https://fantasy.premierleague.com/api/bootstrap-static/"
RAW_DIR = Path("data/raw")

def fetch_bootstrap () -> dict:
    """Fetches the bootstrap data from the FPL API and returns it as a dictionary."""
    response = requests.get(URL , timeout=30)
    response.raise_for_status()
    return response.json()

def save_raw(data:dict) -> Path:
    """Saves the raw data to a JSON file in the RAW_DIR directory."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d")
    file_path = RAW_DIR / f"bootstrap_{timestamp}.json"
    file_path.write_text(json.dumps(data))
    return file_path

if __name__ == "__main__":
    data = fetch_bootstrap()
    file_path = save_raw(data)
    print(f"Saved {len(data['elements'])} players to {file_path}")
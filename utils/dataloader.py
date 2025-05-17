import csv
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path(__file__).parent.parent / "Data" / "Data.csv"
MENU_FILE = Path(__file__).parent.parent / "Data" / "Menu.csv"

def load_data() -> List[Dict]:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Data file not found at path: {DATA_FILE}")

    with open(DATA_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def load_veg_starters() -> List[str]:
    if not MENU_FILE.exists():
        raise FileNotFoundError(f"Menu file not found at path: {MENU_FILE}")

    with open(MENU_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            veg_starters = eval(row["menu.veg.starters"])  # Convert string to list
            return veg_starters
    return []
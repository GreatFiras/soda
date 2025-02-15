import json
import os

def ensure_json_file_exists(file_path):
    """Creates an empty JSON file if it doesn't exist."""
    if not os.path.exists(file_path):
        print(f"🔍 Creating missing JSON file: {file_path}")
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4, ensure_ascii=False)

def load_json(file_path):
    """Load JSON safely, ensuring the file exists first."""
    ensure_json_file_exists(file_path)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"❌ JSON Decode Error: {e}")
        return []

def save_json(file_path, data):
    """Save data to a JSON file, ensuring it exists first."""
    ensure_json_file_exists(file_path)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

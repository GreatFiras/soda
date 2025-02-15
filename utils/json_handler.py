import json
import os

def load_json(file_path, env_var=None):
    """Load data from a JSON file or environment variable if available."""
    # Check if JSON data exists in environment variables (for Render)
    if env_var and env_var in os.environ:
        try:
            return json.loads(os.environ[env_var])  # Load from env variable
        except json.JSONDecodeError:
            print(f"❌ Failed to load JSON from environment variable: {env_var}")
            return []

    # Load from file if no environment variable
    if not os.path.exists(file_path):
        print(f"❌ File {file_path} not found.")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"❌ Error loading JSON from {file_path}: {e}")
        return []

def save_json(file_path, data):
    """Save data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


import os
import json
import yaml
import re
import secrets
import string
import sys
from collections import defaultdict

def find_yaml_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        if 'defaults' in root and 'main.yml' in files:
            yield os.path.join(root, 'main.yml')

def merge_yaml_files(files):
    merged_data = defaultdict(dict)
    for file in files:
        with open(file, 'r') as f:
            data = yaml.safe_load(f)
            # role_name = os.path.basename(os.path.dirname(os.path.dirname(file)))
            # merged_data[role_name].update(data)
            merged_data.update(data)
    return dict(merged_data)

def generate_random_string(length):
    """Generate a random string of specified length."""
    # Create a string containing all ASCII letters and digits
    characters = string.ascii_letters + string.digits + '!+-_'
    # Use secrets.choice to ensure secure random selection of characters
    random_string = ''.join(secrets.choice(characters) for i in range(length))
    return random_string

def load_data(file_path):
    """Load data from a JSON or YAML file based on its extension."""
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            return json.load(file)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    else:
        raise ValueError("Unsupported file extension. Please use a JSON or YAML file.")

def save_data(data, file_path):
    """Save data to a JSON or YAML file based on its extension."""
    if file_path == "-":
        yaml.dump(data, sys.stdout, default_flow_style=False)
    elif file_path.endswith('.json'):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
    else:
        raise ValueError("Unsupported file extension. Please use a JSON or YAML file.")

def replace_secrets(data, marker_regex=r"\{\{SECRET:(\d+)\}\}"):
    """Recursively replace markers in the data structure."""
    if isinstance(data, dict):
        return {k: replace_secrets(v, marker_regex) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_secrets(i, marker_regex) for i in data]
    elif isinstance(data, str):
        return re.sub(marker_regex, lambda x: generate_random_string(int(x.group(1))), data)
    return data

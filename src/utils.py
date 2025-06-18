import os

def load_cuisines(file_path="data/cuisines.txt"):
    """Loads a list of cuisines from a text file."""
    try:
        with open(file_path, "r") as f:
            cuisines = [line.strip() for line in f if line.strip()]
        return sorted(list(set(cuisines))) # Remove duplicates and sort
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Returning empty list.")
        return []

def load_styles(file_path="data/styles.txt"):
    """Loads a list of styles from a text file."""
    try:
        with open(file_path, "r") as f:
            styles = [line.strip() for line in f if line.strip()]
        return sorted(list(set(styles))) # Remove duplicates and sort
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Returning empty list.")
        return []
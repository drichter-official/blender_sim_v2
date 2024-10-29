import json
def load_transforms(filepath):
    with open(filepath, 'r') as f:
        transforms = json.load(f)
    return transforms
import json

def save_data(data):
    with open("candidates.json", "a") as f:
        json.dump(data, f)
        f.write("\n")
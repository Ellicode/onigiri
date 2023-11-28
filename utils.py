import json

class JsonFileManager:
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def __enter__(self):
        # Read the JSON file on entering the with block
        with open(self.filename, 'r') as file:
            self.data = json.load(file)
        return self.data

    def __exit__(self, exc_type, exc_value, traceback):
        # Write the modified data back to the JSON file on exiting the with block
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=2)

def LoadJson(path):
    with open(path, "r") as f:
        return json.load(f)
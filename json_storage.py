import json
import os

class JsonStorage:
    def init(self, filename="space_photo.json"):
        self.filename = filename

    # load
    def load_history(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r", encoding="utf-8") as f:   # "r" = read
            history = json.load(f)
        return history

    # save
    def save_entry(self, entry: dict):
        history = self.load_history()
        history.append(entry)
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(history, f)
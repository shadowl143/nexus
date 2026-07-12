import os
import json


class MultiLanguageService:
    def __init__(self, language="es_MX"):
        self.language = language

    def load_transaction(self) -> dict:
        local_path = os.path.join(
            "nexus_desktop", "tkinter", "locales", f"{self.language}.json"
        )
        with open(local_path, "r", encoding="utf-8") as file:
            return json.load(file)

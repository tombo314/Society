import json
from typing import Any

class FileOperation:
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path

    def read(self) -> Any:
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def write(self, data: Any) -> None:
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

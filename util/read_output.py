import json


def read_output(file_path: str = "./output.json") -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)
    return json_data

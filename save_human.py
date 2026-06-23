from human import Human
import json

def save_human(people: list[Human]):
    with open("database/human.json", "w", encoding="utf-8") as f:
        save_data: dict[str, dict[str, dict[str, str | int]]] = {"people": dict()}
        for human in people:
            save_data["people"][human.name] = dict()
            save_data["people"][human.name]["name"] = human.name
            save_data["people"][human.name]["money"] = human.money
        json.dump(save_data, f, indent=4, ensure_ascii=False)

from python.society.people.human import Human
import json

with open("database/residents.json", "r", encoding="utf-8") as f:
    residents_json = json.load(f)

residents_dict = residents_json["residents"]
residents: list[Human] = []

for name in residents_dict:
    money: int = residents_dict[name]["money"]
    resident = Human(name, money)
    residents.append(resident)

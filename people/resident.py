import json
from random import choice

from people.human import Human

class Resident:
    def __init__(self) -> None:
        self.INIT_MONEY: int = 10000
        with open("database/residents.json", "r", encoding="utf-8") as f:
            self.residents_json = json.load(f)
        self.residents_dict: dict[str, dict[str, int]] = self.residents_json["residents"]
        self.residents: list[Human] = []
        self._build()

    def _build(self) -> None:
        for name in self.residents_dict:
            money: int = self.residents_dict[name]["money"]
            resident = Human(name, money)
            self.residents.append(resident)

    def add_person(self) -> None:
        with open("database/name_candidate.json", "r", encoding="utf-8") as f:
            last_first_candidate = dict(json.load(f))["candidate"]
        last_candidate: list[str] = last_first_candidate["lastName"]
        first_candidate: list[str] = last_first_candidate["firstName"]
        last_selected: str = choice(last_candidate)
        first_selected: str = choice(first_candidate)
        name: str = last_selected + " " + first_selected
        person: dict[str, dict[str, dict[str, int]]] = {
            "residents": {
                name: {
                    "money": self.INIT_MONEY
                }
            }
        }
        with open("database/residents.json", "w") as f:
            json.dump(person, f, indent=4, ensure_ascii=False)

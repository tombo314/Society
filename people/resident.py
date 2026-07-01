import json
from random import choice

from people.human import Human

class Resident:
    def __init__(self) -> None:
        self.INIT_MONEY: int = 10000
        self.INIT_HUNGER: int = 100
        with open("database/residents.json", "r", encoding="utf-8") as f:
            self.residents_json = json.load(f)
        if len(self.residents_json["residents"]) == 0:
            self.add_people()
            with open("database/residents.json", "r", encoding="utf-8") as f:
                self.residents_json = json.load(f)
        self.residents_dict: dict[str, dict[str, int]] = self.residents_json["residents"]
        self.residents: list[Human] = []
        self._build()

    def _build(self) -> None:
        """ 住民一覧をメンバ変数として構築する """
        for name in self.residents_dict:
            money: int = self.residents_dict[name]["money"]
            hunger: int = self.residents_dict[name]["hunger"]
            resident = Human(name, money, hunger)
            self.residents.append(resident)

    def add_people(self) -> None:
        with open("database/name_candidate.json", "r", encoding="utf-8") as f:
            last_first_candidate = dict(json.load(f))["candidate"]
        last_candidate: list[str] = last_first_candidate["lastName"]
        first_candidate_male: list[str] = last_first_candidate["firstName"]["male"]
        first_candidate_female: list[str] = last_first_candidate["firstName"]["female"]

        # 名字と名前を1つずつ選んで、最初の住民1人を構築する
        # FIXME: 2人にして結婚できるようにする
        last_name: str = choice(last_candidate)
        first_name_male: str = choice(first_candidate_male)
        first_name_female: str = choice(first_candidate_female)
        male_name: str = last_name + " " + first_name_male
        female_name: str = last_name + " " + first_name_female
        person: dict[str, dict[str, dict[str, int]]] = {
            "residents": {
                male_name: {
                    "money": self.INIT_MONEY,
                    "hunger": self.INIT_HUNGER
                },
                female_name: {
                    "money": self.INIT_MONEY,
                    "hunger": self.INIT_HUNGER
                }
            }
        }
        with open("database/residents.json", "w") as f:
            json.dump(person, f, indent=4, ensure_ascii=False)

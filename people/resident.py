import json
from random import choice
from typing import TypedDict

from people.human import Human

class ResidentData(TypedDict):
    gender: str
    money: int
    satiety: int

class Resident:
    def __init__(self) -> None:
        self.INIT_MONEY: int = 10000
        self.INIT_SATIETY: int = 50
        with open("database/residents.json", "r", encoding="utf-8") as f:
            self.residents_json = json.load(f)
        if len(self.residents_json["residents"]) == 0:
            self.add_people()
            with open("database/residents.json", "r", encoding="utf-8") as f:
                self.residents_json = json.load(f)
        self.residents_dict: dict[str, ResidentData] = self.residents_json["residents"]
        self.residents: list[Human] = []
        self._build()

    def _build(self) -> None:
        """ 住民一覧をメンバ変数として構築する """
        for name in self.residents_dict:
            gender: str = self.residents_dict[name]["gender"]
            money: int = self.residents_dict[name]["money"]
            satiety: int = self.residents_dict[name]["satiety"]
            resident = Human(name, gender, money, satiety)
            self.residents.append(resident)

    def add_people(self) -> None:
        """ 名字と名前を1つずつ選んで、最初の住民1人を構築する """
        with open("database/name_candidate.json", "r", encoding="utf-8") as f:
            last_first_candidate = dict(json.load(f))["candidate"]
        last_candidate: list[str] = last_first_candidate["lastName"]
        first_candidate_male: list[str] = last_first_candidate["firstName"]["male"]
        first_candidate_female: list[str] = last_first_candidate["firstName"]["female"]

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
                    "satiety": self.INIT_SATIETY
                },
                female_name: {
                    "money": self.INIT_MONEY,
                    "satiety": self.INIT_SATIETY
                }
            }
        }
        with open("database/residents.json", "w") as f:
            json.dump(person, f, indent=4, ensure_ascii=False)

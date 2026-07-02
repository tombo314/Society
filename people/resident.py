import json
from random import choice
from typing import TypedDict

from people.human import Human
from const import *

class ResidentData(TypedDict):
    gender: str
    money: int
    satiety: int

class Resident:
    def __init__(self) -> None:
        FILE_PATH = "database/residents.json"
        try:
            # 住民ファイルを開く
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                self.residents_json = json.load(f)
            # 住民データが2人未満のとき、最初の住民2人を新しく作成する
            if len(self.residents_json["residents"]) < 2:
                self._init_people()
        except:
            # 住民ファイルが空のとき/破損しているとき、最初の住民2人を作成する
            self._init_people()

        # 住民データをロードする
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            self.residents_json = json.load(f)
            self.residents_dict: dict[str, ResidentData] = self.residents_json["residents"]

        # 外部公開用の住民リストを作る
        self.residents: list[Human] = []
        self._build()

    def get_residents(self) -> list[Human]:
        """ 住民のリストを取得する """
        return self.residents

    def _build(self) -> None:
        """ 外部公開用の住民リストを作る """
        for name in self.residents_dict:
            resident_data = self.residents_dict[name]
            gender: str = resident_data["gender"]
            money: int = resident_data["money"]
            satiety: int = resident_data["satiety"]
            resident: Human = Human(name, gender, money, satiety)
            self.residents.append(resident)

    def _select_from_candicate(self) -> list[str]:
        with open("database/name_candidate.json", "r", encoding="utf-8") as f:
            candidate = dict(json.load(f))["candidate"]
            last_name_candidate = candidate["lastName"]
            first_name_candidate = candidate["firstName"]
        
        # 名字をランダムに選ぶ
        last_name: str = choice(last_name_candidate)
        
        # 名前をランダムに選ぶ
        first_candidate_male: list[str] = first_name_candidate["male"]
        first_candidate_female: list[str] = first_name_candidate["female"]
        first_name_male: str = choice(first_candidate_male)
        first_name_female: str = choice(first_candidate_female)

        # 2人の名前を作成する
        male_name: str = last_name + " " + first_name_male
        female_name: str = last_name + " " + first_name_female

        return [male_name, female_name]

    def _init_people(self) -> None:
        """
        住民DBに誰もいない場合、名字と名前を1つずつ選んで、最初の住民2人を構築する
        """
        male_name, female_name = self._select_from_candicate()

        # 男女のペアを作成する
        primitive_pair: dict[str, dict[str, ResidentData]] = {
            "residents": {
                male_name: {
                    "money": INIT_MONEY,
                    "gender": GENDER_MALE,
                    "satiety" : INIT_SATIETY
                },
                female_name: {
                    "money": INIT_MONEY,
                    "gender": GENDER_MALE,
                    "satiety": INIT_SATIETY
                }
            }
        }

        # 最初の2人のデータをDBに書き込む
        with open("database/residents.json", "w") as f:
            json.dump(primitive_pair, f, indent=4, ensure_ascii=False)

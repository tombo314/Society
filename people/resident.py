from random import choice

from people.human import Human
from file_operation import FileOperation
import const

class Resident:
    def __init__(self) -> None:
        fo = FileOperation(const.FILE_PATH_RESIDENTS)
        try:
            # 住民ファイルを開く
            self.residents_json = fo.read()
            # 住民データが2人未満のとき、最初の住民2人を新しく作成する
            if len(self.residents_json["residents"]) < const.INIT_PEOPLE_NUM:
                self._init_people()
        except:
            # 住民ファイルが空のとき/破損しているとき、最初の住民2人を作成する
            self._init_people()

        # 住民データを取得する
        self.residents_json = fo.read()
        self.residents_dict: dict[str, dict[str, str | int]] = self.residents_json["residents"]

        # 外部公開用の住民リストを作る
        self.residents: list[Human] = []
        self._build()

    def get_residents(self) -> list[Human]:
        """ 住民のリストを取得する """
        return self.residents

    def _build(self) -> None:
        """ 外部公開用の住民リストを作る """
        for name in self.residents_dict:
            resident: Human = Human.from_dict(name, self.residents_dict[name])
            self.residents.append(resident)

    def _select_from_candicate(self) -> list[str]:
        fo = FileOperation(const.FILE_PATH_NAME_CANDIDATE)
        candidate = dict(fo.read())["candidate"]
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
        male = Human(
            male_name,
            const.GENDER_MALE,
            const.INIT_MONEY,
            const.INIT_SATIETY,
            const.INIT_AGE,
            const.INIT_DAYS_PASSED
        )
        female = Human(
            female_name,
            const.GENDER_MALE,
            const.INIT_MONEY,
            const.INIT_SATIETY,
            const.INIT_AGE,
            const.INIT_DAYS_PASSED
        )
        primitive_pair: dict[str, dict[str, dict[str, str | int]]] = {
            "residents": {
                male.name: male.to_dict(),
                female.name: female.to_dict(),
            }
        }

        # 最初の2人のデータをDBに書き込む
        fo = FileOperation(const.FILE_PATH_RESIDENTS)
        fo.write(primitive_pair)

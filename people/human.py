from const import *

class Human:
    def __init__(self, name: str, gender: str, money: int, satiety: int, age: int, days_passed: int) -> None:
        self.name: str = name
        self.gender: str = gender
        self.money: int = money
        self.satiety: int = satiety
        self.days_passed: int = days_passed
        self.action_log: str = ""
        self.parents: dict[str, str] = {"father": "", "mother": ""}
        self.childs: list[str] = []
        self.husband: str = ""
        self.wife: str = ""
        self.age: int = age

    def __repr__(self) -> str:
        return self.name

    def to_dict(self) -> dict[str, str | int]:
        """
        DB保存用のdictに変換する
        （nameはDBのキーに使うのでここには含めない）
        新しいメンバを永続化したいときは、ここと from_dict と __init__ に足すだけでよい
        """
        return {
            "gender": self.gender,
            "money": self.money,
            "satiety": self.satiety,
            "age": self.age,
            "days_passed": self.days_passed
        }

    @classmethod
    def from_dict(cls, name: str, data: dict[str, str | int]) -> "Human":
        """
        DBのdict（residents.jsonの1人分）からHumanを生成する
        古いDBに存在しないメンバは get() のデフォルト値で補う
        """
        return cls(
            name=name,
            gender=str(data.get("gender", GENDER_MALE)),
            money=int(data.get("money", INIT_MONEY)),
            satiety=int(data.get("satiety", INIT_SATIETY)),
            age=int(data.get("age", INIT_AGE)),
            days_passed=int(data.get("days_passed", INIT_DAYS_PASSED))
        )

    def show_status(self) -> None:
        print(f"{self} は {self.action_log}")
        print(f"まんぷく度: {self.satiety}")
        print(f"過ごした日: {self.days_passed}日")
        print(f"お金: {self.money}円")
        print("------------")

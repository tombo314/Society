from people.human import Human
from const import *

class Marriage():
    def __init__(self, husband: Human, wife: Human) -> None:
        self.husband: Human = husband
        self.wife: Human = wife

    def marriage(self) -> dict[str, Human]:
        self.husband.wife = self.wife.name
        self.wife.husband = self.husband.name
        return {
            "husband": self.husband,
            "wife": self.wife
        }

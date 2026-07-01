class Human:
    def __init__(self, name: str, money: int, hunger: int) -> None:
        self.name: str = name
        self.money: int = money
        self.hunger: int = hunger
        self.action_log: str = ""

    def __repr__(self) -> str:
        return self.name

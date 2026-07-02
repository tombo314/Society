class Human:
    def __init__(self, name: str, money: int, satiety: int) -> None:
        self.name: str = name
        self.money: int = money
        self.satiety: int = satiety
        self.action_log: str = ""

    def __repr__(self) -> str:
        return self.name

    def show_status(self) -> None:
        print(f"{self} は {self.action_log}")
        print(f"所持金: {self.money}円")
        print(f"満腹度: {self.satiety}")
        print("------------")

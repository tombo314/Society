class Human:
    def __init__(self, name: str, money: int) -> None:
        self.name: str = name
        self.money: int = money

    def __repr__(self) -> str:
        return f"名前: {self.name}"

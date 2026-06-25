from random import choice

class Action:
    def __init__(self) -> None:
        self.actions: list[str] = [
            "朝ご飯を食べた。"
        ]

    def get_random_action(self) -> str:
        return choice(self.actions)

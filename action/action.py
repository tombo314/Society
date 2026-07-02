from random import randint

from people.human import Human

class Action:
    def __init__(self) -> None:
        self.actions: list[str] = [
            "何もしなかった。",
            "朝ご飯を食べた。"
        ]

    def act_randomly(self, person: Human) -> Human:
        # 行動をランダムに決定する
        random_action_id = randint(0, len(self.actions) - 1)
        person.action_log = self.actions[random_action_id]
        person = self._act(person, random_action_id)
        return person

    def _act(self, person: Human, action_id: int) -> Human:
        match action_id:
            case 1:
                # 食事をする
                person = self.have_meal(person)
            case _:
                # 何もしない
                pass
        # 1行動で1日経過する
        person.days_passed += 1
        return person

    def have_meal(self, person: Human) -> Human:
        SATIETY_INCREMENT: int = 30
        SATIETY_LIMIT: int = 100
        person.satiety = min(SATIETY_LIMIT, person.satiety + SATIETY_INCREMENT)
        if person.satiety >= SATIETY_LIMIT:
            person.action_log += f"{person.name} はお腹いっぱいになった。"
        return person

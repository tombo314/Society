from random import randint

from people.human import Human

class Action:
    def __init__(self) -> None:
        # action_id: action
        self.actions: list[str] = [
            "何もしなかった",
            "朝ご飯を食べた。"
        ]

    def act_randomly(self, person: Human) -> Human:
        random_action_id = randint(0, len(self.actions) - 1)
        person = self._act(person, random_action_id)
        person.action_log = self.actions[random_action_id]
        return person

    def _act(self, person: Human, action_id: int) -> Human:
        match action_id:
            case 1:
                # 食事をする
                self.have_meal(person)
            case _:
                # 何もしない
                pass
        return person

    def have_meal(self, person: Human) -> Human:
        HUNGER_INCREMENT: int = 30
        person.hunger += HUNGER_INCREMENT
        person.action_log = "朝ごはんを食べた。"
        return person

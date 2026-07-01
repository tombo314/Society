from random import randint

from people.human import Human

class Action:
    def __init__(self) -> None:
        # action_id: action
        self.actions: list[str] = [
            "朝ご飯を食べた。"
        ]

    def act_randomly(self, person: Human) -> Human:
        random_action_id = randint(0, len(self.actions) - 1)
        person = self._act(person, random_action_id)
        person.action_log = self.actions[random_action_id]
        return person

    def _act(self, person: Human, action_id: int) -> Human:
        if action_id == 0:
            person.hunger += 30
        return person

from time import sleep
import json

from people.resident import Resident
from action import Action
# from human import Human
# from shop.shop import Shop
# from save_human import save_human

# デバッグモード
DEBUG_MODE = True

DAILY_LOOP_SLEEP_DURATION: int = 4
DAILY_LOOP_SLEEP_DURATION_DEBUG: int = 1
day_count: int = 1

def update_day(day_count: int) -> int:
    """
    日付が変わる
    param: その日の日付
    return: 翌日の日付
    """
    print()
    if DEBUG_MODE:
        sleep(DAILY_LOOP_SLEEP_DURATION_DEBUG)
    else:
        sleep(DAILY_LOOP_SLEEP_DURATION)
    day_count += 1
    return day_count

if DEBUG_MODE:
    # 住民をリセットする
    with open("database/residents.json", "w") as f:
        residents: dict[str, dict[str, str | int]] = {
            "residents": {}
        }
        json.dump(residents, f, indent=4)

action = Action()
resident = Resident()

# デイリーループ
while True:
    # 日数表示
    print(f"日数:{day_count:3}日目")

    # 個人の行動
    print("------------")
    for person in resident.residents:
        # 1アクション/日
        person = action.act_randomly(person)
        print(f"{person} は {person.action_log}")
        print(f"所持金: {person.money}円")
        print(f"空腹度: {person.hunger}")
        print("------------")

    day_count = update_day(day_count)

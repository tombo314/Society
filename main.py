from time import sleep

from people.resident import Resident
from people.save_human import save_human
from action.action import Action
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

action = Action()
resident = Resident()

# デイリーループ
while True:
    print("-----------------------------------------")
    # 日数表示
    print(f"日数:{day_count:3}日目")

    # 個人の行動
    print("------------")

    for person in resident.get_residents():
        # 1人につき1アクション/日
        person = action.act_randomly(person)
        person.show_status()
        save_human(person)

    day_count = update_day(day_count)

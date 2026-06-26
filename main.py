from time import sleep

from people.resident import residents
from action import Action
# from human import Human
# from shop.shop import Shop
# from save_human import save_human

# DAILY_LOOP_SLEEP_DURATION: int = 4
DAILY_LOOP_SLEEP_DURATION: int = 1 # デバッグ用に高速化
day_count: int = 1

def update_day(day_count: int) -> int:
    print()
    sleep(DAILY_LOOP_SLEEP_DURATION)
    day_count += 1
    return day_count

action = Action()

# デイリーループ
while True:
    # 日数表示
    print(f"日数:{day_count:3}日目")

    # 個人の行動
    for person in residents:
        # 1アクション/日
        daily_action: str = action.get_random_action()
        print(f"{person} は {daily_action}")

    day_count = update_day(day_count)

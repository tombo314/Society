from random import choice
from time import sleep

from residents import residents
from human import Human
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

# デイリーループ
while True:
    # 日数表示
    print(f"日数:{day_count:3}日目")

    person: Human = choice(residents)
    action: str = "朝ご飯を食べた。"

    print(f"{person} は {action}")

    day_count = update_day(day_count)

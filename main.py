from people.resident import Resident
from people.save_human import save_human
from action.action import Action
from metadata import MetaData
import const

# デバッグモード
# True: 1秒/日
# False: 4秒/日
DEBUG_MODE = True

# メタデータを管理する
metadata = MetaData(DEBUG_MODE, const.INIT_DAYS_PASSED)

# 行動を管理する
action = Action()

# 住民を管理する
resident = Resident()

# デイリーループ
while True:
    print("-----------------------------------------")
    # 日数表示
    print(f"日数:{metadata.days_passed:3}日目")

    # 個人の行動
    print("------------")

    for person in resident.get_residents():
        # 1人につき1アクション/日
        person = action.act_randomly(person)
        person.show_status()
        save_human(person)

    metadata.update_day()

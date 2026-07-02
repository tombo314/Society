from people.human import Human

import json

def save_human(person: Human):
    SAVE_PATH = "database/residents.json"

    # 既存データを読み込む（ない場合は初期化）
    try:
        with open(SAVE_PATH, "r", encoding="utf-8") as f:
            save_data: dict[str, dict[str, dict[str, str | int]]] = json.load(f)
    except:
        save_data = {"residents": {}}

    # 住民を追加・更新
    save_data["residents"][person.name] = {
        "name": person.name,
        "gender": person.gender,
        "money": person.money,
        "satiety": person.satiety,
    }

    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(save_data, f, indent=4, ensure_ascii=False)

from people.human import Human
from file_operation import FileOperation
import const

def save_human(person: Human):
    fo = FileOperation(const.FILE_PATH_RESIDENTS)
    # 既存データを読み込む（ない場合は初期化）
    try:
        save_data: dict[str, dict[str, dict[str, str | int]]] = fo.read()
    except:
        save_data = {"residents": {}}

    # 住民を追加・更新
    save_data["residents"][person.name] = person.to_dict()

    fo = FileOperation(const.FILE_PATH_RESIDENTS)
    fo.write(save_data)

from time import sleep
from file_operation import FileOperation
import const

class MetaData:
    def __init__(self, debug_mode: bool, days_passed: int) -> None:
        self.debug_mode: bool = debug_mode
        self.days_passed: int = days_passed
        self._load_days_passed()

    def _load_days_passed(self):
        try:
            fo = FileOperation(const.FILE_PATH_METADATA)
            metadata = fo.read()["metadata"]
        except:
            fo = FileOperation(const.FILE_PATH_METADATA)
            fo.write({"metadata": {"days_passed": const.INIT_DAYS_PASSED}})
            metadata = fo.read()["metadata"]
        self.days_passed = metadata["days_passed"]

    def update_day(self) -> None:
        """ 次の日になる """
        print()

        # 先に日数を増やして保存する（住民と足並みを揃える）
        self.days_passed += 1

        fo = FileOperation(const.FILE_PATH_METADATA)
        fo.write({"metadata": {"days_passed": self.days_passed}})

        # 住民・metadata の保存が済んでから次の日まで待つ
        # （待機中に中断されても両者の日数がズレない）
        if self.debug_mode:
            sleep(const.DAILY_LOOP_SLEEP_DURATION_DEBUG)
        else:
            sleep(const.DAILY_LOOP_SLEEP_DURATION)

    def to_dict(self) -> dict[str, bool | int]:
        """
        DB保存用のdictに変換する
        新しいメンバを永続化したいときは、ここと from_dict と __init__ に足すだけでよい
        """
        return {
            "debug_mode": self.debug_mode,
            "days_passed": self.days_passed
        }

    @classmethod
    def from_dict(cls, data: dict[str, bool | int]) -> "MetaData":
        """
        DBのdict（residents.jsonの1人分）からHumanを生成する
        古いDBに存在しないメンバは get() のデフォルト値で補う
        """
        return cls(
            debug_mode=bool(data.get("debug_mode", const.DEFAULT_DEBUG_MODE)),
            days_passed=int(data.get("days_passed", const.INIT_DAYS_PASSED))
        )

from human import Human

class Shop:
    def __init__(self) -> None:
        self.item_price: dict[str, int] = {
        }

    def buy(self, user: Human, item_name: str, item_num: int) -> None:
        """
        user が item_name を item_num 個購入する
        """
        price = self.item_price[item_name] * item_num
        if user.money >= price:
            user.money -= price
            print(f"{item_name} の購入に成功しました。")
        else:
            print(f"金額が足りません。{item_name} の購入に失敗しました。")
        print(f"残金 {user.money} 円")

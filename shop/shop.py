from human import Human

class Shop:
    def __init__(self) -> None:
        self.item_count: dict[str, int] = {
        }
        self.item_price: dict[str, int] = {
        }

    def buy(self, user: Human, item_name: str) -> int:
        price = self.item_price[item_name]
        if user.money >= price:
            user.money -= price
            print(f"{item_name} の購入に成功しました。")
        else:
            print(f"金額が足りません。{item_name} の購入に失敗しました。")
        print(f"残金 {user.money} 円")
        return 1

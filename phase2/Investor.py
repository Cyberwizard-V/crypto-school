
class Investor:
    def __init__(self, coin) -> None:
        self.money = 1000000
        self.currency = {"coin": coin, "amount": 0} 

    def buyStock(self, stockRate: float) -> None:
        """ Buy stock rate with all the money """
        self.currency["amount"] = int(self.money / stockRate)
        self.money =- self.money
        return

    def sellStock(self, stockRate: float) -> None:
        """ Sell stock rate with all coins """
        self.money += int(self.currency["amount"] * stockRate)
        self.currency["amount"] = 0
        return
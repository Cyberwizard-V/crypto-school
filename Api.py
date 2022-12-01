import requests
import pprint

class Api:
    def __init__(self, API_KEY = "Dxi1TAblGX6Z6v59"):
        self.API_KEY = API_KEY

    def getCoins(self):
        response = requests.get("https://api.basecampcrypto.nl/v1/coin?key=" + self.API_KEY)
        response = response.json()
        pp = pprint.PrettyPrinter(indent=4)
        return response

    def getAllCoinData(self):
        listCoin = self.getCoins()
        data = []
        Currencies = ["ALB", "BHA", "CAS", "DUB", "ELG", "FAW"]
        for x in listCoin:
            if x['symbol'] in Currencies:
                response = requests.get(f"https://api.basecampcrypto.nl/v1/coin/{x['symbol']}/history?key=" + self.API_KEY)
                data.append(response.json())
        return data

    def getSingleCoin(self, coinName) -> int:
        data = []
        response = response = requests.get(f"https://api.basecampcrypto.nl/v1/coin/{coinName}/history?key=" + self.API_KEY)
        data.append(response.json())
        return data
    
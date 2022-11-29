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
        for x in listCoin:
            response = requests.get(f"https://api.basecampcrypto.nl/v1/coin/{x['symbol']}/history?key=" + self.API_KEY)
            data.append(response.json())
        return data
    
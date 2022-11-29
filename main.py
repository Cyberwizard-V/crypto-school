import requests
import pprint

class cryptoApi:
    def __init__(self, API_KEY = "Dxi1TAblGX6Z6v59"):
        self.API_KEY = API_KEY

    def getCoins(self):
        response = requests.get("https://api.basecampcrypto.nl/v1/coin?key=" + self.API_KEY)
        response = response.json()
        pp = pprint.PrettyPrinter(indent=4)
        return response

    def getAllCoinData(self):
        listCoin = self.getCoins()
        for x in listCoin:
            print(x['symbol'])
            response = requests.get(f"https://api.basecampcrypto.nl/v1/coin/{x['symbol']}/history?key=" + self.API_KEY)
            response = response.json()
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(response)

    


#https://api.basecampcrypto.nl/v1/coin/XUA/history?key=Dxi1TAblGX6Z6v59
myObj = cryptoApi()
#myObj.getCoins()
myObj.getAllCoinData()
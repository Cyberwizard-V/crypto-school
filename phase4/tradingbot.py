import os, sys, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import Api as c_api


cash = None
coins = None

def main():
    global cash
    global coins

    # Buy stock < 10% and Sell stock > 10%
    # If after 10 days nothing happend it will change to 5% for once

    # Get coin history
    api = c_api.Api()


    while True:
        data = api.getSingleCoin("ELG")
        coinHistory = [i["value"] for x in data for i in x['history']]
        currentRate = api.getCurrentCoinValue("ELG")

        # Up - Sell
        percentage = 0.10
        if (currentRate["value"] * (1 + percentage) ) >= coinHistory[-2]:
            api.sellCoin("ELG", coins)
        # Dip - Buy
        elif (currentRate["value"] * (1 - percentage) ) <= coinHistory[-2]:
            cash = api.getTeamInfo()["cash"]
            api.buyCoin("ELG", cash)
            coins = api.getLastOrder()["quantity"]
            
        time.sleep(20)


if __name__ == "__main__":
    main()
import os, sys
import Investor as inv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import Api as c_api

def main():
    fakeCoin = {"SWA": [100,50,120,123,231,536,123]}

    # create an object for every person
    investors = {"Alice": "ALB", "Bob": "BHA", "Carol": "CAS", "Dave": "DUB", "Eve": "ELG", "Frank": "FAW"}
    for person in investors:
        investors[person] = inv.Investor(investors[person])

    # loop trough the objects
    c = c_api.Api()


    for person in investors:
        data = c.getSingleCoin(investors[person].currency["coin"])
        coinData = [i["value"] for x in data for i in x['history']]

        if person == "Alice":
            # BUY : when stock rate < 1500 SELL : when stock rate > 1600
            for x in coinData:
                # BUY STOCK
                if x < 1500:
                    print("====================================")
                    investors[person].buyStock(x)
                    print("BUY: " , x)
                    print('MONEY', investors[person].money)
                    print('COINS' , investors[person].currency['amount'])
                # SELL STOCK
                elif x > 1600:
                    print("====================================")
                    investors[person].sellStock(x)
                    print("SELL: " , x)
                    print('MONEY' ,investors[person].money)
                    print('COINS' ,investors[person].currency['amount'])
                    print("====================================")

            print(investors["Alice"].currency)
            print(f'''Current money: {investors["Alice"].money}''')

        elif person == "Bob":
            # BUY : when stock rate < 1000 SELL : when stock rate > 1100
            pass

        elif person == "Carol":
            # BUY : when stock rate reaches valley (how do you detect a valley?) SELL : when stock rate reaches top (how do you detect a top?)
            pass

        elif person == "Dave":
            # BUY : after three days of decreasing rates SELL : after three days of increasing rates
            pass

        elif person == "Eve":
            # BUY : on day 1, 11, 21, 31, 41 , etc SELL : on day 5, 15, 25, 35, 45, etc
            pass

        elif person == "Frank":
            # BUY : at day 1 and repeat: SELL : after an increase of 20% BUY again: after a decrease of 20%
            pass




# print(c.getSingleCoin("FAW"))


if __name__ == "__main__":
    main()
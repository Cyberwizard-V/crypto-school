import os, sys
import Investor as inv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import Api as c_api

def main():

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
            count = 0
            for Stockrate in range(0, len(coinData)):
                if count == 3:
                    if rate == "decreasing":
                        investors[person].buyStock(coinData[Stockrate])
                    elif rate == "increasing":
                        investors[person].sellStock(coinData[Stockrate])
                    count = 0
                if coinData[Stockrate] < coinData[Stockrate-1]:
                    count += 1
                    rate = "decreasing"
                elif coinData[Stockrate] > coinData[Stockrate-1]:
                    count += 1
                    rate = "increasing"
                else:
                    count = 0

        elif person == "Eve":
            # BUY : on day 1, 11, 21, 31, 41 , etc SELL : on day 5, 15, 25, 35, 45, etc
            buyDays = [x for x in range(1,len(coinData), 10)]
            sellDays = [x for x in range(5, len(coinData), 10)]

            for day in range(0,len(coinData)):
                if day in buyDays:
                    investors[person].buyStock(coinData[day])
                elif day in sellDays:
                    investors[person].sellStock(coinData[Stockrate])

        elif person == "Frank":
            # BUY : at day 1 and repeat: SELL : after an increase of 20% BUY again: after a decrease of 20%
            investors[person].buyStock(coinData[0])
            measureStock = coinData[0]
            for stockRate in range(1, len(coinData)):
                # Sell stocks
                if measureStock * 1.20 == coinData[stockRate]:
                    investors[person].sellStock(coinData[stockRate])
                    measureStock = coinData[stockRate]
                # Buy stocks
                elif measureStock * 0.80 == coinData[stockRate]:
                    investors[person].buyStock(coinData[stockRate])
                    measureStock = coinData[stockRate]




# print(c.getSingleCoin("FAW"))


if __name__ == "__main__":
    main()
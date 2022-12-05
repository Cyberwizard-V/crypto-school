import os, sys
import Investor as inv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import Api as c_api
import phase1.Statistics as Stats
global Trades

def main():        
    while True:
        
            print(f'''
[A] Show statistics
[B] Graphs Menu
[C] Investors 
[Z] Exit
            ''')
            getInput = input("Please choose a option: ")
            if getInput == "A":
                x = Stats.Statistics().getStatistics()
                Stats.Statistics().dataFrame(x)
                
            elif getInput == "B":
                while True:
                    print(f'''
    [A] line graph
    [B] boxplot
    [C] histogram 
    [Z] Exit
                ''')
                    graphInput = input("Please choose a option: ")

                    if graphInput == "A":    
                        Stats.Statistics().line_graph()
                    elif graphInput == "B":
                        Stats.Statistics().boxplot()
                    elif graphInput == "C":
                        Stats.Statistics().histogram()
                    else:
                        break
            elif getInput == "C":
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
                            if x < 1500 and investors[person].currency['amount'] == 0:
                                investors[person].buyStock(x)
                            # SELL STOCK
                            elif x > 1600 and investors[person].currency['amount'] > 0:
                                print(investors[person].sellStock(x))
                        print("Alice - TRADER")
                        print(investors["Alice"].currency)
                        print(f'''Current money: {investors["Alice"].money}''')
                    elif person == "Bob":
                        # BUY : when stock rate < 1000 SELL : when stock rate > 1100
                        for x in coinData:
                        # BUY STOCK
                            if x < 1000 and investors[person].currency['amount'] == 0:
                                investors[person].buyStock(x)

                            # SELL STOCK
                            elif x > 1100 and investors[person].currency['amount'] > 0:
                                print('MONEY BEFORE SELL', investors[person].money)
                                print(investors[person].sellStock(x))
                                print("SELL: " , x)
                        print("Bob - TRADER")
                        print(investors["Bob"].currency)
                        print(f'''Current money: {investors["Bob"].money}''')

                    elif person == "Carol":
                        # BUY : when stock rate reaches valley (how do you detect a valley?) SELL : when stock rate reaches top (how do you detect a top?)
                        canBuy = True
                        for stockRate in range(0,len(coinData)):
                            if coinData[stockRate - 2] > coinData[stockRate -1]  < coinData[stockRate] and canBuy is True:
                                investors[person].buyStock(coinData[stockRate])
                                canBuy = False
                            elif coinData[stockRate - 2] < coinData[stockRate - 1] > coinData[stockRate] and canBuy is False:
                                investors[person].sellStock(coinData[stockRate])
                                canBuy = True
                        print("Carol - TRADER")
                        print(investors["Carol"].currency)
                        print(f'''Current money: {investors["Carol"].money}''')

                    elif person == "Dave":
                        # BUY : after three days of decreasing rates SELL : after three days of increasing rates
                        count = 0
                        increasing, decreasing = 0, 0
                        for Stockrate in range(0, len(coinData)):
                            if increasing == 3:
                                investors[person].sellStock(coinData[Stockrate])
                                increasing, decreasing = 0, 0
                            elif increasing == 3:
                                investors[person].buyStock(coinData[Stockrate])
                                increasing, decreasing = 0, 0

                            if coinData[Stockrate] < coinData[Stockrate-1]:
                                decreasing += 1
                                increasing = 0
                            elif coinData[Stockrate] > coinData[Stockrate-1]:
                                increasing += 1
                                decreasing = 0
                            else:
                                increasing, decreasing = 0, 0
                                
                        print("Dave - TRADER")
                        print(investors["Dave"].currency)
                        print(f'''Current money: {investors["Dave"].money}''')

                    elif person == "Eve":
                        # BUY : on day 1, 11, 21, 31, 41 , etc SELL : on day 5, 15, 25, 35, 45, etc
                        buyDays = [x for x in range(1,len(coinData), 10)]
                        sellDays = [x for x in range(5, len(coinData), 10)]

                        for day in range(0,len(coinData)):
                            if day in buyDays:
                                investors[person].buyStock(coinData[day])
                            elif day in sellDays:
                                investors[person].sellStock(coinData[Stockrate])
                                
                        print("Eve - TRADER")
                        print(investors["Eve"].currency)
                        print(f'''Current money: {investors["Eve"].money}''')

                    elif person == "Frank":
                        # BUY : at day 1 and repeat: SELL : after an increase of 20% BUY again: after a decrease of 20%
                        investors[person].buyStock(coinData[0])
                        measureStock = coinData[0]
                        for stockRate in range(1, len(coinData)):
                            # Sell stocks
                            if measureStock * 1.20 >= coinData[stockRate]:
                                investors[person].sellStock(coinData[stockRate])
                                measureStock = coinData[stockRate]
                            # Buy stocks
                            elif measureStock * 0.80 <= coinData[stockRate]:
                                investors[person].buyStock(coinData[stockRate])
                                measureStock = coinData[stockRate]
                                
                        print("Frank - TRADER")
                        print(investors["Frank"].currency)
                        print(f'''Current money: {investors["Frank"].money}''')
                        

if __name__ == "__main__":
    main()
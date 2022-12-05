import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import Api as c_api



def

def main():
    pass

    # Buy stock < 10% and Sell stock > 10%
    # If after 10 days nothing happend it will change to 5% for once

    # Get coin history
    api = c_api.Api()
    data = api.getSingleCoin("ALB")
    coinData = [i["value"] for x in data for i in x['history']]

    # Up - Sell
    percentage = 0.10
    if (coinData[-1] * (1 + percentage) ) >= coinData[-2]:
        pass
    # Dip - Buy
    elif (coinData[-1] * (1 - percentage) ) <= coinData[-2]:
        pass




if __name__ == "__main__":
    main()
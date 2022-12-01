import Investor as inv

def main():
    fakeCoin = {"SWA": [100,50,120,123,231,536,123]}

    # create an object for every person
    investors = {"Alice": "ALB", "Bob": "BHA", "Carol": "CAS", "Dave": "DUB", "Eve": "ELG", "Frank": "FAW"}
    for person in investors:
        investors[person] = inv.Investor(investors[person])

    # loop trough the objects
    for person in investors:

        if person == "Alice":
            # BUY : when stock rate < 1500 SELL : when stock rate > 1600
            pass

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

    
    

if __name__ == "__main__":
    main()
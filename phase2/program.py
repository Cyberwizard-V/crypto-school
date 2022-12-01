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

    investors["Alice"].buyStock(100)
    print(investors["Alice"].currency["amount"])

    investors["Alice"].sellStock(150)
    print(investors["Alice"].money)

c = c_api.Api()
print(c.getSingleCoin("FAW"))


if __name__ == "__main__":
    main()
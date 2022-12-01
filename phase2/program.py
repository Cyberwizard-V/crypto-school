import Investor as inv

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
    
    

if __name__ == "__main__":
    main()
import pandas as pd
import numpy as np
import main as mn 


# initialize data of lists.

myObj = mn.cryptoApi()
currenyData = myObj.getAllCoinData()

data = {
    'AVG': [],
}

for x in range(0, len(currenyData)):


    AllValues = [val["value"] for val in currenyData[x]["history"]]

    # calcute average
    data["AVG"].append(np.average(AllValues))




# Creates pandas DataFrame.
df = pd.DataFrame(data, index=[x["symbol"] for x in myObj.getCoins()])
# print the data
print(df) 
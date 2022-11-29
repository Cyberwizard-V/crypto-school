import pandas as pd
import numpy as np
import Api as c_api

class Statistics:
    """
    This class calculates data / statistics and visualize the data
    """

    def __init__(self) -> None:
        self.api = c_api.Api()
        self.allCoinData = self.getAllCoinData()
        self.statisticData = {"AVG": [], "MIN": [], "MAX": [], "SD": [], "Q1": [], "Q2": [], "Q3": [], "RNG": [], "IQR": [], "UPS": [], "DOWN": [], "LUP": [], "LDWN": [],}

        # create statistics
        self.getStatistics()

        # load dataframe
        self.dataFrame()

    def getAllCoinData(self):
        return self.api.getAllCoinData()

    def getStatistics(self):
        for x in range(0, len(self.allCoinData)):
            coinData = [val["value"] for val in self.allCoinData[x]["history"]]

            # append coindata
            self.statisticData["AVG"].append(self.calculateAverage(coinData))

    def calculateAverage(self, coinData: list):
        return np.average(coinData)

    def dataFrame(self):
        df = pd.DataFrame(self.statisticData, index=[x["symbol"] for x in self.api.getCoins()])
        # print the data
        print(df) 





    pass
test = Statistics()
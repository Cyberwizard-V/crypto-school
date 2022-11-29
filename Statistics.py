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
        self.statisticData = {"AVG": [], "MIN": [], "MAX": [], "SD": [], "Q1": [], "Q2": [], "Q3": [],"IQR": [],"RNG - low" : [], "RNG - high" : [], "UPS": [], "DOWNS": [], "LUPS": [],"LDWN": [],}

        # create statistics
        self.getStatistics()

        # load dataframe
        self.dataFrame()

    def getAllCoinData(self):
        return self.api.getAllCoinData()

    def getStatistics(self):
        for x in range(0, len(self.allCoinData)):
            coinData = [val["value"] for val in self.allCoinData[x]["history"]]
            coinSD = np.array([coinData])

            # First quartile (Q1)
            Q1 = np.percentile(coinData, 25)
            # Second quartile (Q2)
            Q2 = np.percentile(coinData, 50)
            # Third quartile (Q3)
            Q3 = np.percentile(coinData, 75)
            # Interquaritle range (IQR)
            IQR = Q3 - Q1
            # append coindata
            self.statisticData["AVG"].append(self.calculateAverage(coinData))
            self.statisticData["MIN"].append(self.calculateAverage(min(coinData)))
            self.statisticData["MAX"].append(self.calculateAverage(max(coinData)))
            self.statisticData["SD"].append(self.calculateAverage(np.std(coinSD)))
            self.statisticData["Q1"].append(self.calculateAverage(Q1))
            self.statisticData["Q2"].append(self.calculateAverage(Q2))
            self.statisticData["Q3"].append(self.calculateAverage(Q3))
            self.statisticData["IQR"].append(self.calculateAverage(IQR))
            self.statisticData["RNG - low"].append(self.calculateAverage(min(coinData)))
            self.statisticData["RNG - high"].append(self.calculateAverage(max(coinData)))
            self.statisticData["UPS"].append(self.calculateUps(coinData))
            self.statisticData["DOWNS"].append(self.calculateDowns(coinData))
            self.statisticData["LUPS"].append(self.calculateLongestUp(coinData))
            self.statisticData["LDWN"].append(self.calculateLongestDown(coinData))



    def calculateAverage(self, coinData: list):
        return np.average(coinData)

    def calculateUps(self, coinData: list):
        return len([coinData[x] for x in range(0, len(coinData)) if coinData[x] > coinData[x-1]])

    def calculateDowns(self, coinData: list):
        return len([coinData[x] for x in range(0, len(coinData)) if coinData[x] < coinData[-1]])

    def calculateLongestUp(self, coinData: list):

        longestUp = 0
        currentSequence = 0

        for x in range(0, len(coinData)):
            if coinData[x] > coinData[x-1]:
                currentSequence += 1
            else:
                if currentSequence > longestUp:
                    longestUp = currentSequence
                currentSequence = 0
        return longestUp

    def calculateLongestDown(self, coinData: list):

        longestDown = 0
        currentSequence = 0

        for x in range(0, len(coinData)):
            if coinData[x] < coinData[x-1]:
                currentSequence += 1
            else:
                if currentSequence > longestDown:
                    longestDown = currentSequence
                currentSequence = 0
        return longestDown

    def dataFrame(self):
        df = pd.DataFrame(self.statisticData, index=[x["symbol"] for x in self.api.getCoins()])
        # print the data
        print(df) 





    pass
test = Statistics()
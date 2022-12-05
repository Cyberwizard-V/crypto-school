import pandas as pd
import numpy as np
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import Api as c_api
import matplotlib.pyplot as plt

class Statistics:
    """
    This class calculates data / statistics and visualize the data
    """

    def __init__(self) -> None:
        self.api = c_api.Api()
        self.allCoinData = self.getAllCoinData()
        self.statisticData = {"AVG": [], "MIN": [], "MAX": [], "SD": [], "Q1": [], "Q2": [], "Q3": [],"IQR": [],"RNG" : [], "UPS": [], "DOWNS": [], "LUPS": [],"LDWN": [],}

        # create statistics
        # self.getStatistics()

        # load dataframe
        # self.dataFrame()

    def getAllCoinData(self):
        return self.api.getAllCoinData()

    def getStatistics(self):
        X = {"AVG": [], "MIN": [], "MAX": [], "SD": [], "Q1": [], "Q2": [], "Q3": [],"IQR": [],"RNG" : [], "UPS": [], "DOWNS": [], "LUPS": [],"LDWN": [],}
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
            X["AVG"].append(self.calculateAverage(coinData))
            X["MIN"].append(min(coinData))
            X["MAX"].append(max(coinData))
            X["SD"].append(np.std(coinSD))
            X["Q1"].append(Q1)
            X["Q2"].append(Q2)
            X["Q3"].append(Q3)
            X["IQR"].append(IQR)
            X["RNG"].append(max(coinData) - min(coinData))
            X["UPS"].append(self.calculateUps(coinData))
            X["DOWNS"].append(self.calculateDowns(coinData))
            X["LUPS"].append(self.calculateLongestUp(coinData))
            X["LDWN"].append(self.calculateLongestDown(coinData))
            
            
        return X


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

    def dataFrame(self, data):
        Currencies = ["ALB", "BHA", "CAS", "DUB", "ELG", "FAW"]
        df = pd.DataFrame(data, index=[x["symbol"] for x in self.api.getCoins() if x["symbol"] in Currencies])
        # print the data frame
        print(df)
        
    def line_graph(self):
        count = 1
        for x in self.getAllCoinData():
            days = [z['day'] for z in x['history']]
            value = [z['value'] for z in x['history']]
            plt.subplot(2, 3, count)
            plt.plot(days, value)
            plt.xlabel('Days')
            plt.ylabel('Values')
            plt.title(x["symbol"])
            count += 1
        plt.show()
    
    def boxplot(self):
        count = 1
        for x in self.getAllCoinData():
            value = [z['value'] for z in x['history']]
            plt.subplot(2, 3, count)
            plt.boxplot(value)
            plt.title(x["symbol"])
            count += 1
        plt.show()

    def histogram(self):
        count = 1
        for x in self.getAllCoinData():
            value = [z['value'] for z in x['history']]
            plt.subplot(2, 3, count)
            plt.hist(value, bins= 25, edgecolor="black")
            plt.xlabel('Price')
            plt.ylabel('Count')
            plt.title(x["symbol"])
            count += 1
        plt.show()
        
# #stats = Statistics().line_graph()
# stats = Statistics().boxplot()
# #stats = Statistics().histogram()
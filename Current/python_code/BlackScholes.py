import numpy as np

class BlackScholes:
    def __init__(self, interest_, volatility_):
        self.interest = interest_
        self.volatility = volatility_


class Stock(BlackScholes):
    def __init__(self, interest_, volatility_, initialPrice_):
        self.interest = interest_
        self.volatility = volatility_
        self.initialPrice = initialPrice_
    
    def generateSamplePath(self, expiry, steps):
        """Generates a sample path"""
        stockPrice = self.initialPrice
        samplePath = np.zeros(steps)
        timeIncrement = expiry/steps
        samplePath[0] = stockPrice
        for i in range(1, steps):
            noise = np.random.normal(0, 1)
            samplePath[i] = stockPrice*np.exp((self.interest - 0.5*self.volatility**2)*timeIncrement + self.volatility*np.sqrt(timeIncrement)*noise)
            stockPrice = samplePath[i]
        self.stockProcess = samplePath
    
    def getSamplePath(self):
        return self.stockProcess
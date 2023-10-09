import numpy as np
from BlackScholes import BlackScholes 

class Derivative:
    def __init__(self, expiry_, steps_):
        self.expiry = expiry_
        self.steps = steps_ 
    
    def payoff(self, samplePath):
        return 0
    
    def generateVirtualSamplePath(self, Model: BlackScholes, initialPrice):
        stockPrice = initialPrice
        samplePath = np.zeros(self.steps)
        timeIncrement = self.expiry/self.steps
        samplePath[0] = stockPrice
        for i in range(1, self.steps):
            noise = np.random.normal(0, 1)
            samplePath[i] = stockPrice*np.exp((Model.interest - 0.5*Model.volatility**2)*timeIncrement + Model.volatility*np.sqrt(timeIncrement)*noise)
            stockPrice = samplePath[i]
        self.virtualSamplePath = samplePath
    
    def getVirtualSamplePath(self):
        return self.virtualSamplePath
    
    def generateStockProcess(self, Model: BlackScholes, initialPrice):
        stockPrice = initialPrice
        samplePath = np.zeros(self.steps)
        timeIncrement = self.expiry/self.steps
        samplePath[0] = stockPrice
        for i in range(1, self.steps):
            noise = np.random.normal(0, 1)
            samplePath[i] = stockPrice*np.exp((Model.interest - 0.5*Model.volatility**2)*timeIncrement + Model.volatility*np.sqrt(timeIncrement)*noise)
            stockPrice = samplePath[i]
        self.stockProcess = samplePath            
    
    def monteCarloPricer(self, Model: BlackScholes, initialPrice, iterations=int(1e+6)):
        value = 0
        for i in range(iterations):
            self.generateVirtualSamplePath(Model, initialPrice)
            path = self.getVirtualSamplePath()
            value = (i*value + self.payoff(path))/(i+1)
        return np.exp(-Model.interest*self.expiry)*value

    def valueProcess(self, Model: BlackScholes, initialPrice):
        self.generateStockProcess()
        return
                   
class CallOption(Derivative):
    def __init__(self, expiry_, steps_, strike_):
        self.expiry = expiry_
        self.steps = steps_
        self.strike = strike_
    
    def payoff(self, samplePath):
        if (samplePath[-1] - self.strike)>0:
            return samplePath[-1] - self.strike
        else:
            return 0
    

    
    
    
    
    
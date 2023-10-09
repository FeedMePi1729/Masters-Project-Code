import numpy as np
from BlackScholes import BlackScholes, Stock

class Derivative:
    def __init__(self, expiry_, steps_):
        self.expiry = expiry_
        self.steps = steps_ 
    
    def payoff(self, samplePath):
        return 0
           
    def monteCarloPricer(self, stock: Stock, steps=None, expiry=None, iterations=int(1e+6)):
        value = 0
        steps = self.steps if steps is None else steps
        expiry = self.expiry if expiry is None else expiry
        for i in range(iterations):
            stock.generateSamplePath(self.expiry, self.steps)
            path = stock.getSamplePath()
            value = (i*value + self.payoff(path))/(i+1)
        return np.exp(-stock.interest*self.expiry)*value
    
    def valueProcess(self, stock: Stock):
        valuePath = np.zeros(self.steps)
        # valuePath[0] = self.monteCarloPricer(stock)
        stepSize = self.expiry/self.steps
        for i in range(self.steps):
            valuePath[i] = self.monteCarloPricer(stock, steps=self.steps-i, expiry=self.expiry-i*stepSize)
        return valuePath
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
    

    
    
    
    
    
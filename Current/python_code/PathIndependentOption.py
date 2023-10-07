import numpy as np
from BlackScholes import BlackScholes 

class Derivative:
    def __init__(self, expiry_, steps_):
        self.expiry = expiry_
        self.steps = steps_ 
    
    def payoff(self, samplePath):
        """
        This is a function that will be overriden when we use this base class for inheritance
        """
        return 0
    
    def monteCarloPricer(self, Model: BlackScholes, iterations=int(1e+6)):
        value = 0
        for i in range(iterations):
            Model.generateSamplePath(self.expiry, self.steps)
            path = Model.getSamplePath()
            value = (i*value + self.payoff(path))/(i+1)
        return np.exp(-Model.interest*self.expiry)*value
    
    def arbitrageFreePrice(self, Model: BlackScholes, simulations, iterations):
        aggregateSum = 0
        value = 0
        for i in range(simulations):
            value = self.monteCarloPricer(Model, iterations)
            aggregateSum += value
        value /= simulations
        return value
                   
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
    

    
    
    
    
    
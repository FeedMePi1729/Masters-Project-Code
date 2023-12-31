import numpy as np
import matplotlib.pyplot as plt

STEP_SIZE_SPACE = 0.005
STEP_SIZE_TIME = np.sqrt(4*STEP_SIZE_SPACE)
SPACE_UPPER_BOUND = 20
SPACE_LOWER_BOUND = 0
TIME_UPPER_BOUND = 2
INTEREST = 0.04
VOLATILITY_SQUARED = 2
COLUMNS = int((SPACE_UPPER_BOUND-SPACE_LOWER_BOUND)/STEP_SIZE_SPACE)
ROWS = int(TIME_UPPER_BOUND/STEP_SIZE_TIME)
SOLUTION_GRID = np.zeros((ROWS, COLUMNS))


class Grid: 
    """
    Is a class that can solve the Black-Scholes (or any generic PDE)
    """
    def __init__(self, initialCondition, strike):
        self.initialCondition = initialCondition
        self.nRows = int(TIME_UPPER_BOUND/STEP_SIZE_TIME)
        self.nCols = int((SPACE_UPPER_BOUND-SPACE_LOWER_BOUND)/STEP_SIZE_SPACE)
        self.grid = np.zeros((self.nRows, self.nCols))
        self.initialiseGrid(strike=strike)
        self.solvePDE()
    
    def initialiseGrid(self, strike, lowerBoundaryCondition=SPACE_LOWER_BOUND, upperBoundaryCondition=SPACE_UPPER_BOUND):
        for i in range(self.nRows):
            self.grid[i][0] = lowerBoundaryCondition
            self.grid[i][self.nCols-1] = upperBoundaryCondition
        
        for i in range(self.nCols):
            self.grid[0][i] = self.initialCondition(i*STEP_SIZE_SPACE, strike)
    
    def solvePDE(self):
        for timeStep in range(self.nRows-1):
            for spaceStep in range(1, self.nCols-1):
                stockPrice = STEP_SIZE_SPACE*spaceStep
                currentValue = self.grid[timeStep][spaceStep]
                firstDerivative = (self.grid[timeStep][spaceStep+1] - self.grid[timeStep][spaceStep-1])/(2*STEP_SIZE_TIME)
                secondDerivative = (self.grid[timeStep][spaceStep+1] - 2*self.grid[timeStep][spaceStep] + self.grid[timeStep][spaceStep-1])/(STEP_SIZE_TIME**2)
                generator = INTEREST*currentValue - INTEREST*stockPrice*firstDerivative - 0.5*VOLATILITY_SQUARED*(stockPrice**2)*secondDerivative
                self.grid[timeStep+1][spaceStep] = currentValue - STEP_SIZE_SPACE*generator
    
    def optionFairPrice(self, stockPrice, time):
        spaceIndex = int(stockPrice/STEP_SIZE_SPACE) if int(stockPrice/STEP_SIZE_SPACE) < COLUMNS else COLUMNS
        timeIndex = int((TIME_UPPER_BOUND-time)/STEP_SIZE_TIME) if int((TIME_UPPER_BOUND-time)/STEP_SIZE_TIME) < ROWS else ROWS
        return self.grid[timeIndex-1][spaceIndex-1]
    
    def plotSolution(self, stockPrice):
        time = np.arange(0, TIME_UPPER_BOUND-1, STEP_SIZE_TIME)
        prices = [self.optionFairPrice(stockPrice, t) for t in time]
        plt.plot(time, prices)
        plt.show()
        
def terminalCondition(spaceValue, strike):
    if (spaceValue - strike> 0):
        return spaceValue - strike
    return 0

def main():
    x = Grid(terminalCondition, 2)
    x.plotSolution(stockPrice=2)

if __name__ == "__main__":
    main()
import numpy as np
import matplotlib.pyplot as plt

STEP_SIZE_SPACE = 0.05
STEP_SIZE_TIME = np.sqrt(8*STEP_SIZE_SPACE)
SPACE_UPPER_BOUND = 50
SPACE_LOWER_BOUND = 0
TIME_UPPER_BOUND = 10
INTEREST = 0.05
VOLATILITY_SQUARED = 0.04
COLUMNS = int((SPACE_UPPER_BOUND-SPACE_LOWER_BOUND)/STEP_SIZE_SPACE)
ROWS = int(TIME_UPPER_BOUND/STEP_SIZE_TIME)
SOLUTION_GRID = np.zeros((ROWS, COLUMNS))


class Grid:
    def __init__(self, initialCondition):
        self.initialCondition = initialCondition
        self.nRows = int(TIME_UPPER_BOUND/STEP_SIZE_TIME)
        self.nCols = int((SPACE_UPPER_BOUND-SPACE_LOWER_BOUND)/STEP_SIZE_SPACE)
        self.grid = np.zeros((self.nRows, self.nCols))
    
    def initialiseGrid(self, lowerBoundaryCondition=SPACE_LOWER_BOUND, upperBoundaryCondition=SPACE_UPPER_BOUND):
        for i in range(self.nRows):
            self.grid[i][0] = lowerBoundaryCondition
            self.grid[i][self.nCols-1] = upperBoundaryCondition
        
        for i in range(self.nCols):
            self.grid[0][i] = self.initialCondition(i*STEP_SIZE_SPACE)
    
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
        spaceIndex = int(stockPrice/STEP_SIZE_SPACE)
        timeIndex = int((TIME_UPPER_BOUND-time)/STEP_SIZE_TIME)
        return self.grid[timeIndex-1][spaceIndex-1]
    
    def plotSolution(self, stockPrice):
        time = np.arange(0, TIME_UPPER_BOUND, STEP_SIZE_TIME)
        prices = [optionFairPrice(stockPrice, t) for t in time]
        plt.plot(time, prices)
        plt.show()
        
def terminalCondition(spaceValue):
    if (spaceValue - 5 > 0):
        return spaceValue - 5
    return 0

def initialiseGrid(lowerBoundaryCondition=0, upperBoundaryCondition=95):
    for i in range(ROWS):
        SOLUTION_GRID[i][0] = lowerBoundaryCondition
        SOLUTION_GRID[i][COLUMNS-1] = upperBoundaryCondition
    
    
    for i in range(COLUMNS):
        SOLUTION_GRID[0][i] = terminalCondition(i*STEP_SIZE_SPACE)


def solvePDE():
    for timeStep in range(ROWS-1):
        for spaceStep in range(1, COLUMNS-1):
            stockPrice = STEP_SIZE_SPACE*spaceStep
            currentValue = SOLUTION_GRID[timeStep][spaceStep]
            firstDerivative = (SOLUTION_GRID[timeStep][spaceStep+1] - SOLUTION_GRID[timeStep][spaceStep-1])/(2*STEP_SIZE_TIME)
            secondDerivative = (SOLUTION_GRID[timeStep][spaceStep+1] - 2*SOLUTION_GRID[timeStep][spaceStep] + SOLUTION_GRID[timeStep][spaceStep-1])/(STEP_SIZE_TIME**2)
            generator = INTEREST*currentValue - INTEREST*stockPrice*firstDerivative - 0.5*VOLATILITY_SQUARED*(stockPrice**2)*secondDerivative
            SOLUTION_GRID[timeStep+1][spaceStep] = currentValue - STEP_SIZE_SPACE*generator

def optionFairPrice(stockPrice, time):
    spaceIndex = int(stockPrice/STEP_SIZE_SPACE)
    timeIndex = int((TIME_UPPER_BOUND-time)/STEP_SIZE_TIME)
    return SOLUTION_GRID[timeIndex-1][spaceIndex-1]

def main():
    x = Grid(initialCondition=terminalCondition)
    x.initialiseGrid()
    x.solvePDE()
    stockPrice = np.arange(SPACE_LOWER_BOUND, SPACE_UPPER_BOUND, STEP_SIZE_SPACE)
    price = [optionFairPrice(stock, 1) for stock in stockPrice]
    plt.plot(stockPrice, price)
    plt.show()
if __name__ == "__main__":
    main()
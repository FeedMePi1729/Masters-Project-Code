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
    initialiseGrid()
    solvePDE()
    time = np.linspace(0, TIME_UPPER_BOUND, int((SPACE_UPPER_BOUND-10)/STEP_SIZE_SPACE))
    stockPrices = np.arange(0, SPACE_UPPER_BOUND-10, STEP_SIZE_SPACE)
    stockValue = 6
    for i in range(9):
        prices = [optionFairPrice(stock, i) for stock in stockPrices]
        plt.plot(time, prices, label=f'{i}')
    plt.axvline(x=9)
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()
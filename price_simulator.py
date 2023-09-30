import numpy as np
import matplotlib.pyplot as plt

from process_simulator import Process, Simulation
from pde_solver import * # it is considered bad practice to import *. Consider something else in the future





def main():
    grid = Grid(terminalCondition)
    grid.initialiseGrid(2)
    grid.solvePDE()
    drift = lambda t,x: 0.15*x
    diffusion = lambda t,x: np.sqrt(VOLATILITY_SQUARED)*x
    initialPosition = 1
    spaceSteps = grid.nCols
    diffusionProcess = Process(drift=drift, diffusion=diffusion, initialPosition=initialPosition)
    simulation = Simulation(diffusionProcess=diffusionProcess, endTime=TIME_UPPER_BOUND, steps=spaceSteps)
    timeSteps = np.linspace(0, TIME_UPPER_BOUND, spaceSteps)
    stockPrices = simulation.getPath()
    optionPrices = [grid.optionFairPrice(stockPrice=stock,time=t) for stock, t in zip(stockPrices, timeSteps)]
    plt.plot(timeSteps, optionPrices)
    plt.show()
    
    
if __name__ == "__main__":
    main()


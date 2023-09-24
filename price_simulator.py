import numpy as np
import matplotlib.pyplot as plt

from process_simulator import Process, Simulation
from pde_solver import * # it is considered bad practice to import *. Consider something else in the future





def main():
    grid = Grid(terminalCondition)
    drift = lambda t,x: 0.15*x
    diffusion = lambda t,x: np.sqrt(VOLATILITY_SQUARED)*x
    initialPosition = 1
    diffusionProcess = Process(drift=drift, diffusion=diffusion, initialPosition=initialPosition)
    simulation = Simulation(diffusionProcess=diffusionProcess, endTime=10, steps=1000)
    stockPrices = simulation.getPath()
    optionPrices = [grid.optionFairPrice(stockPrice=stock, )]
    
    
    
if __name__ == "__main__":
    main()


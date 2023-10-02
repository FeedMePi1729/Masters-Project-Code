import numpy as np
import matplotlib.pyplot as plt

from process_simulator import Process, Simulation
from pde_solver import * # it is considered bad practice to import *. Consider something else in the future

INITIAL_POSITION=1
drift = lambda t,x: 0.12*x
diffusion = lambda t,x: VOLATILITY_SQUARED*x

class Portfolio:
    def __init__(self, grid: Grid, strikePrice, drift, diffusion):
        self.grid=grid
        self.grid.initialiseGrid(strike=strikePrice)
        self.grid.solvePDE()
        # We have now initialised our grid and ready for solving the PDE

    def initialisePortfolio(self):
        """Need to run this before anything"""
        self.process=Process(drift=drift, diffusion=diffusion, initialPosition=INITIAL_POSITION)
        self.spaceSteps=self.grid.nCols
        self.simulation=Simulation(diffusionProcess=self.process, endTime=TIME_UPPER_BOUND, steps=self.spaceSteps)
        self.timeSteps=np.linspace(0,TIME_UPPER_BOUND, self.spaceSteps)
        self.stockPrices=self.simulation.getPath()
        self.optionPrices=[self.grid.optionFairPrice(stockPrice=stock, time=t) for stock, t in zip(self.stockPrices, self.timeSteps)]
        
    
    def plotOptionPath(self, strikePrice=0):
        plt.plot(self.timeSteps, self.optionPrices)
        plt.show()




def main():
    x = Portfolio(Grid(terminalCondition), 0, drift=drift, diffusion=diffusion)
    x.initialisePortfolio()
    x.plotOptionPath()
    
    
if __name__ == "__main__":
    main()


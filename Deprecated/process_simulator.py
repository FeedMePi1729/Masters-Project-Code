import numpy as np
import matplotlib.pyplot as plt

class Process:
    def __init__(self, drift, diffusion, initialPosition):
        self.drift = drift
        self.diffusion = diffusion
        self.initialPosition = initialPosition
    
class Simulation:
    def __init__(self, diffusionProcess, endTime, steps):
        self.drift = diffusionProcess.drift
        self.diffusion = diffusionProcess.diffusion
        self.initialPosition = diffusionProcess.initialPosition
        self.process = diffusionProcess
        self.steps = steps
        self.endTime = endTime
        self.stepSize = endTime/steps
        
    def getPath(self):
        """ Returns a realised path of a process

        Returns:
            numpy array: gives the path of a process
        """
        
        process = np.zeros(self.steps)
        process[0] = float(self.initialPosition)
        for i in range(self.steps-1):
            process[i+1] = process[i] + self.drift(i*self.stepSize, process[i])*self.stepSize + self.diffusion(i*self.stepSize, process[i])*self._brownianMotionIncrement()
        self.simulatedPath = process
        
        return self.simulatedPath
    
    def getProcess(self):
        """Returns a Diffusion Object

        Returns:
            Diffusion Object
        """
        return self.process
    
    def _brownianMotionIncrement(self):
        """Generates a brownian motion increment

        Args:
            stepSize (float/int): Is the stepsize of the process we want to simulate

        Returns:
            float: The generated Brownian Motion Increment
        """
        dw = np.random.normal(0, np.sqrt(self.stepSize))
        return dw
    
    def simulationDiffusion(self):
        """Simulates a 1 dimensional diffusion process

        Args:
            drift (func): is the drift coefficient
            diffusion (func): is the diffusion coefficient
            endTime (float): is the terminal time for the process (length of the process)
            steps (int): How many steps should we do
            initialPos (float, optional): Initial position of the process. Defaults to 0.

        Returns:
            array: returns an array of size steps containing the simulated path of the process
        """

        
    
    def plotPath(self):
        """
        Generates a plot of a singular path of the chosen diffusion process
        """
        self.simulationDiffusion()
        time = np.linspace(0, self.endTime, self.steps)
        self.getPath()
        plt.plot(time, self.simulatedPath)
        plt.show()
    
    def plotMultiplePaths(self, numOfPaths):
        """Plots multiple paths of the chosen diffusion path

        Args:
            numOfPaths (int): number of paths we want simulated
        """
        time = np.linspace(0, self.endTime, self.steps)
        for i in range(numOfPaths):
            self.simulationDiffusion()
            plt.plot(time, self.simulatedPath)
        plt.show()
        

def main():
    drift = lambda t,x: 0.2*x
    diffusion = lambda t,x: 0.1*x
    initialPosition = 1
    diffusionProcess = Process(drift=drift, diffusion=diffusion, initialPosition=initialPosition)
    simulation = Simulation(diffusionProcess=diffusionProcess, endTime=10, steps=10000)
    simulation.plotPath()

if __name__ == "__main__":
    main()
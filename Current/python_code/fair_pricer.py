import numpy as np
import matplotlib.pyplot as plt

from BlackScholes import BlackScholes
from PathIndependentOption import *

def main():
    model = BlackScholes(0.03, 1)
    derivative = CallOption(2, 1000, 20)
    print(derivative.monteCarloPricer(model, 10, 10_000))

if __name__ == "__main__":
    main()

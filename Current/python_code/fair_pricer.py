import numpy as np
import matplotlib.pyplot as plt

from BlackScholes import BlackScholes
from PathIndependentOption import *

def main():
    model = Stock(0.03, 1, 10)
    derivative = CallOption(2, 100, 20)
    print(derivative.valueProcess(model))

if __name__ == "__main__":
    main()

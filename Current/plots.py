import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


def plotAutoCorrelationAppleStock():
    applePrice = yf.Ticker('AAPL')
    data = applePrice.history(period='1mo', interval='1h')['Close']
    logPrices = np.log(data)
    logReturns = logPrices.diff(1)

    autoCor = []
    for i in range(20):
        autoCor += [logReturns.autocorr(lag=i)]

    plt.title('Auto Correlation of $AAPL taken at hourly increments over a 1 month period')
    plt.scatter(np.linspace(0,19,20), autoCor)
    plt.xlabel('Lag')
    plt.ylabel('Auto Correlation')
    plt.axhline(y=-0.05, linestyle='dashed', color='red')
    plt.axhline(y=0.05, linestyle='dashed', color='red')
    plt.grid(True)
    plt.show()

def main():
    plotAutoCorrelationAppleStock()    
    return

if __name__ == "__main__":
    main()
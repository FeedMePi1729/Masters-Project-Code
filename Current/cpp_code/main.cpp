#include <iostream>
#include "PathIndependentOption.h"


using namespace std;

int main(){
    double initial=10, interest=0.03, volatility=0.2;
    // BlackScholes Model(initial, interest, volatility);
    double expiry = 1/12;
    double strike = 10;
    int steps = 30;
    CallOption Option(expiry, strike, steps);

    long N = 30000;
    // std::cout << Option.monteCarloPricer(Model, N) << "\n";
    // Option.monteCarloPricer(Model, N);
    return 0;
}
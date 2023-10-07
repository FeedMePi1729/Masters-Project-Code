#include <cmath>
#include "BlackScholes.h"


const double pi = 4.0*atan(1.0);

double gaussian(){
    // Generates a Gaussian Random Variable with mean 0, variance 1
    double U1 = (rand()+1.0)/(RAND_MAX+1.0);
    double U2 = (rand()+1.0)/(RAND_MAX+1.0);
    return sqrt(-2.0*log(U1))*cos(2.0*pi*U2);
}

BlackScholes::BlackScholes(
        double initialPrice_,
        double interest_,
        double volatility_
        ){
        initialPrice = initialPrice_;
        interest = interest_;
        volatility = volatility_;
        srand(time(NULL));
        // sets the seed for random numbers
    }

void BlackScholes::generateSamplePath(double T, int m, SamplePath& S){
    double stockPrice = initialPrice;
    for (int k=0; k<m; k++){
        S[k] = stockPrice*exp((interest-volatility*volatility*0.5)*(T/m)+volatility*sqrt(T/m)*gaussian());
        stockPrice = S[k];
    }
}

// int main(){
//     return 0;
// }

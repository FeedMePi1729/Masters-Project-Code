#include <pathIndependentOption.h>
#include <cmath>

double PathIndependentOption::monteCarloPricer(BlackScholes Model, long iterations){
        double value;
        SamplePath S(iterations);
        for (long n=0; n<iterations; n++){
            Model.generateSamplePath(expiry, steps, S);
            value = (n*value + payoff(S))/(n+1);
        }
        return exp(-Model.interest*expiry)*value;
    }

double CallOption::payoff(SamplePath& S){
    if (S[steps-1] - strike > 0){
        return S[steps-1] - strike;
    }
    return 0;
}



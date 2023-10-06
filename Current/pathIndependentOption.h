#ifndef PathIndependentOption_h
#define PathIndependentOption_h

#include "blackScholes.h"

class PathIndependentOption {
    public:
        double expiry;
        int steps;
        double monteCarloPricer(BlackScholes Model, long iterations);
        virtual double payoff(SamplePath& S){
            return 0;
        };
};

class CallOption : public PathIndependentOption {
    public:
        double strike;
        CallOption(double expiry_, double strike_, int steps_){
            expiry = expiry_;
            strike = strike_;
            steps = steps_;
        };
        double payoff(SamplePath& S);
};

#endif
#include <iostream>
#include <vector>
#include <cmath>

typedef std::vector<double> SamplePath;

const double pi = 4.0*atan(1.0);

class BlackScholes {
    public:
        double initialPrice, interest, volatility;
        BlackScholes(
            double initialPrice_,
            double interest_,
            double volatility_
            );
        void generateSamplePath(
            double T,
            int m,
            SamplePath& S
            );
             // to generate the sample path with m being steps required
};

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

class PathIndependentOption {
    public:
        double expiry;
        int steps;
        double monteCarloPricer(BlackScholes Model, long iterations);
        virtual double payoff(SamplePath& S)=0;
};

class CallOption : public PathIndependentOption {
    public:
        double strike;
        CallOption(double expiry_, double strike_, int steps_);
        double payoff(SamplePath& S);
};

CallOption::CallOption(double expiry_, double strike_, int steps_){
        expiry = expiry_;
        strike = strike_;
        steps = steps_;
}

double CallOption::payoff(SamplePath& S){
    if (S[steps-1] - strike > 0){
        return S[steps-1] - strike;
    }
    return 0;
}

double PathIndependentOption::monteCarloPricer(BlackScholes Model, long iterations){
        double value;
        SamplePath S(iterations);
        for (long n=0; n<iterations; n++){
            Model.generateSamplePath(expiry, steps, S);
            value = (n*value + payoff(S))/(n+1);
        }
        return exp(-Model.interest*expiry)*value;
    }

int main(){
    double initial=10, interest=0.03, volatility=1;
    BlackScholes Model(initial, interest, volatility);
    double expiry = 10;
    double strike = 20;
    int steps = 3000;
    CallOption Option(expiry, strike, steps);

    long N = 30000;
    std::cout << Option.monteCarloPricer(Model, N) << "\n";
    // Option.monteCarloPricer(Model, N);
    return 0;
}
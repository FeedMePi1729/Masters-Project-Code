#ifndef BSModel_h
#define BSModel_h

using namespace std;
#include <vector>

typedef vector<double> SamplePath;

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

#endif

#include <iostream>
#include <cmath>

double STEP_SIZE_SPACE = 0.05;
double STEP_SIZE_TIME = std::sqrt(2*STEP_SIZE_SPACE); // ensures stability of solution
double SPACE_UPPER_BOUND = 100;
double SPACE_LOWER_BOUND = 0;
double TIME_UPPER_BOUND = 10;
double INTEREST = 1;
double STRIKE = 5;
double VOLATILITY_SQUARED = 0.04; // require volatility to be small in order to ensure the stability of solution
int COLUMNS;
int ROWS;

void getGridDimensions(
    double stepSizeSpace=STEP_SIZE_SPACE,
    double stepSizeTime=STEP_SIZE_TIME,
    double spaceUpperBound=SPACE_UPPER_BOUND,
    double spaceLowerBound=SPACE_LOWER_BOUND,
    double timeUpperBound=TIME_UPPER_BOUND,
    int* columns=&COLUMNS,
    int* rows=&ROWS
    ){
        double distance = spaceUpperBound - spaceLowerBound;
        *columns = static_cast<int>(distance/stepSizeSpace);
        *rows = static_cast<int>(timeUpperBound/stepSizeTime);
    }

float initialValue(float spaceVal){
    if (spaceVal - 5 > 0){
        return spaceVal - 5;
    } 
    return 0;
}

double optionFairPrice(double stockPrice, double time){
    getGridDimensions();
    double SOLUTION_GRID[ROWS][COLUMNS];
    for (int i=1; i<COLUMNS; i++){ // initial condition
        SOLUTION_GRID[0][i] = initialValue(i*STEP_SIZE_SPACE);
    }
    for (int i=0; i<ROWS; i++){
        SOLUTION_GRID[i][0] = 0;
        SOLUTION_GRID[i][COLUMNS-1] = 95;
    }

    for (int timeStep=0; timeStep<ROWS-1; timeStep++){
        for (int spaceStep=1; spaceStep<COLUMNS-1; spaceStep++){
            double stockPrice = STEP_SIZE_SPACE*spaceStep;
            double currentValue = SOLUTION_GRID[timeStep][spaceStep];
            double firstDerivative = (SOLUTION_GRID[timeStep][spaceStep+1] - SOLUTION_GRID[timeStep][spaceStep-1])/(2*STEP_SIZE_TIME);
            double secondDerivative = (SOLUTION_GRID[timeStep][spaceStep+1] - 2*SOLUTION_GRID[timeStep][spaceStep] + SOLUTION_GRID[timeStep][spaceStep-1])/(std::pow(STEP_SIZE_TIME,2));
            double generator = INTEREST*currentValue - INTEREST*stockPrice*firstDerivative - 0.5*VOLATILITY_SQUARED*std::pow(stockPrice, 2)*secondDerivative;
            SOLUTION_GRID[timeStep+1][spaceStep] = currentValue - STEP_SIZE_SPACE*generator; // ready to solve a generic problem
        }
    }
    int spaceIndex = stockPrice/STEP_SIZE_SPACE;
    int timeIndex = (TIME_UPPER_BOUND-time)/STEP_SIZE_TIME;

    return SOLUTION_GRID[timeIndex][spaceIndex]; 
}


class Grid {
    private:
        double stepSizeSpace;
        double stepSizeTime;
        double spaceUpperBound;
        double spaceLowerBound;
        double timeUpperBound;
        int columns;
        int rows;

        void setRows(){
            rows = static_cast<int>(timeUpperBound/stepSizeTime);
        }
        void setColumns(){
            double distance = spaceUpperBound - spaceLowerBound;
            columns = static_cast<int>(distance/stepSizeSpace);
        }
    public:
        void setStepSizeSpace(double s=STEP_SIZE_SPACE){
            stepSizeSpace=s;
        }
        void setStepSizeTime(double s=STEP_SIZE_TIME){
            stepSizeTime=s;
        }
        void setSpaceUpperBound(double s=SPACE_UPPER_BOUND){
            spaceUpperBound=s;
        }
        void setSpaceLowerBound(double s=SPACE_LOWER_BOUND){
            spaceLowerBound=s;
        }
        void setTimeUpperBound(double s=TIME_UPPER_BOUND){
            timeUpperBound=s;
        }
        void setDimensions(){
            getRows();
            getColumns();
        }
        int getRows(){
            return rows;
        }
        int getColumns(){
            return columns;
        }
        double getStepSizeSpace(){
            return stepSizeSpace;
        }
        double getStepSizeTime(){
            return stepSizeTime;
        }
        double getSpaceUpperBound(){
            return spaceUpperBound;
        }
};

class Model: public Grid {
    private:
        double volatilitySquared;
        double interest;
        double (*payoffFunction) (double stock);
        double strike;
        int rows = Grid::getRows();
        int columns = Grid::getColumns();
    public:
        void setVolatilitySquared(double s=VOLATILITY_SQUARED){
            volatilitySquared=s;
        }
        double getVolatility(){
            return std::sqrt(volatilitySquared);
        }
        void setInterest(double s=INTEREST){
            interest=s;
        }
        double getInterest(){
            return interest;
        }
        void setPayoff(double (*func)(double x)){
            payoffFunction = func;
        }
        void setStrike(double s=5){
            strike = s;
        }
        double solutionGrid[rows]
        void setGrid(){
            double stepSizeSpace = Grid::getStepSizeSpace();
            double stepSizeTime = Grid::getStepSizeTime();
            double spaceUpperBound = Grid::getSpaceUpperBound();
            double solutionGrid[rows][columns];
            for (int i=0; i<columns; i++){
                solutionGrid[0][i] = payoffFunction(i*stepSizeSpace);
            }
            for (int i=0; i<rows; i++){
                solutionGrid[i][0] = 0;
                solutionGrid[i][columns-1] = spaceUpperBound - strike;
            }
        }
        void solvePDE(){
        setGrid();
        for (int timeStep=0; timeStep<ROWS-1; timeStep++){
            for (int spaceStep=1; spaceStep<COLUMNS-1; spaceStep++){
                double stockPrice = STEP_SIZE_SPACE*spaceStep;
                double currentValue = solutionGrid[timeStep][spaceStep];
                double firstDerivative = (solutionGrid[timeStep][spaceStep+1] - solutionGrid[timeStep][spaceStep-1])/(2*STEP_SIZE_TIME);
                double secondDerivative = (solutionGrid[timeStep][spaceStep+1] - 2*solutionGrid[timeStep][spaceStep] + solutionGrid[timeStep][spaceStep-1])/(std::pow(STEP_SIZE_TIME,2));
                double generator = interest*currentValue - interest*stockPrice*firstDerivative - 0.5*volatilitySquared*std::pow(stockPrice, 2)*secondDerivative;
                SOLUTION_GRID[timeStep+1][spaceStep] = currentValue - STEP_SIZE_SPACE*generator; // ready to solve a generic problem
            }
    }
        }
};

int main(){
    for (int t=0; t<TIME_UPPER_BOUND; t++){
        std::cout << optionFairPrice(5, t) << '\n';
    }
    return 0;
}
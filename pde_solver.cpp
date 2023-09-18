#include <iostream>
#include <cmath>


double SPACE_STEP_SIZE = 0.005;
double TIME_STEP_SIZE = std::sqrt(2*SPACE_STEP_SIZE); // Ensuring stability of results
double END_TIME = 1;
double STOCK_UPPER_BOUND = 4;
double INTEREST = 0.01;
double VOLATILITY = 1;
int ROWS;
int COLUMNS;


 // TODO: find a way to make the initial condition of the grid be what we want it to be
int timeSteps(double endTime, double timeIncrement){
    return static_cast<int>(endTime/timeIncrement);
}

int stockSteps(double stockUpperBound, double spaceIncrement){
    return static_cast<int>(stockUpperBound/spaceIncrement);
}

void gridDimensions(
    double endTime,
    double stockUpperBound,
    double timeIncrement,
    double spaceIncrement,
    int& rows,
    int& columns){
        int nRows = endTime/timeIncrement;
        int nCols = stockUpperBound/spaceIncrement + 2*nRows; // to deal with the unbounded case
        rows = nRows;
        columns = nCols;
}

double payoff(double stock, double strike=0){
    if (stock - strike > 0){
        return stock - strike;
    }
    return 0;
}

int main(){
    gridDimensions(END_TIME, STOCK_UPPER_BOUND, TIME_STEP_SIZE, SPACE_STEP_SIZE, ROWS, COLUMNS);
    double SOLUTION_GRID[ROWS][COLUMNS]; // Sets the grid for our PDE to solve

    for (int i=0; i<COLUMNS; i++){ // initialising grid
        SOLUTION_GRID[0][i] = payoff(-ROWS*SPACE_STEP_SIZE + i*SPACE_STEP_SIZE);
    };

    for (int timeStep=0; timeStep<ROWS-1; timeStep++){
        for (int spaceStep=timeStep; spaceStep<COLUMNS-timeStep; spaceStep++){
            double currentValue = SOLUTION_GRID[timeStep][spaceStep];
            double firstDerivative = (SOLUTION_GRID[timeStep][spaceStep+1] - SOLUTION_GRID[timeStep][spaceStep-1])/(2*TIME_STEP_SIZE);
            double secondDerivative = (SOLUTION_GRID[timeStep][spaceStep+1] - 2*SOLUTION_GRID[timeStep][spaceStep]- SOLUTION_GRID[timeStep][spaceStep-1])/(TIME_STEP_SIZE*TIME_STEP_SIZE);
            double stock = -ROWS*SPACE_STEP_SIZE + spaceStep*SPACE_STEP_SIZE;
            SOLUTION_GRID[timeStep+1][spaceStep] = currentValue - SPACE_STEP_SIZE*(INTEREST*currentValue - INTEREST*stock*firstDerivative - 0.5*std::pow(VOLATILITY, 2)*std::pow(stock, 2)*secondDerivative); 
        };
    }; // This is the scheme to solving the PDE

    for (int i=0; i < COLUMNS; i++){
        std::cout << SOLUTION_GRID[ROWS-1][i] << '\n';
    };



    return 0;
}

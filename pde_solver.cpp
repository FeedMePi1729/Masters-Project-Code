#include <iostream>
#include <cmath>

double STEP_SIZE_SPACE = 0.05;
double STEP_SIZE_TIME = std::sqrt(2*STEP_SIZE_SPACE); // ensures stability of solution
double SPACE_UPPER_BOUND = 10;
double SPACE_LOWER_BOUND = 0;
double TIME_UPPER_BOUND = 10;
double INTEREST = 0.01;
double VOLATILITY_SQUARED = 1;
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



int main(){
    getGridDimensions();
    double SOLUTION_GRID[ROWS][COLUMNS];
    for (int i=1; i<COLUMNS; i++){ // initial condition
        SOLUTION_GRID[0][i] = initialValue(i*STEP_SIZE_SPACE);
    }
    for (int i=0; i<ROWS; i++){
        SOLUTION_GRID[i][0] = 0;
        SOLUTION_GRID[i][COLUMNS-1] = 100;
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
    for (int i=0; i<ROWS; i++){
        std::cout << SOLUTION_GRID[i][100] << '\n';
    }
    return 0;
}
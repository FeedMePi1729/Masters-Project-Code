#include <iostream>


void incrementSetter(double& timeIncrement, double& spaceIncrement){
    // Used for setting the time and space increments
    double newTimeIncrement, newSpaceIncrement;
    std::cout << "Enter New Time Increment: "; std::cin >> newTimeIncrement;
    std::cout << "Enter New Space Increment: "; std::cin >> newSpaceIncrement;
    timeIncrement = newTimeIncrement;
    spaceIncrement = newSpaceIncrement;
}

 // TODO: find a way to make the initial condition of the grid be what we want it to be
 
int main(){
    double timeIncrement = 0;
    double spaceIncrement = 0;
    double endTime = 1;
    double stockUpperBound = 4;
    incrementSetter(timeIncrement, spaceIncrement);
    int timeSteps = endTime/timeIncrement;
    int stockSteps = stockUpperBound/spaceIncrement;
    double SOLUTION_GRID[timeSteps][stockSteps]; // Sets the grid for our PDE to solve
    std::cout << sizeof(SOLUTION_GRID);
    return 0;
}

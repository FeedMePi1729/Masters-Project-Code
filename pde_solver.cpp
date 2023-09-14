#include <iostream>


void incrementSetter(double& timeIncrement, double& spaceIncrement){
    double newTimeIncrement, newSpaceIncrement;

    std::cout << "Enter New Time Increment: "; std::cin >> newTimeIncrement;
    std::cout << "Enter New Space Increment: "; std::cin >> newSpaceIncrement;
    timeIncrement = newTimeIncrement;
    spaceIncrement = newSpaceIncrement;
}

int main(){
    double timeIncrement = 0;
    double spaceIncrement = 0;
    incrementSetter(timeIncrement, spaceIncrement);
    std::cout << timeIncrement << '\n';
    std::cout << spaceIncrement;
    return 0;
}

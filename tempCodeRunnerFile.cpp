    std::ofstream solutionSpace;
    solutionSpace.open("solutionSpace.txt");
    for (int time=0; time<ROWS; time++){
        for (int stock=0; stock<COLUMNS; stock++){
            solutionSpace << optionFairPrice(stock*STEP_SIZE_SPACE, time*STEP_SIZE_TIME) << " ";
        }
        solutionSpace << '\n';
    }
    solutionSpace.close();
    return 0;
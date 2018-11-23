# Lekker-oke-

## Introduction
This project is created as part of the course 'Heuristieken' at the University of Amsterdam. 
Amstelhaege is a new building project just south of Amsterdam. It is a lot of 160 by 180 meters.
To maintain the nature-like surroundingss south of Amsterdam, the new neighborhood has to be composed of a lot of free space with 
just a few houses; plans of 20, 40 or 60 houses are considerd.

Three different kinds of houses (small, medium and large) are designed to be built on the lot. Each of the houses will be build in a fixed
percentage of the total amout of houses and each of these houses has their own properties regarding dimensions and price. The houses are
obliged to have a fixed minimum amount of free space; each extra meter of free space will result in a rise in the worth of the house.

To preserve the rural design of the neigborhood, 20% of the neigborhood has to consist of water present in 4 rectangular or oblong bodies.

## Background
The first step in providing a succesfull solution to this problem is to understand its real complexity and to define the problem
theoretically. It is necessar therefore to define the state space, upper and lower bounds, a visualisation of the problem, a means to
compare the result and define the best (by means of a score function) an possibly a division of the problem in subproblems or a flow.

### State space
For this problem, there is a grid of 180 * 160. This means there are 28800 places to plant the first house. For the 20-houses solution, 
this results in 28800 ^ 20 =  1,54 * 10 ^ 89 solutions. However, this allows houses to be placed on top of each other and next to or on
the boundaries of the grid. Correcting for these constraints still leaves **2.57 * 10 ^ 87** options. 
This state space doesn't take the correctness in terms of interdependent free space and water, since the calculations of these
constriants is dependent on the actual locations of earlier houses. 

### Upper and lower bounds


## Structure
The powerpoint presentations for the weekly meetings are present in the folder /powerpoints.
The code for the creation of the grid and the building is provided in the folder /grid.
The file 'Theorie van het probleem.docx' is a short writing describing the theoretical beackground of the problem.
It contains calculations of the state space, lower bound and upper bound.

### Authors
- Eveline Tiekink
- Coen Mol
- Corné Heijnen

### Acknowledgements
- Stackoverflow
- Minor Programmeren at University of Amsterdam
- Angelo Groot (Tech Assistent)

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
compare the result and define the best (by means of a score function) and possibly a division of the problem in subproblems or a flow.

### State space
For this problem, there is a grid of 180 * 160. This means there are 28800 places to plant the first house. For the 20-houses solution, 
this results in 28800<sup>20</sup>=  1.54 * 10<sup>89</sup> solutions. However, this allows houses to be placed on top of each other and next to or on
the boundaries of the grid. Correcting for these constraints still leaves **2.57 * 10<sup>87</sup>** options. 
This state space doesn't take the correctness in terms of interdependent free space and water, since the calculations of these
constriants is dependent on the actual locations of earlier houses. 

### Problem type and score function
As a base case, the objecctive of this problem is to place the required houses in a grid of 180 * 160 meters and to place a maximum
of four square or oblong bodies of water strechting out 20% of the total surface. This means there are definitely constraints associated
with this problem. However, all solutions of this problem can be ranked based on the total worth of all the houses. This mean this is 
a constraint optimisation problem. 
The score function of this problem is based on the base price of the houses and an enlargement factor based on the amount of free space
for this house. This can be summarised like this:
Type of house, base price, minimum free space, bonus enlargement for extra free space: S, 285000, 2, 3 -- M, 399000, 3, 4 -- L, 610000, 6, 6

The scores per house would be:

scoreL = 610000 * 1.06<sup>(fs - 6)</sup>

scoreM = 399000 * 1.04<sup>(fs - 4)</sup>

scoreS = 285000 * 1.03<sup>(fs - 62</sup>

The total score is the sum of the scores for all the houses. The goal is to maximize this score.

### Upper and lower bounds
The above mentioned score function can take on a wide range of values. To understand the problem better, and know the relative quality
of an individual solution. The lower bound is a situation in which the houses are placed to each other as close as possible, leaving 
the extra free space of all the houses at 0.

A general formula for this would be:
Score = priceLarge * nLarge + priceMedium * nMedium+ priceSmall * nSmall

In the case of a 20-house setup, this will result in a score of **€7.215.000**.
In the case of a 40-house setup, this will result in a score of **€14.430.000**. 
In the case of a 60-house setup, this will result in a score of **€21.615.000**. 

The first calculated upper bound would be a situation in which all the houses have the maximum free space, as is achieved by placing
all the houses in the middle of the grid. This would, in general, lead to the following formula:

score = houseWorth * (1 + relativeIncrease) <sup>min((gridHeight - houseHeight)/2,  (gridWidth - houseWidth)/2) - freeSpaceReq</sup>

In the above mentioned situation, this would lead to a upper bound of:

scoreL = 610000 * 1.06 <sup>min ((160 - 10,5)/2, (180-11)/2) - 6</sup> = **€33.504.880**

scoreM = 399000 * 1.04 <sup>min ((160 - 7,5)/2, (180-10)/2) - 3</sup> = **€7.057.729**

scoreS = 285000 * 1.03 <sup>min ((160 - 8)/2, (180-8)/2) - 3</sup> = **€2.465.825**

The total upper bound is **€165.393.185**. With all the constraints as they are, this situation is far from reality

The upper bound is a situation in which the free space is totally taken up by the maisons, since an increase in its free space will 
result in the maximal relative and absolute increase in total worth. This (unrealistic) situation will return an relatively loose
upper bound that surely will not be met. This upperbound is at **€16.029.000** for the 20-house setup. 

### Visualisation of the state
This problem will be displayed as a map of all the houses at their coordinates, as shown in the picture below.
![afbeelding](https://user-images.githubusercontent.com/43990565/49215236-a5795080-f3c8-11e8-9583-29a6e7dbe636.png)

## Algorithms
The first solution to this problem has been attempted by the usage of a random algorithm. This algorithm randomly places all the 
houses on a certain coordinate and checks whether or not this will lead to a valid siuation. Only valid sets will lead to an output. 
This random algorithm is not really an algorithm, since there is no heuristics involved in it. The distribution of the score of 10000
runs is plotted in the figure below.This shows the distribution is between 8M and 10.7M. 
![Alt Text](https://github.com/corne12345/Lekker-oke-/blob/master/output/random_run(10000).png)

The "heuristic" approach is to force the algorithm to perform multiple reandom runs and to save the best one. This will result for 1K
runs in a score of 10.7M (repeated tests). 

Two constructive algorithms have been built. First of all a greedy algorithm that places a house on a coordinate, which will maximize
the free space of that house and therefore results in a maximal free space of that house. This greedy algorithm is short-sighted and
doesn't take past or future attemps into account.
A seconds constructive algorithm is a depth-first algorithm that has been simplified to greatly reduce running time. 

A iterative hill climber was also constructed. This changes the coordinates of a selected house randomly (min and max can be alterered) 
and saves if this change increases the worth.

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
- Angelo Groot (Technical Assistent)

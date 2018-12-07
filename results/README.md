# Results
## Calculating the state space and the bounds of the objective function
##### State space
To calculate the upper bound of our **state space**, we used the following formula:  

  _upper bound = (field size - 1)^cars_ * _(field size - 2)^trucks_  

  As a car has a length of 2, it can move 1 step less than the total size of the
field. A truck has a length of 3, so it cannot move more than 2 steps less than
the size of the field.

  To calculate the state space of the game, we allowed the vehicles to overlap. In
fact, the vehicles are not allowed to overlap, so the actual state space will be
smaller than the function suggests. To level off this upper bound, especially for
the larger fields, we calculated new state spaces, taking into account that vehicles
in the same row or column block each other in every state. The table below shows
this upper bound of our state space for each game.


##### Objective function
As we could not find a way to calculate the upper and lower bound of the objective function of the game Rush Hour
as a whole is, we decided to establish the upper and lower bound of the objective function when our heuristics are
used. This rendered the following results:

In our first heuristic, a malus point is given for each car blocking the red car's way to the exit. As the length
of the red car is 2, the highest amount of vehicles between the red car and the exit is equal to the width of the board minus 2.
This is how we established the upper bound of the objective function for heuristic 1: 4 for a 6x6 game, 7 for a 9x9 game, and 10 for a 12x12 game. The ideal scenario would be having no vehicles blocking the red car from exiting.
Thus, the lower bound of the objective function for this heuristic is always 0.

In our second heuristic, we looked at the blockage caused by vehicles. A more detailed description can be found below, in the
section on comparing algorithms and heuristics. One point is awarded for each vehicle that could not move. Thus, the minimum would, again, be 0; in this case, the red car would be able to exit. The maximum amount of malus points depends on the amount of cars on the board. It is highly unlikely that every car is blocked, but the worst case scenario is that only one car can move. In this case, the amount of malus points given to this board would be the number of cars minus one: every car is blocked, except for one.

||Game 1|Game 2|Game 3|
|---| :--- | :--- | :---|
|_State Space_|Lower: 34|Lower: 16|Lower: 22|
||Upper: 1.000.000|Upper: 45.562.500|Upper: 9.112.500|
|_Objective function cars-to-exit_|Lower: 0|Lower: 0|Lower: 0|
||Upper: 4|Upper: 4|Upper: 4|
|_Objective function cars-in-traffic_|Lower: 0|Lower: 0|Lower: 0|
||Upper: 8|Upper: 12|Upper: 12|
|_Random Solver_|total runs: 30.000|total runs: 30.000|total runs: 30.000|
||min: 189|min: 28|min: 45|
|_Breadth-First_|34 moves|16 moves|22 moves|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_states_|4.239|939|528|
|_BF cars-to-exit_|34 moves|16 moves|23 moves|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_states_|3.748|621|411|
|_BF cars-in-traffic_|34 moves|16 moves|23 moves|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_states_|3.716|414|274|
|_Depth-First_|474 moves|901 moves|127 moves|

||Game 4|Game 5|Game 6|
|:---|:---| :---| :---|
|_State Space_|Lower: |Lower: |Lower: |
||Upper: 1,72E13|Upper: 8,43E18|Upper: 1,65E19|
|_Objective function cars-to-exit_|Lower: 0|Lower: 0|Lower: 0|
||Upper: 7|Upper: 7|Upper: 7|
|_Objective function cars-in-traffic_|Lower: 0|Lower: 0|Lower: 0|
||Upper: 22|Upper: 23|Upper: 25|
|_Random Solver_|total runs: 30.000|total runs: 30.000|total runs: 30.000|
||min: 172|min: 92|min: 93|
|_Breadth-First_|28 moves|23 moves|19 moves|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_states_|102.988|2.708.602|13.480.365|
|_BF cars-to-exit_|28 moves|23 moves|19 moves|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_states_|58.605|2.002.915|2.762.199|
|_BF cars-in-traffic_|37 moves|24 moves|19 moves|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_states_|53.322|52.863|990.144|
|_Depth-First_| -- | -- | -- |

||Game 7|
|:---|:---|
|_State Space_|Lower: |
||Upper:1,32E36|
|_Objective function cars-to-exit_|Lower: 0|
||Upper: 10|
|_Objective function cars-in-traffic_|Lower: 0|
||Upper: 43|
|_Random Solver_|total runs: 30.000|
||min: 634|
|_Breadth-First_|>14 moves|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_states_|> 12.472.669|
|_BF cars-to-exit_| -- |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_states_| -- |
|_BF cars-in-traffic_| -- |
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_states_| -- |
|_Depth-First_| -- |


## Comparing algorithms and heuristics
To solve the Rush Hour puzzles, we used three different algorithms. First, to get a grasp
of the size of our problem, we used a random solver. Later on, we also implemented
a branch and bound paradigm to narrow the scope when searching for a solution.

To find the lowest amount of steps to the solution, we used a breadth-first search algorithm. This algorithm rendered viable solutions when executed on 6x6 and 9x9 boards. However, as of game 5 and game 6, the algorithm would check millions of states before arriving at the solution.

To minimise the amount of checked states, we implemented two different heuristics. Firstly, the **cars-to-exit** heuristic, and secondly the **cars-in-traffic** heuristic.

The **cars-to-exit** heuristic checks how many cars are blocking the red car's route to the exit. Every car renders one malus point; fewer points would therefore suggest that a board is closer to the solution. In almost every case, this heuristic found a solution of as many steps as the breadth first without any heuristics. However, it had to check significantly fewer states to get there.  

The **cars-in-traffic** heuristic starts off at the red car. It checks whether the red car can move toward the exit. If not, it checks whether the first vehicle blocking the way can move. If not, it checks whether the vehicle blocking that vehicle can move, and so on. The length of this 'traffic jam' determines the amount of malus points given to a board. Again, fewer points would suggest that the board is closer to the solution. This algorithm

Thirdly, we used depth-first search to find a solution. When executed on the smaller boards, the algorithm rendered a solution, yet it subsequently needed more steps to complete the puzzle than the breadth first option.

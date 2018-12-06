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
  The **objective function** has an upper bound and a lower bound. We estimate the
lower bound to be ... and the upper bound to be ... .  

  Furthermore, we solved the first three games with three different algorithms:
a random algorithm; a breath-first algorithm; and a depth-first algorithm. To implement
a heuristic, we applied a priority queue to the breath-first algorithm: fewer cars
between the red car and the exit makes for a higher priority.

Game 4, breadth_first: Moves: 28, States: 102987, runtime +/- 1 min
breadth_first (no priority) every step: Moves: 28, States: 260697 -> same solution, twice as many states
with priority: Moves: 37, States: 53321, time +/- 2x as fast, but worse solution

Game 5, call_breadth_first, RushHour, breadth_first (without priority queue;
best solution possible), Moves: 23, States: 2.708.602, time: +/- 23 min
with priority (cars_in_traffic): Moves: 24, States: 52.835, runtime +/- 2 min

Game 6, call_breadth_first without priority queue, so best solution:
Moves: 19, States: 13.480.365, runtime +/- 2.5 hours
with priority (cars_in_traffic): Moves: 19, States: 990.143, runtime +/- 10 min (15x as fast and same solution!)

Game 7
Breadth first


||Game 1|Game 2|Game 3|
|---| :--- | :--- | :---|
|_State Space_|Lower: 34|Lower: 16|Lower: 22|
||Upper: 1.000.000|Upper: 45.562.500|Upper: 9.112.500|
|_Objective Function_|Lower: 1|Lower: 2|Lower: 3|
||Upper: |Upper: |Upper: |
|_Random Solver_|total runs: 30.000|total runs: 30.000|total runs: 30.000|
||max: 32516|max: 5058|max: 14649|
||min: 189|min: 28|min: 45|
||mean: 4469.48|mean: 977.75||mean: 2284.88|
||median: 3407.0|median: 741.5|median: 1677.0|
||stddev: 3733.6|stddev: 793.94|stddev: 2022.18|
|_Breadth-First_|34 moves|16 moves|22 moves|
|_Breath-First Priority Queue_|34 moves|16 moves|23 moves|
|_Depth-First_|474 moves|901 moves|127 moves|


||Game 4|Game 5|Game 6|
|:---|:---| :---| :---|
|_State Space_|Lower: |Lower: |Lower: |
||Upper: 1,72E13|Upper: 8,43E18|Upper: 1,65E19|
|_Objective Function_|Lower: 2|Lower: 1|Lower: 2|
||Upper: |Upper: |Upper: |
|_Random Solver_|total runs: 30.000|total runs: 30.000|total runs: 30.000|
||min: 172|min: 92|min: 93|
|_Breadth-First_| -- | -- | -- |
|_Breath-First Priority Queue_| -- | -- | -- |
|_Depth-First_| -- | -- | -- |

||Game 7|
|:---|:---|
|_State Space_|Lower: |
||Upper:1,32E36|
|_Objective Function_|Lower: 2|
||Upper: |
|_Random Solver_|total runs: 30.000|
||min: 634|
|_Breadth-First_| -- |
|_Breath-First Priority Queue_| -- |
|_Depth-First_| -- |


## Comparing algorithms and heuristics
To solve the Rush Hour puzzles, we used three different algorithms. First, to get a grasp
of the size of our problem, we used a random solver. Later on, we also implemented
a branch and bound paradigm to narrow the scope when searching for a solution.

To find the lowest amount of steps to the solution, we used a breadth-first search algorithm. This algorithm rendered viable solutions when executed on 6x6 and 9x9 boards. However, as of game 5 and game 6, the algorithm would check millions of states before arriving at the solution.

To minimise the amount of checked states, we implemented two different heuristics. Firstly, the **cars-to-exit** heuristic, and secondly the **cars-in-traffic** heuristic.

The **cars-to-exit** heuristic checks how many cars are blocking the red car's route to the exit. Every car renders one malus point; fewer points would therefore suggest that a board is closer to the solution.

The **cars-in-traffic** heuristic starts off at the red car. It checks whether the red car can move toward the exit. If not, it checks whether the first vehicle blocking the way can move. If not, it checks whether the vehicle blocking that vehicle can move, and so on. The length of this 'traffic jam' determines the amount of malus points given to a board. Again, fewer points would suggest that the board is closer to the solution.

 Thirdly, we used depth-first search to find a solution. When executed on the smaller boards, the algorithm rendered a solution. 

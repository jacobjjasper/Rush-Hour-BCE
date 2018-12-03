# Results
### Calculating the state space and the bounds of the objective function
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

  The **objective function** has an upper bound and a lower bound. We estimate the
lower bound to be ... and the upper bound to be ... .  

  Furthermore, we solved the first three games with three different algorithms:
a random algorithm; a breath-first algorithm; and a depth-first algorithm. To implement
a heuristic, we applied a priority queue to the breath-first algorithm: fewer cars
between the red car and the exit makes for a higher priority.

  However, as of the fourth puzzle, there seems to be a bug in our algorithm:
after about 50 (game 4) or 26 layers (game 5), the queue seems to be empty and
the algorithm has not returned a solution.


||Game 1|Game 2|Game 3|
|---| :--- | :--- | :---|
|_State Space_|Lower: 34|Lower: 16|Lower: 22|
||Upper: 1.000.000|Upper: 45.562.500|Upper: 9.112.500|
|_Objective Function_|Lower: 1|Lower: 2|Lower: 3|
||Upper: |Upper: |Upper: |
|_Random Solver_|total runs: 1000|total runs: 1000|total runs: 1000|
||max: 32516|max: 5058|max: 14649|
||min: 293|min: 38|min: 82|
||mean: 4469.48|mean: 977.75|
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
|_Random Solver_|total runs: 0|total runs: 0|total runs: 0|
||max: |max: |max: |
||min: |min: |min: |
||mean: 2284.88|mean: |mean: |mean: |
||median: |median: |median: |
||stddev: |stddev: |stddev: |
|_Breadth-First_| -- | -- | -- |
|_Breath-First Priority Queue_| -- | -- | -- |
|_Depth-First_| -- | -- | -- |

||Game 7|
|:---|:---|
|_State Space_|Lower: |
||Upper:1,32E36|
|_Objective Function_|Lower: 2|
||Upper: |
|_Random Solver_|total runs: 0|
||max: |
||min: |
||mean: |
||median: |
||stddev: |
|_Breadth-First_| -- |
|_Breath-First Priority Queue_| -- |
|_Depth-First_| -- |

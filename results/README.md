# Results
### Calculating the state space and the bounds of the objective function
To calculate the upper bound of our **state space**, we used the following formula:  
  _upper bound = (field size - 1)^cars * _(field size - 2)^trucks_  
  As a car has a length of 2, it can move 1 step less than the total size of the
field. A truck has a length of 3, so it cannot move more than 2 steps less than
the size of the field.
  To calculate the state space of the game, we allowed the vehicles to overlap. In
fact, the vehicles are not allowed to overlap, so the actual state space will be
smaller than the function suggests. The table below shows the upper bound of our
state space for each game.
  The **objective function** has an upper bound and a lower bound. We estimate the
lower bound to be ... and the upper bound to be ... .




||Game 1|Game 2|Game 3|Game 4|Game 5|Game 6|Game 7|
|---| :--- | :--- | :---| :---| :---| :---| :---|
|_State Space_|Lower Bound: 34|Lower Bound: 16|Lower Bound: 22|Lower Bound: |Lower Bound: |Lower Bound: |Lower Bound: |
||Upper Bound: 1.000.000|Upper Bound: 976.562.500|Upper Bound:976.562.500|Upper Bound: 2,43E18|Upper Bound:2,12E21|Upper Bound: 1,04E23 |Upper Bound:1,31E44|
|_Objective Function_|Lower Bound: 1|Lower Bound: 1|Lower Bound: 1|Lower Bound: 1|Lower Bound: 1|Lower Bound: 1|Lower Bound: 1|
||Upper Bound: |Upper Bound: |Upper Bound: |Upper Bound: |Upper Bound: |Upper Bound: |Upper Bound: |
|_Random Solver_|total runs: 1000|total runs: 1000|total runs: 1000|total runs: 0|total runs: 0|total runs: 0|total runs: 0|
||max: 32516|max: 5058|max: 14649|max: |max: |max: |max: |
||min: 293|min: 38|min: 82|min: |min: |min: |min: |
||mean: 4469.48|mean: 977.75|mean: 2284.88|mean: |mean: |mean: |mean: |
||median: 3407.0|median: 741.5|median: 1677.0|median: |median: |median: |median: |
||stddev: 3733.6|stddev: 793.94|stddev: 2022.18|stddev: |stddev: |stddev: |stddev: |
|_Breadth-First_|34 moves|16 moves|22 moves|-- moves|-- moves|-- moves|-- moves|
|_Breath-First Priority Queue_|33 moves|15 moves|22 moves|-- moves|-- moves|-- moves|-- moves|
|_Depth-First_|474 moves|901 moves|127 moves|-- moves|-- moves|-- moves|-- moves|

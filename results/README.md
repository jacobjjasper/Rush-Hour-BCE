# Results
### Calculating the state space and the bounds of the objective function
To calculate the upper bound of our state space, we used the following formula:  
_upper bound = (field size - 1)^cars * (field size - 2)^trucks_




||Game 1|Game 2|Game 3|
|---| :--- | :--- | :---|
|_State Space_|Lower Bound: 34|Lower Bound: 16|Lower Bound: 22|
||Upper Bound: |Upper Bound: |Upper Bound:|
|_Objective Function_|Lower Bound: 1|Lower Bound: 1|Lower Bound: 1|
||Upper Bound: |Upper Bound: |Upper Bound: |
|_Random Solver_|total runs: 1000|total runs: 1000|total runs: 1000|
||max: 32516|max: 5058|max: 14649|
||min: 293|min: 38|min: 82|
||mean: 4469.48|mean: 977.75|mean: 2284.88|
||median: 3407.0|median: 741.5|median: 1677.0|
||stddev: 3733.6|stddev: 793.94|stddev: 2022.18|
|_Breadth-First_|34 moves|16 moves|22 moves|
|_Breath-First Priority Queue_|33 moves|15 moves|22 moves|
|_Depth-First_|474 moves|901 moves|127 moves|

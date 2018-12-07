# Rush Hour BCE :car:
#### Heuristics problem Rush Hour game

Rush Hour looks like an easy game, but can be quite hard. The goal is to move the red car to the exit of the puzzle board. Cars and trucks block the road. Vehicles can only be moved along their orientation. The goal of this project is to solve Rush Hour boards with one or more algorithms, while trying to determine the shortest possible solution.



## Data
The following games will be played. The data files of these games are in the folder 'data2' and contain:
* The game board size (e.g. 6, 9, or 12) on the first line
* The red car on the second line
* Other vehicles thereafter (no particular order)
* A vehicle is build up of:
  * 'C' or 'T' (for Car or Truck)
  * X-coordinate (leftest)
  * Y-coordinate (upmost)
  * 'H' or 'V' (for horizontal or vertical positioning)
  * The upper-left corner of the game field gets coordinate(0,0)


##### 6x6 (games 1, 2, and 3)
<img title = "Game 1" src="http://heuristieken.nl/wiki/images/9/95/Rushhour6x6_1.jpg" width="150" style="max-width:100%;"> <img title = "Game 2" src="http://heuristieken.nl/wiki/images/a/aa/Rushhour6x6_2.jpg" width="150" style="max-width:100%;"> <img title = "Game 3" src="http://heuristieken.nl/wiki/images/c/c7/Rushhour6x6_3.jpg" width="150" style="max-width:100%;">

##### 9x9 (games 4, 5, and 6)
<img title = "Game 4" src="http://heuristieken.nl/wiki/images/9/96/Rushhour9x9_1.jpg" width="150" style="max-width:100%;"> <img title = "Game 5" src="http://heuristieken.nl/wiki/images/1/1e/Rushhour9x9_2.jpg" width="150" style="max-width:100%;"> <img title = "Game 6" src="http://heuristieken.nl/wiki/images/9/95/Rushhour9x9_3.jpg" width="150" style="max-width:100%;">

##### 12x12 (game 7)
<img title = "Game 7" src="http://heuristieken.nl/wiki/images/2/26/Rushhour12x12_1.jpg" width="150" style="max-width:100%;">


## Files
This repository is divided into [code](https://github.com/jacobjjasper/Rush-Hour-BCE/tree/master/code), [data](https://github.com/jacobjjasper/Rush-Hour-BCE/tree/master/data), [results](https://github.com/jacobjjasper/Rush-Hour-BCE/tree/master/results) and [main.py](https://github.com/jacobjjasper/Rush-Hour-BCE/blob/master/main.py). The data folder holds all the game data (loading in Rush Hour boards) and some images for visualisations. The results file contains csv-files with data from the random-algorithm and some general information about the state space of the problem, fastest solutions and other outcomes of our exploration. The code folder is made up of:
* algorithms.py - all algorithms
* rush.py - old version of rush2.py
* rush2.py - general RushHour class, holds most of the functions
* vehicle.py - class Vehicle to represent a car or truck on the board


## How to start Rush Hour
You can run the game as follows. Insert game number 1 to 7, corresponding to the images above. 
```
python3 main.py <game_number> <algorithm> <optionals>
```

### Command lines
Show game
```
python3 main.py 1 show
```
<br/>Show solution with visualization
```
python3 main.py 1 play
```
<br/>Show random Branch & Bound line graph
```
python3 main.py 1 random False 0
```
<br/>Run game random 1000 times with bound starting at 500 (bound is optional), Boolean is for showing the field
```
python3 main.py 1 random False 1000 500
```
<br/>Run Breadth First algorithm to find shortest solution
```
python3 main.py 1 breadth_first
```
<br/>Run Best First algorithm to apply heuristic cars_to_exit
```
python3 main.py 1 best_first cars_to_exit
```
<br/>Run Breadth First algorithm to apply heuristic cars_in_traffic
```
python3 main.py 1 best_first cars_in_traffic
```
<br/>

## Results
The results can be found in the [results](https://github.com/jacobjjasper/Rush-Hour-BCE/tree/master/results) folder. The folder contains a readme with explanations.

## Challenges
The first challenge when trying to build a Rush Hour solver is the immense size the game's state space can attain. In the [results](https://github.com/jacobjjasper/Rush-Hour-BCE/tree/master/results) folder, one can find a more detailed description of our state space. In short, the state space of Game 1 is in the order of magnitude of 1.000.000, whereas the state space of Game 7 is in the order of magnitude of 10E44. To prevent checking certain states twice, we need to keep track of all the states that have been visited. Therefore, exploring the entire state space seems to be a sheer impossible job: to find a solution, it is imperative that it be found before the computer uses all of its (working) memory. We considered saving memory by only storing the previous and the current layers (using breadth first). Our reasoning behind this was, that a 'grandparent board' can only be reached from the current board by passing through a 'parent board'. At first, we were weary to use this paradigm. We feared that a loop would still be possible when the loop existed of, for example, four fields. However, we have tried to use the paradigm, reasoning that we could still end up in an extensive loop, but the chances of this happening were quite slim.
A second difficulty when solving a game of Rush Hour, is that there is no known 'end state' to work towards; thus, when assessing a state, one can almost never assert how close to the solution that board is situated. Moreover, after a move, a board (state A) can seem to be further away from the solution than its predecessor (state B), but after a next move, its successor (state C) can be a lot closer to the solution than said predecessor (state A). Therefore, we experienced great difficulty in determining whether a heuristic would be admissive. 

When comparing the number of states visited while looking for the solution, it seems as though, for our solver, certain games are more difficult to solve than others: for instance, our breadth-first, no-heuristic solver found a solution of 28 steps for Game 4 and checked approximately 100.000 states to get there. However, for Game 6 (which is also a 9x9 game), 19 steps were needed, yet our solver had to check over 13 million states to find a solution. These findings beg the question: why is Game 6 so much harder than Game 4? Or, ultimately: what makes a Rush Hour board hard to solve? 

The difficulty of a Rush Hour board is dependent on at least two factors: the amount of possibilities (state space) and the amount of steps to the solution. For example: two games can be solved in 19 steps, though one could have a larger state space which makes it harder for the player to choose which vehicles to move. Of course, the hardness of the game could also depend on the strategy and intuition of the player, but for an algorithm these factors together might define the difficulty of the game.

## Students
* Jacob Jasper (10650385)
* Tobias Maätita (10730109)
* Fried Schölvinck (10729267)

University of Amsterdam, Heuristieken

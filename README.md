# Rush Hour BCE :car:
Heuristics problem Rush Hour game

Rush Hour looks like an easy game, but can be quite hard. The goal is to move the red car to the exit of the puzzle board. Car and trucks block the road. Vehicles can only be moved in within their orientation. The goal of this project is to solve Rush Hour boards wit h one or more algorithms, while trying to determine the shortest possible solution.


## Data (game boards)
The following games will be played. The data files of these games are in the folder 'data2' and contain:
* The game board size (e.g. 6, 9, or 12) on the first line
* The red car on the second line
* Other vehicles thereafter (no particular order)
* A vehicle is build up of:
  * 'C' or 'T' (for Car or Truck)
  * X-coordinate (leftest)
  * Y-coordinate (upmost)
  * 'H' or 'V' (for horizontal or vertical positioning)
  * The upper-left corner of the game field get's coordinate (0,0)


##### 6x6
<img src="http://heuristieken.nl/wiki/images/9/95/Rushhour6x6_1.jpg" width="150" style="max-width:100%;"> <img src="http://heuristieken.nl/wiki/images/a/aa/Rushhour6x6_2.jpg" width="150" style="max-width:100%;"> <img src="http://heuristieken.nl/wiki/images/c/c7/Rushhour6x6_3.jpg" width="150" style="max-width:100%;">

##### 9x9
<img src="http://heuristieken.nl/wiki/images/9/96/Rushhour9x9_1.jpg" width="150" style="max-width:100%;"> <img src="http://heuristieken.nl/wiki/images/1/1e/Rushhour9x9_2.jpg" width="150" style="max-width:100%;"> <img src="http://heuristieken.nl/wiki/images/9/95/Rushhour9x9_3.jpg" width="150" style="max-width:100%;">

##### 12x12
<img src="http://heuristieken.nl/wiki/images/2/26/Rushhour12x12_1.jpg" width="150" style="max-width:100%;">


## Files
This repository is devides into code, data, results and main.py. For our latest versions, we used the data2 file and code/rush2.py. The data folder holds all the game data (loading in Rush Hour boards) and some images for visualisations. The results file contains csv-files with data from the random-algorithm and some general information about the state space of the problem, fastest solutions and other outcomes of our exploration. The code folder is made up of:
* algorithms.py - all algorithms
* rush.py - old version of rush2.py
* rush2.py - general RushHour class, holds most of the functions
* vehicle.py - class Vehicle to represent a car or truck on the board


## How to start Rush Hour
You can run the game as follows.
```
python3 main.py <game_number> <algorithm> <optionals>
```

### Shortkeys
Show game
```
python3 main.py 1 show
```
<br/>Run game random 1000 times with bound starting at 500 (bound is optional)
```
python3 main.py 1 random 1000 500
```
<br/>Run Breadth First algorithm to find shortest solution
```
python3 main.py 1 breadth_first
```
<br/>Run Breadth First algorithm to find a short solution faster
```
python3 main.py 1 breadth_first_priority
```
<br/>
```
python3 main.py 1
```

## Students
* Jacob Jasper
* Tobias Maätita
* Fried Schölvinck

University of Amsterdam, Heuristieken

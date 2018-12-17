# Data
This folder contains data for loading in and visualizing Rush Hour games. A game.txt file is set up as follows.

* The game board size (e.g. 6, 9, or 12) on the first line
* The red car on the second line
* Other vehicles thereafter (no particular order)
* A vehicle (one line) is build up of:
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

## Rush Hour Images
This subfolder contains images for visualizing 6x6, 9x9 or 12x12 Rush Hour boards up to 40 vehicles. 
These files are used by the function show_field in [rush.py](https://github.com/jacobjjasper/Rush-Hour-BCE/tree/master/data/rush.py).

# imports
from src.Grid import Grid

__author__ = 'Emma'
__project__ = 'Draughts'


# define main
def main():
    # create grid of width and height
    grid = Grid(8,8)
    # print grid
    grid.printGrid()


# run from main
if __name__ == "__main__":
    main()

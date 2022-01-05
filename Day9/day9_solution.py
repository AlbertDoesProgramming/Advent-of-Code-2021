import numpy as np
def main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return f.read()

# find low points on grid
# a low point is the the lowest number, based on adjacent numbers - up,down,left,right
# risk is 1 + height. What is sum of risk?

# Make Grid
# Find adjacent values to the current
# 

    def getAdjacent(grid, point):
        for point in grid:
            continue
        return
        
    def getLowPoints(input: str):
        prelim = np.array([[int(y) for y in list(x)] for x in list(readfile(input).split('\n'))])
        
        return prelim

    print(f'Problem 2 Solution : \n{getLowPoints(input)}')

if __name__ == "__main__":
    main('Day9\day9_input.txt')
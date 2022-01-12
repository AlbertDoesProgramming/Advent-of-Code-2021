import numpy as np
from numpy import vstack
def main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return f.read()

    def getAdjacentRows(listOfLists, index):

        currentRow = np.array(listOfLists[index])
        if index == len(listOfLists)-1:
            previousRow = np.array(listOfLists[index-1])
            miniGrid = np.vstack((previousRow, currentRow))
        elif index == 0:
            nextRow = np.array(listOfLists[index+1])
            miniGrid = np.vstack((currentRow, nextRow))
        else:
            previousRow = np.array(listOfLists[index-1])
            nextRow = np.array(listOfLists[index+1])
            miniGrid = np.vstack((previousRow, currentRow, nextRow))
        return miniGrid

    def getAdjacentNumsOnly(grid, i, rowType):
        currentRow = 1
        up = 99
        down = 99
        left = 99
        right = 99
        if rowType == 'first':
            currentRow = 0
            if i == 0:
                num = grid[currentRow][i]
                down = grid[currentRow+1][i]
                right = grid[currentRow][i+1]
            elif i == len(grid[currentRow])-1:
                num = grid[currentRow][i]
                down = grid[currentRow+1][i]
                left = grid[currentRow][i-1]
            else:
                num = grid[currentRow][i]
                down = grid[currentRow+1][i]
                right = grid[currentRow][i+1]
                left = grid[currentRow][i-1]
            microGrid = np.vstack(np.array([[99, up, 99],[left, num, right],[99, down, 99]]))
        elif rowType == 'last':
            if i == 0:
                num = grid[currentRow][i]
                up = grid[currentRow-1][i]
                right = grid[currentRow][i+1]
            elif i == len(grid[currentRow])-1:
                num = grid[currentRow][i]
                up = grid[currentRow-1][i]
                left = grid[currentRow][i-1]
            else:
                num = grid[currentRow][i]
                up = grid[currentRow-1][i]
                right = grid[currentRow][i+1]
                left = grid[currentRow][i-1]
            microGrid = np.vstack(np.array([[99, up, 99],[left, num, right],[99, down, 99]]))
        else:
            if i == 0:
                num = grid[currentRow][i]
                up = grid[currentRow-1][i]
                down = grid[currentRow+1][i]
                right = grid[currentRow][i+1]
            elif i == len(grid[currentRow])-1:
                num = grid[currentRow][i]
                up = grid[currentRow-1][i]
                down = grid[currentRow+1][i]
                left = grid[currentRow][i-1]
            else:
                num = grid[currentRow][i]
                up = grid[currentRow-1][i]
                down = grid[currentRow+1][i]
                right = grid[currentRow][i+1]
                left = grid[currentRow][i-1]
            microGrid = np.vstack(np.array([[99, up, 99],[left, num, right],[99, down, 99]]))
        return microGrid

    def getLowPoints2(input: str):
        grid = np.array([[int(y) for y in list(x)] for x in list(readfile(input).split('\n'))])
        lowPoints1 = []
        currentRow = 0
        lenDataset = len(grid)-1
        for y in range(len(grid)):
            rowType = ''
            adjacentRows = getAdjacentRows(grid, y)
            if y == 0:
                rowType = 'first'
            elif y == lenDataset:
                rowType = 'last'
            for x in range(len(adjacentRows[currentRow])):
                microGrid = getAdjacentNumsOnly(adjacentRows, x, rowType)
                num = microGrid[1][1]
                gridListP1 =  np.delete(microGrid, 4)
                gridListP1 = [item for item in gridListP1 if item != 99]
                if all(z > num for z in gridListP1):
                    lowPoints1.append((num,[y,x]))        
        return lowPoints1
    
    lowPoints = getLowPoints2(input)
    lowPoints1 = np.array([x for x,y in lowPoints])
    print(f'Problem 1 Solution : \n{sum(lowPoints1+1)}')

    def getNodes(matrix, x, y, nodes, maxHeight, maxWidth):
        if x < 0 or y < 0 or x > maxHeight or y > maxWidth or matrix[x][y] == 9 or (x, y) in nodes:
            return
        nodes.append((x, y))
        getNodes(matrix, x, y + 1, nodes, maxHeight, maxWidth)
        getNodes(matrix, x, y - 1, nodes, maxHeight, maxWidth)
        getNodes(matrix, x - 1, y, nodes, maxHeight, maxWidth)
        getNodes(matrix, x + 1, y, nodes, maxHeight, maxWidth)

    grid = np.array([[int(y) for y in list(x)] for x in list(readfile(input).split('\n'))])
    basins = []
    maxHeight = len(grid) - 1
    maxWidth = len(grid[0]) - 1
    for depths in lowPoints:
        z, [x, y] = depths
        points = []
        getNodes(grid, x, y, points, maxHeight, maxWidth)
        basins.append(len(points))

    basins.sort(reverse=True)
    print(f"Problem 2 Solution: \n{basins[0] * basins[1] * basins[2]}")

if __name__ == "__main__":
    main('Day9\day9_input.txt')

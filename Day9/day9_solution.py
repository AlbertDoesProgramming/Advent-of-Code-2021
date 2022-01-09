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
            miniGrid = np.vstack((currentRow,  previousRow))
        elif index == 0:
            nextRow = np.array(listOfLists[index+1])
            miniGrid = np.vstack((currentRow, nextRow))
        else:
            previousRow = np.array(listOfLists[index-1])
            nextRow = np.array(listOfLists[index+1])
            miniGrid = np.vstack((currentRow, nextRow, previousRow))
        return miniGrid
    
    def getAdjacentNums(grid, index, lastRowIndex):
        lowPoints1 = []
        lowPoints2 = []
        currentRow = 0
        rowType = ''
        if index == 0:
            rowType = 'first'
        elif index == lastRowIndex:
            rowType = 'last'
        for i in range(len(grid[currentRow])):
            testSet1 = []
            testSet2 = []
            if rowType == 'first':    
                if i == 0:
                    num = grid[currentRow][i]
                    down = grid[currentRow+1][i]
                    right = grid[currentRow][i+1]
                    rightDown = grid[currentRow+1][i+1]
                    testSet1 = {down,right}
                    testSet2 = {down,right,rightDown}
                elif i == len(grid[currentRow])-1:
                    num = grid[currentRow][i]
                    down = grid[currentRow+1][i]
                    left = grid[currentRow][i-1]
                    leftDown = grid[currentRow+1][i-1]
                    testSet1 = {down,left}
                    testSet2 = {down,left,leftDown}
                else:
                    num = grid[currentRow][i]
                    down = grid[currentRow+1][i]
                    right = grid[currentRow][i+1]
                    rightDown = grid[currentRow+1][i+1]
                    left = grid[currentRow][i-1]
                    leftDown = grid[currentRow+1][i-1]
                    testSet1 = {down,left,right}
                    testSet2 = {down,left,leftDown,right,rightDown}
                
                if all(x > num for x in testSet1) :
                    lowPoints1.append(num)
                if all(x > num for x in testSet2) :
                    lowPoints2.append(num)
                
                

            elif rowType == 'last':
                if i == 0:
                    num = grid[currentRow][i]
                    up = grid[currentRow-1][i]
                    right = grid[currentRow][i+1]
                    rightUp = grid[currentRow+1][i+1]
                    testSet1 = {up,right}
                    testSet2 = {up,right,rightUp}
                elif i == len(grid[currentRow])-1:
                    num = grid[currentRow][i]
                    up = grid[currentRow-1][i]
                    left = grid[currentRow][i-1]
                    leftUp = grid[currentRow-1][i-1]
                    testSet1 = {up,left}
                    testSet2 = {up,left,leftUp}
                else:
                    num = grid[currentRow][i]
                    up = grid[currentRow-1][i]
                    right = grid[currentRow][i+1]
                    rightUp = grid[currentRow-1][i+1]
                    left = grid[currentRow][i-1]
                    leftUp = grid[currentRow-1][i-1]
                    testSet1 = {up,left,right}
                    testSet2 = {up,left,leftUp,right,rightUp}
                    
                if all(x > num for x in testSet1) :
                    lowPoints1.append(num)
                if all(x > num for x in testSet2) :
                    lowPoints2.append(num)

            else:
                if i == 0:
                    num = grid[currentRow][i]
                    up = grid[currentRow-1][i]
                    down = grid[currentRow+1][i]
                    right = grid[currentRow][i+1]
                    rightDown = grid[currentRow-1][i+1]
                    rightUp = grid[currentRow-1][i+1]
                    testSet1 = {up,right,down}
                    testSet2 = {up,down,right,rightUp,rightDown}

                elif i == len(grid[currentRow])-1:
                    num = grid[currentRow][i]
                    up = grid[currentRow-1][i]
                    down = grid[currentRow+1][i]
                    left = grid[currentRow][i-1]
                    leftUp = grid[currentRow-1][i-1]
                    leftDown = grid[currentRow+1][i-1]
                    testSet1 = {up,down,left}
                    testSet2 = {up,down,left,leftUp,leftDown}
                else:
                    num = grid[currentRow][i]
                    up = grid[currentRow-1][i]
                    right = grid[currentRow][i+1]
                    rightUp = grid[currentRow-1][i+1]
                    left = grid[currentRow][i-1]
                    leftUp = grid[currentRow-1][i-1]
                    down = grid[currentRow+1][i]
                    leftDown = grid[currentRow+1][i-1]
                    rightDown = grid[currentRow-1][i+1]
                    testSet1 = {up,down,left,right}
                    testSet2 = {up,down,left,leftUp,leftDown,right,rightUp,rightDown}               
                if all(x > num for x in testSet1) :
                    lowPoints1.append(num)
                if all(x > num for x in testSet2) :
                    lowPoints2.append(num)
                
        return lowPoints1, lowPoints2
        
    def getLowPoints(input: str):
        prelim = np.array([[int(y) for y in list(x)] for x in list(readfile(input).split('\n'))])
        lowPoints1 = []
        lowPoints2 = []
        lenDataset = len(prelim)-1
        for i in range(len(prelim)):
            minigrid = getAdjacentRows(prelim, i)
            points1, points2 = getAdjacentNums(minigrid, i, lenDataset)
            if points1 != []:
                lowPoints1.append(points1)
                lowPoints2.append(points2)
        return np.hstack(np.array(lowPoints1)), np.hstack(np.array(lowPoints2))

    lowPoints1, lowPoints2 = getLowPoints(input)   
    print(f'Problem 1 Solution : \n{sum(lowPoints1+1)}')
    print(f'Problem 2 Solution : \n{lowPoints2}')

if __name__ == "__main__":
    main('Day9\day9_input.txt')

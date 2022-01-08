import numpy as np
from numpy import vstack
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

    def getAdjacentRows(listOfLists, index):
    # Easy way, get the adjacent rows
        
        currentRow = np.array(listOfLists[index])
        if index == -1:
            previousRow =np.array( listOfLists[index-1])
            miniGrid = np.vstack((currentRow,  previousRow))
        elif index == 0:
            nextRow = np.array(listOfLists[index+1])
            miniGrid = np.vstack((currentRow, nextRow))
        else:
            previousRow =np.array( listOfLists[index-1])
            nextRow = np.array(listOfLists[index+1])
            miniGrid = np.vstack((currentRow, nextRow, previousRow))
        return miniGrid
    
    def getAdjacentNums(grid):
        lowPoints1 = []
        lowPoints2 = []

        for i in range(len(grid)):
            if i == 0:    
                for nums in range(len(grid[i])):
                    if nums == 0:
                        num = grid[i][nums]
                        down = grid[i+1][nums]
                        right = grid[i][nums+1]
                        rightDown = grid[i+1][nums+1]
                        testSet1 = {down,right}
                        testSet2 = {down,right,rightDown}
                    if nums == -1:
                        num = grid[i][nums]
                        down = grid[i+1][nums]
                        left = grid[i][nums-1]
                        leftDown = grid[i+1][nums-1]
                        testSet1 = {down,left}
                        testSet2 = {down,left,leftDown}
                    else:
                        num = grid[i][nums]
                        down = grid[i+1][nums]
                        right = grid[i][nums+1]
                        rightDown = grid[i+1][nums+1]
                        left = grid[i][nums-1]
                        leftDown = grid[i+1][nums-1]
                        testSet1 = {down,left,leftDown,right,rightDown}
                        testSet2 = {down,left,leftDown,right,rightDown}
                    
                    if [x for x in testSet1 if x > num and x != num] != []:
                        lowPoints1.append(num)
                    if [x for x in testSet2 if x > num and x != num] != []:
                        lowPoints2.append(num)

            elif i == -1:
                for nums in range(len(grid[i])):
                    if nums == 0:
                        num = grid[i][nums]
                        up = grid[i+1][nums]
                        down = grid[i+1][nums]
                        right = grid[i][nums+1]
                        rightUp = grid[i+1][nums+1]
                        rightDown = grid[i-1][nums+1]
                        testSet1 = {up,right}
                        testSet2 = {up,right,rightUp}
                    if nums == -1:
                        num = grid[i][nums]
                        up = grid[i+1][nums]
                        down = grid[i+1][nums]
                        left = grid[i][nums-1]
                        leftUp = grid[i+1][nums-1]
                        leftDown = grid[i+1][nums-1]
                        testSet1 = {up,left}
                        testSet2 = {up,left,leftUp}
                    else:
                        num = grid[i][nums]
                        up = grid[i+1][nums]
                        down = grid[i+1][nums]
                        right = grid[i][nums+1]
                        rightDown = grid[i+1][nums+1]
                        rightUp = grid[i+1][nums+1]
                        left = grid[i][nums-1]
                        leftDown = grid[i+1][nums-1]
                        leftUp = grid[i+1][nums-1]
                        testSet1 = {up,left,leftUp,right,rightUp}
                        testSet2 = {up,left,leftUp,right,rightUp}
                    
                    if [x for x in testSet1 if x > num and x != num] != []:
                        lowPoints1.append(num)
                    if [x for x in testSet2 if x > num and x != num] != []:
                        lowPoints2.append(num)
            
            else:
                for nums in range(len(grid[i])):
                    if nums == 0:
                        num = grid[i][nums]
                        up = grid[i+1][nums]
                        right = grid[i][nums+1]
                        rightUp = grid[i+1][nums+1]
                        testSet1 = {up,right}
                        testSet2 = {up,right,rightUp}
                    if nums == -1:
                        num = grid[i][nums]
                        up = grid[i+1][nums]
                        left = grid[i][nums-1]
                        leftUp = grid[i+1][nums-1]
                        testSet1 = {up,left}
                        testSet2 = {up,left,leftUp}
                    else:
                        num = grid[i][nums]
                        up = grid[i+1][nums]
                        right = grid[i][nums+1]
                        rightUp = grid[i+1][nums+1]
                        left = grid[i][nums-1]
                        leftUp = grid[i+1][nums-1]
                        testSet1 = {up,left,leftUp,right,rightUp}
                        testSet2 = {up,left,leftUp,right,rightUp}
                    
                    if [x for x in testSet1 if x > num and x != num] != []:
                        lowPoints1.append(num)
                    if [x for x in testSet2 if x > num and x != num] != []:
                        lowPoints2.append(num)
        return lowPoints1, lowPoints2
        
    def getLowPoints(input: str):
        prelim = np.array( [[int(y) for y in list(x)] for x in list(readfile(input).split('\n'))])
        lowPoints1 = []
        lowPoints2 = []
        for i in range(len(prelim)):
            x = getAdjacentRows(prelim, i)
            points1, points2 = getAdjacentNums(x)
            if points1 != []:
                lowPoints1.append(points1)
                lowPoints2.append(points2)        
        return lowPoints1, lowPoints2
    print(getLowPoints(input))

   # print(f'Problem 2 Solution : \n{getLowPoints(input)}')

if __name__ == "__main__":
    main('Day9\day9_input.txt')

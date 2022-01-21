import numpy as np

def main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return f.read().split('\n')
    
    def getAdjacentRows(matrix, position):
        adj = []      
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                xRange = range(0, matrix.shape[0])  # X bounds
                yRange = range(0, matrix.shape[1])  # Y bounds               
                (newX, newY) = (position[0]+dx, position[1]+dy)  # adjacent cell
                
                if (newX in xRange) and (newY in yRange) and (dx, dy) != (0, 0):
                    adj.append((newX, newY))
        return adj
 
    def getCounts(matrix, flashCount, step, stepArray):
        for yGrid, row in enumerate(matrix):
            for xGrid, col in enumerate(row):
                if matrix[yGrid][xGrid] > 9:
                    adjacent = getAdjacentRows(np.array(matrix), (yGrid,xGrid))
                    matrix[yGrid][xGrid] = -1
                    flashCount += 1
                    for adjRow, adjCol in adjacent:
                        if matrix[adjRow][adjCol] >= 0:
                                matrix[adjRow][adjCol] += 1        
        if np.any(matrix >= 10):
            matrix, flashCount, step = getCounts(matrix, flashCount, step, stepArray)            
        
        if np.all(matrix == -1):
            stepArray.append(step)
            
        for yFinal, row in enumerate(matrix):
            for xFinal, col in enumerate(row):
                if matrix[yFinal][xFinal] == -1:
                    matrix[yFinal][xFinal] += 1
        
        
        return matrix, flashCount, stepArray
    
    def solution(input):
        f = readfile(input)
        grid = np.array([[int(y) for y in x] for x in f])
        grid2 = np.array([[int(y) for y in x] for x in f])
        flashCount = 0
        flashCount2 = 0
        stepList = []
        stepList2 = []
        for i in range(100):        
            grid += 1
            grid, flashCount, na1  = getCounts(grid, flashCount, i, stepList)
        
        for s in range(1000):        
            grid2 += 1
            grid2, na2, stepList = getCounts(grid2, flashCount2, s, stepList2)
        
        return flashCount, stepList 
    
    flashCount, stepArray = solution(input)
    
    print(f"Part 1 answer is:  {flashCount}")
    print(f"Part 2 answer is:  {stepArray[0]+1}")
    
if __name__ == "__main__":
    main('Day11\day11_input.txt')
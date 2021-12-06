import numpy as np

def main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return f.read().split('\n\n') 

    def getGrids(input):
        lines = readfile(input)
        scoring_nums = lines.pop(0).split(',')
        scoring_nums = [int(x) for x in scoring_nums]
        lines = [x.split('\n') for x in lines] 
        lines = [[y.split(' ') for y in x] for x in lines]
        lines = [[[int(z) for z in y if z != ''] for y in x] for x in lines]
        grids = [ np.array(x) for x in lines]
        return grids, scoring_nums

    def checkIfWon(grid):
        for y in range(grid.shape[0]):
            if np.all(grid[y,:] < 0): return True
        for x in range(grid.shape[1]):
            if np.all(grid[:,x] < 0): return True
        return False

    def getWinners(input):
        winners = []
        grids, scoring_nums = getGrids(input)
        for score in scoring_nums:
            for i in range(len(grids)-1, -1, -1):
                grid = grids[i]
                grid[grid == score] *= -1
                if checkIfWon(grid):
                    winners.append((grid, score))
                    grids.pop(i)
        return winners
        
    def results(grid, num):
        return np.sum(grid[grid > 0]) * num

    print(f"Problem 1 answer is: {results(*getWinners(input)[0])}")
    print(f"Problem 1 answer is: {results(*getWinners(input)[-1])}")
if __name__ == "__main__":
    main('Day4\day4_input.txt')
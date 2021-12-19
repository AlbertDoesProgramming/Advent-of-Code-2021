import numpy as np
from numpy import bincount

def main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return f.read().strip().split(',')

    def getFishCountEfficiently(input: list, days: int):
        listOfFish = np.array([int(x) for x in readfile(input)])
        counter = np.concatenate((bincount(listOfFish), [0,0,0]))
        for day in range(days):
            reproducers = counter[0]
            for i in range(8):
                counter[i] = counter[i+1]
            counter[8] = reproducers
            counter[6] += reproducers
        return sum(counter)

    print(f'Problem 1 Solution With A More Efficient Function: \n {getFishCountEfficiently(input, 80)}')
    print(f'Problem 2 Solution With A More Efficient Function: \n {getFishCountEfficiently(input, 256)}')

if __name__ == "__main__":
    main('Day6\day6_input.txt')


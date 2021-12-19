import numpy as np

def main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return f.read().strip().split(',')

    def MoveTheCrabs1(input: list):
        listOfCrabs = np.sort(np.array([int(x) for x in readfile(input)]))
        fuelSpent = []
        for i in range(np.max(listOfCrabs)):
            diff = 0
            for crab in listOfCrabs:
                diff += np.abs(i - crab)
            fuelSpent.append(diff)
        return np.min(fuelSpent)
    
    def MoveTheCrabs2(input: list):  
        listOfCrabs = np.sort(np.array([int(x) for x in readfile(input)]))
        fuelSpent = []
        for i in range(np.max(listOfCrabs)):
            diff = []
            for crab in listOfCrabs:
                n = np.abs(i - crab)
                diff.append(n * (n +1 ) // 2) # Formula for triangular numbers
            fuelSpent.append(sum(diff))
        return np.min(fuelSpent)
    
    print(f'Problem 1 Solution : \n {MoveTheCrabs1(input)}')
    print(f'Problem 2 Solution : \n {MoveTheCrabs2(input)}')

if __name__ == "__main__":
    main('Day7\day7_input.txt')
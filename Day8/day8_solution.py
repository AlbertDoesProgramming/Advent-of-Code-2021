import numpy as np

def main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return f.read().strip().split(',')

    def MoveTheCrabs1(input: list):
        list = np.sort(np.array([int(x) for x in readfile(input)]))
        
    
    # print(f'Problem 1 Solution : \n {func(input)}')
    # print(f'Problem 2 Solution : \n {func(input)}')

if __name__ == "__main__":
    main('Day7\day7_input.txt')
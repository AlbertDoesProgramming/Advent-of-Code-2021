from os import read


def main(input1):
    
    def readfile(textfile):
        f = open(file=f"{textfile}", mode="r")
        return f.read().split("\n")
    
    def getPosition(input1):
        directions = readfile(input1)
        return directions

if __name__ == "__main__":
    main('Day2\day2_input2.txt')

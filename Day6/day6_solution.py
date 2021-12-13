def main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return f.read().strip().split('\n')

    
if __name__ == "__main__":
    main('Day5\day5_input.txt')
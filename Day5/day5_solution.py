from collections import Counter

def main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return f.read().strip().split('\n')

    def getDangerZones(input):
        lines = readfile(input)
        part1 = []
        part2 = []
        for line in lines:
            x1, y1 = tuple([int(x) for x in line.split(' -> ')[0].split(',')])
            x2, y2 = tuple([int(x) for x in line.split(' -> ')[1].split(',')])
            (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])
            if x1 == x2 or y1 == y2:
                part1 += [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
            elif y1 < y2:
                part2 += [(x, y1 + index) for index, x in enumerate(range(x1, x2 + 1))]
            else:
                part2 += [(x, y1 - index) for index, x in enumerate(range(x1, x2 + 1))]
        
        solution1 = sum(x > 1 for x in Counter(part1).values())
        solution2 = sum(x > 1 for x in (Counter(part1) + Counter(part2)).values())
        return f"The solution for problem 1 is: {solution1}\nThe solution for problem 2 is: {solution2}"

    print(getDangerZones(input))

if __name__ == "__main__":
    main('Day5\day5_input.txt')
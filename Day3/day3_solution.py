def main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return [line.replace('\n','') for line in f]
    
    def convertNum(list, base = 10):
        number = int("".join(map(str, list)), base)
        return number
    
    def getPowerRating(input):
        lines = readfile(input)
        epsilon = []
        gamma = []
        for i in range(len(lines[0])):
            sum = 0
            for num in range(len(lines)):
                if int(lines[num][i]) > 0:
                    sum += 1
            if sum > len(lines)//2:
                epsilon.append(1)
                gamma.append(0)
            else:
                epsilon.append(0)
                gamma.append(1)                    
        return convertNum(epsilon)*convertNum(gamma)
    
    def getO2Rating(input):
        lines = readfile(input)
        init_len = len(lines[0])
        o2_list = []
        for i in range(init_len):
            mcv = 0
            if len(lines) == 1:
                break
            sum = 0
            for num in range(len(lines)):
                if int(lines[num][i]) > 0:
                    sum += 1
            if sum >= len(lines)/2:
                mcv = 1
            lines = [x for x in lines if int(x[i]) == int(mcv)]
        return lines

    def getCO2Rating(input):
        lines = readfile(input)
        init_len = len(lines[0])
        for i in range(init_len):
            lcv = 1
            if len(lines) == 1:
                break
            sum = 0
            for num in range(len(lines)):
                if int(lines[num][i]) > 0:
                    sum += 1
            if sum >= len(lines)/2:
                lcv = 0
            lines = [x for x in lines if int(x[i]) == int(lcv)]           
        return lines


    print(f"Problem 1 answer is: {getPowerRating(input)}")
    print(f"Problem 2 answer is: {convertNum(getO2Rating(input),2)*convertNum(getCO2Rating(input),2)}")

if __name__ == "__main__":
    main('Day3\day3_input.csv')

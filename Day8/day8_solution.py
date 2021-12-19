from collections import Counter

def main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return f.read().split('\n')

    def getLetters(input: list):
        counts = Counter()
        lists = [x.split(' | ')[1] for x in readfile(input)]
        lists = [[len(y) for y in x.split(' ')] for x in lists]
        for letters in lists:
            count = Counter(letters)
            counts.update(count)
        return sum([y for x,y in counts.items() if x in (2, 3, 4, 7)])
    
    print(f'Problem 1 Solution : \n{getLetters(input)}')
    
    def deCodeLetters(input: list):
        one = two = three = four = five = six = seven = eight = nine = zero = ''
        inputList = [x.split(' | ')[0] for x in readfile(input)]
        outputList = [x.split(' | ')[1] for x in readfile(input)]
        codeDict = dict(zip(inputList, outputList))
        outputNums = []
        for inputs, outputs in codeDict.items():
            input = inputs.split(' ')
            output = outputs.split(' ')
            fiveLens = []
            sixLens = []
            for n in range(len(input)):
                string = input[n]
                string = ''.join(sorted(string))
                if len(string) == 2:                                          
                    one = list(string)                                
                if len(string) == 3:                                          
                    seven = list(string)                                      
                if len(string) == 4:                                          
                    four = list(string)                                       
                if len(string) == 7:                                          
                    eight = list(string)                                      
                if len(string) == 5:                                          
                    fiveLens.append(list(string))                             
                if len(string) == 6:                                          
                    sixLens.append(list(string))                              
            
            # Mapping out rules and lines from the above
            topLine = [x for x in seven if x not in one][0]                                     
            bottomChars = [[y for y in x if y not in four and y not in topLine] for x in sixLens]
            bottomLine = [x for x in bottomChars if len(x) == 1][0][0]
            bottomLeftLine = [[y for y in x if y != bottomLine ] for x in bottomChars if len(x) == 2][0][0]
            nine = [x for x in sixLens if bottomLeftLine not in x][0]
            middleLineChars = [[y for y in x if y not in one] for x in sixLens if bottomLeftLine in x]
            middleLine = list(set(middleLineChars[0]).symmetric_difference(set(middleLineChars[1])))[0][0]
            zero = [x for x in sixLens if middleLine not in x][0] #
            six = [x for x in sixLens if middleLine in x and bottomLeftLine in x][0] #
            upperRightLine = list(set(eight).symmetric_difference(set(six)))[0][0] #
            three = sorted([middleLine, bottomLine, topLine, one[0], one[1]])
            five = [x for x in fiveLens if bottomLine in x and upperRightLine not in x][0] #
            two = [x for x in fiveLens if x != three and x != five][0]
            
            decodedNumbers = [''.join(sorted(x)) for x in [zero, one, two, three, four, five, six, seven, eight, nine]]            
            outputPreSum = []

            for x in range(len(output)):
                string = output[x]
                string = "".join(sorted(string))
                index = decodedNumbers.index(string)
                outputPreSum.append(index)
            outputNums.append(outputPreSum)
        sum1 = [int("".join(str(x)).replace(', ','').replace('[','').replace(']','')) for x in outputNums]
        return sum(sum1)
        
    print(f'Problem 2 Solution : \n{deCodeLetters(input)}')

if __name__ == "__main__":
    main('Day8\day8_input.txt')
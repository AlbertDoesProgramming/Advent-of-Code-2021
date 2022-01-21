import numpy as np
import logging as log

def main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return f.read()    

    def checkBracket(symbol):
        brackets = {'(' : ')', '{' : '}', '[' : ']', '<' : '>'}
        for opener, closer in brackets.items():
            try:
                if symbol == closer:
                    return opener
            except:
                return log.error('Invalid Char')
    
    def getFirstErrors(input):
        firstError = []
        incomplete = []
        brackets = {'(' : ')', '{' : '}', '[' : ']', '<' : '>'}
        lines = readfile(input).split('\n')
        for code in lines:
            stack = []
            for char in code:
                if char in brackets.keys():
                    stack.append(char)                 
                elif char in brackets.values():
                    if stack[-1] == checkBracket(char):
                        stack = stack[:-1]
                    else:
                        firstError.append(char)        
                        break
            else:
                incomplete.append(code)
        return firstError, incomplete
    
    def getScore1(scoreList):
        score = 0
        for symbol in scoreList:
            if symbol == ')':
                score += 3
            elif symbol == ']':
                score += 57
            elif symbol == '}':
                score += 1197
            elif symbol == '>': 
                score += 25137
        return score
    part1, incomplete = getFirstErrors(input)
    print(f"Part 1 Solution : {getScore1(part1)}")
    
    def getScore2(symbol):
        tempScore = 0
        if symbol == '(':
            tempScore += 1
        elif symbol == '[':
            tempScore += 2
        elif symbol == '{':
            tempScore += 3
        elif symbol == '<': 
            tempScore += 4
        return tempScore
    
    def getIncompleteBrackets(lines):
        brackets = {'(' : ')', '{' : '}', '[' : ']', '<' : '>'}
        scoreArray = []
        for code in lines:
            stack = []
            lineScore = 0
            for char in code:
                if char in brackets.keys():
                    stack.append(char)                 
                elif char in brackets.values():
                    if stack[-1] == checkBracket(char):
                        stack = stack[:-1]
            
            while len(stack) > 0:
                endBracket = stack[-1]
                lineScore *= 5, 
                lineScore += getScore2(endBracket)
                stack = stack[:-1]
            
            scoreArray.append(lineScore)
        return scoreArray

    part2 = getIncompleteBrackets(incomplete)
    print(f"Part 2 Solution : {int(np.median(np.array(part2)))}")
    
if __name__ == "__main__":
    main('Day10\day10_input.txt')
    
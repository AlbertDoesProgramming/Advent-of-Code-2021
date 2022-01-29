from collections import defaultdict
import numpy as np
from functools import cache

class Location():
    
    def __init__(self, current, neighbours):
        self.current = current
        self.neighbours = neighbours
        self.start = False
        self.end = False
        
        if 'start' in self.current:
            self.start = True
            
        if 'end' in self.current:
            self.end = True
    
    def traverse(self):
        return

def main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return f.read().split('\n')
    
    def getAllMembers(someList):
        finalList = []
        for i in someList:
            key = i[0]
            tempList = []
            tempList2 = []
            tempList.append(i[0])
            for x in someList:
                if x[0] == key:
                    tempList2.append(x[1])
                if x[1] == key:
                    tempList2.append(x[0])
            tempList.append(tempList2)
            finalList.append(tempList)
        return finalList
                
    def myFunct(input):
        f = [x.split('-') for x in readfile(input)]
        locationDict = {}
        locations = {}
        locationList = getAllMembers(f)
        for item in locationList:
            locationDict[item[0]] = item[1]
        for index, item in enumerate(locationDict.items()):
            locations[f"loc_{index}"] = Location(item[0], item[1])

        return locations
        
    # The next step is to loop through the locations recursively
    # find the next location, add this to a list or a set
    # then we need to check this list next time we run through to make sure we haven't went the same way
        
    part1 = myFunct(input)
    
    print(part1['loc_1'].neighbours)
    print(f"Part 1 answer is:  {part1}")
    
if __name__ == "__main__":
    main('Day12\day12_input.txt')
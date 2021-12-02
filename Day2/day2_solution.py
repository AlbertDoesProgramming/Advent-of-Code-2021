def main(input1):
    
    def readfile(textfile):
        f = open(file=f"{textfile}", mode="r")
        return f.read().split("\n")
    
    def getPosition(input1):
        directions = [x.split(' ') for x in readfile(input1)] 
        x = 0
        y = 0
        for i in directions:
            direction = i[0]
            distance = int(i[1])
            if direction == 'forward':
                x += distance
            elif direction == 'back':
                x -= distance
            elif direction == 'up':
                y -= distance
            elif direction == 'down':
                y += distance
        return x*y
    
    def getPositionWithAim(input1):
        directions = [x.split(' ') for x in readfile(input1)] 
        x = 0
        y = 0
        aim = 0
        for i in directions:
            direction = i[0]
            command = int(i[1])
            if direction == 'forward':
                x += command
                y += (command*aim)
            elif direction == 'up':
               aim -= command
            elif direction == 'down':
                aim += command
        return x*y

    print(f"Problem 1 answer is: {getPosition(input1)}")
    print(f"Problem 1 answer is: {getPositionWithAim(input1)}")

if __name__ == "__main__":
    main('Day2\day2_input2.txt')

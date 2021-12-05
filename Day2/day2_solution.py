def main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return [line.replace('\n','') for line in f]
    
    def getPosition(input):
        directions = [x.split(' ') for x in readfile(input)] 
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
    
    def getPositionWithAim(input):
        directions = [x.split(' ') for x in readfile(input)] 
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

    print(f"Problem 1 answer is: {getPosition(input)}")
    print(f"Problem 2 answer is: {getPositionWithAim(input)}")

if __name__ == "__main__":
    main('Day2\day2_input.txt')

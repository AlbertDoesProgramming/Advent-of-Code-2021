def Main(input):
    
    def readfile(textfile):
        with open(file=f"{textfile}", mode="r") as f:
            return [line.replace('\n','') for line in f]
    
    def inc_counter(lines):
        counter = 0
        for i in range(len(lines)):
            if lines[i] > lines [i-1]:
                counter += 1
        return counter

    def inc_window_counter(lines):
        nums = [lines[i:i+3] for i in range(len(lines))]
        sum_windows = [sum([int(y) for y in x]) for x in nums if len(x) == 3 and "" not in x]
        return inc_counter(sum_windows)

    print(f"task 1 answer = {inc_counter(readfile(input))}")
    print(f"task 2 answer = {inc_window_counter(readfile(input))}")

if __name__ == "__main__":
    Main("Day1\day1_input.txt")

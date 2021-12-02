def Main(input1, input2):
    
    def readfile(textfile):
        f = open(file=f"{textfile}", mode="r")
        return f.read().split("\n")
    
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

    print(f"task 1 answer = {inc_counter(readfile(input1))}")
    print(f"task 2 answer = {inc_window_counter(readfile(input2))}")

if __name__ == "__main__":
    Main("day1_input.txt", "day1_input2.txt")

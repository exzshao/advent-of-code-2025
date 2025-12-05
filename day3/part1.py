
def solve(battery):
    # find the biggest
    biggest = -1
    second = -1
    for i, c in enumerate(battery):
        if i == len(battery)-1 and int(c) > second:
            second = int(c)
            break
        if int(c) > biggest:
            biggest = int(c)
            second = -1
        elif int(c) > second:
            second = int(c)            

    return biggest*10 + second


if __name__ == "__main__":
    lines = []
    with open("day3/input.txt") as f:
        lines = [line.strip() for line in f]

    res = 0
    for line in lines:
        res += solve(line)

    print(res)
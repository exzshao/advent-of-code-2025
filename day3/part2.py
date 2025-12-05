def solve(battery):  
    # find largest number before the 12th last digit
    # find largest before the 11th last digit
    stk = []
    n = len(battery)
    for i in range(n):
        while stk and battery[i] > stk[-1] and n-i > 12-len(stk):
            stk.pop()

        stk.append(battery[i])

    res = "".join(c for c in stk[:12])
    print(res)
    return int(res)


if __name__ == "__main__":
    lines = []
    with open("day3/input.txt") as f:
        lines = [line.strip() for line in f]

    res = 0
    for line in lines:
        res += solve(line)

    print(res)
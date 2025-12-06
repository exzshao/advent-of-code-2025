
if __name__ == "__main__":
    lines = []
    with open("day6/input.txt") as f:
        lines = [line.strip().split() for line in f if line.strip()]

    n = len(lines)
    m = len(lines[0])
    print(n, m)

    total = 0
    for i in range(m):
        sum_total = 0
        mult_total = 1
        op = lines[n-1][i]
        for line in lines[:n-1]:
            if op == '+':
                sum_total += int(line[i])
            elif op == '*':
                mult_total *= int(line[i])
        
        total = total + sum_total if op == '+' else total + mult_total

    print(total)
        

def solve(start, instruction):
    magnitude = int(instruction[1:])
    if instruction[0] == 'L':
        start  = (start - magnitude)%100
    else: # R
        start = (start + magnitude)%100
    return start

if __name__ == "__main__":

    input_lines = []
    with open('day1/input.txt') as f:
        input_lines = [line.strip() for line in f if line.strip()]

    cur = 50
    res = 0
    for input in input_lines:
        cur = solve(cur, input)
        if cur == 0:
            res += 1

    print(res)
"""
solve should take in a start, and an instruction, and return (new pos, the # of times it passes 0)
"""
def solve(start, instruction):
    magnitude = int(instruction[1:])
    remainder = magnitude % 100
    rotations = magnitude // 100

    end = -1
    if instruction[0] == 'L':
        end  = (start - remainder)%100
        if start != 0 and (end > start or end == 0):
            rotations += 1
    else: # R
        end = (start + remainder)%100
        if end < start:
            rotations += 1

    return (end, rotations)

if __name__ == "__main__":

    input_lines = []
    with open('day1/input.txt') as f:
        input_lines = [line.strip() for line in f if line.strip()]

    cur = 50
    res = 0
    for input in input_lines:
        cur, rotations = solve(cur, input)
        res += rotations
        print(f"cur: {cur}, res: {res}")

    print(res)
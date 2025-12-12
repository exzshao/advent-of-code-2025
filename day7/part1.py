# updates lines[i]
# returns how many splits on level i
def solve(i, lines):
    if i == 0:
        return 0
    res = 0
    for j in range(len(lines[i])):
        above = lines[i-1][j]
        if lines[i][j] == '^' and above == '|':
            # check the immediate above for a line
            res += 1
            lines[i][j-1] = '|'
            lines[i][j+1] = '|'
        elif above == '|' or above == 'S':
            lines[i][j] = '|'
    return res

if __name__ == "__main__":
    lines = []
    with open('day7/input.txt') as f:
        lines = [list(line) for line in f]    
    res = 0
    for i, line in enumerate(lines):
        res += solve(i, lines)
    
    print(res)
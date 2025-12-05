def solve(grid):
    res = 0
    n = len(grid)
    m = len(grid[0])

    def find_num_neighbors(r, c):
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        paper_neighbors = 0
        for d in dirs:
            nr, nc = r + d[0], c + d[1]
            if nr in range(n) and nc in range(m) and grid[nr][nc] == '@':
                paper_neighbors += 1
        return paper_neighbors

    for r in range(n):
        for c in range(m):
            if grid[r][c] == '@':
                if find_num_neighbors(r, c) < 4:
                    grid[r][c] = '.'
                    res += 1
    return res


if __name__ == "__main__":
    grid = []
    with open('day4/input.txt') as f:
        grid = [line.rstrip('\n') for line in f]
    
    grid = [list(i) for i in grid]
    total = 0
    res = -1
    while res != 0:
        res = solve(grid)
        total += res

    print(total)



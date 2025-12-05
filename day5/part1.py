
def solve(ranges, ids):
    res = 0
    for id in ids:
        for ra in ranges:
            start, end = ra[0], ra[1]
            if id in range(start, end+1):
                res += 1
                break
    return res


if __name__ == "__main__":
    with open("day5/input.txt") as f:
        lines = [line.strip() for line in f if line.strip()]

    ranges = []
    ids = []
    for line in lines:
        if "-" in line:
            start, end = line.split("-")
            ranges.append([int(start), int(end)])
        else:
            ids.append(int(line))
    
    print(solve(ranges, ids))


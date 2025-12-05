
def solve(ranges):
    ranges.sort(key = lambda x: x[0])
    merged_ranges = []
    merged_ranges.append(ranges[0])

    for i in range(1, len(ranges)):
        start, end = ranges[i][0], ranges[i][1]
        cur_end = merged_ranges[-1][1]

        if start <= cur_end:
            merged_ranges[-1][1] = max(end, cur_end)
        else:
            merged_ranges.append([start, end])

    res = 0
    for ra in merged_ranges:
        start, end = ra[0], ra[1]
        res += end - start + 1
    print(res)

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
    
    # print(solve(ranges))
    solve(ranges)


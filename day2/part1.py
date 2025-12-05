
def sum_interval(interval):
    lower = interval[0]
    upper = interval[1]

    res = 0
    for num in range(lower, upper+1):
        n = len(str(num)) # length of digits
        if n % 2 == 1:
            continue
        first_half = str(num)[:n//2]
        second_half = str(num)[n//2:]
        if first_half == second_half:
            res += num
    return res


if __name__ == "__main__":
    intervals = []
    with open('day2/input.txt') as f:
        line = f.read().strip()
        # Split by comma to get the intervals as strings
        interval_strings = line.split(',')
        for s in interval_strings:
            parts = s.split('-')
            # Convert both bounds to integers
            start = int(parts[0])
            end = int(parts[1])
            intervals.append((start, end))

    res = 0
    for interval in intervals:
        res += sum_interval(interval)

    print(res)
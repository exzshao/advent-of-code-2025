
def solve(i, j, lines): # enforce that i is the index of an operator, j is the index of the longest char
    print(f"solving equation from columns {i} - {j}")
    # first number is lines[3][j], lines[2][j], lines[1][j], lines[0][j] # row, col somehow start from 
    op = lines[-1][i]
    nums = []
    for a in range(i, j+1):
        num = ""
        for b in range(len(lines)-1):
            num += str(lines[b][a])
        nums.append(int(num))

    if op == '+':
        return sum(nums)
    else:
        res = 1
        for num in nums:
            res *= num
        return res


if __name__ == "__main__":
    lines = []
    with open("day6/test.txt") as f:
        lines = [line for line in f]

    cur = 0 # cur op idx
    res = 0

    for i, c in enumerate(lines[-1]):
        if i == len(lines[-1])-1:
            ans = solve(cur, i, lines)
            res += ans


        if i!= 0 and c == '*' or c == '+':
            ans = solve(cur, i-2, lines)
            res += ans
            cur = i

    print(res)
# s fix, o any, a left, r right
n = int(input())
blocks = []
for i in range(n):
    blocks.append(input())


def cal(blocks):
    counts = 1
    ind = 0
    pos_count = [0] * 8
    pos_count[0] = 1
    while ind < n:
        if blocks[ind] == 'a':
            count = 0
            for i in range(7, -1, -1):
                count += pos_count[i]
                pos_count[i] = count
        elif blocks[ind] == 'r':
            for i in range(7, 0, -1):
                pos_count[i] = pos_count[i - 1]
            pos_count[0] = 0
        elif blocks[ind] == 'o':
            for i in range(7, 0, -1):
                pos_count[i] = pos_count[i - 1] * i
            pos_count[0] = 0
        else:
            counts *= sum(pos_count)
            if counts > 10 ** 9:
                counts = counts % (10 ** 9 + 7)
            pos_count = [0] * 8
            pos_count[0] = 1
        ind += 1
    counts *= sum(pos_count)
    if counts > 10 ** 9:
        counts = counts % (10 ** 9 + 7)
    return counts


print(cal(blocks))

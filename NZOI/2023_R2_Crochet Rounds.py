n = int(input())
left = 0
right = 6
row = 0

for i in range(n):
    info = input()
    inst = info[0]
    x = int(info[1])
    if right == 0:
        right = left
        left = 0
        row += 1
    if inst == 'I':
        right -= 1
        left += x
    else:
        if right >= x:
            right -= x
            left += 1
        else:
            x -= right
            right = left
            right -= x
            left = 1
            row += 1
print(left + right)
print(row + 1)

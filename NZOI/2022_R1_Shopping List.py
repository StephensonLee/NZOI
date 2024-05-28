n = int(input())

cost = 0
for i in range(n):
    w, a, x, b, y = map(int, input().split())
    if x <= y:
        if w <= a:
            cost += w * x
        else:
            cost += a * x + (w - a) * y
    else:
        if w <= b:
            cost += w * y
        else:
            cost += b * y + (w - b) * x

print(cost)

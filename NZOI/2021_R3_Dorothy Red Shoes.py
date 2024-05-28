n = int(input())
a = int(input())
b = int(input())
cost = 0
if a / 2 > b / 3:
    if n % 3 == 0:
        cost = n // 3 * b
    elif n % 3 == 1:
        cost = (n - 4) // 3 * b + 2 * a
    else:
        cost = (n - 2) // 3 * b + a
else:
    if n % 2 == 0:
        cost = n // 2 * a
    else:
        cost = (n - 3) // 2 * a + b
print(cost)

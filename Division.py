def solve(n):
    count = 0
    for b in range(1234, 98765 // n + 1):
        a = b * n
        if check(a, b) == 10:
            print(a, '/', b, '=', n)
            count += 1
        elif check(a, b) == 9:
            print(a, '/', '0' + str(b), '=', n)
            count += 1
    if count == 0:
        print('There are no solutions for ' + str(n) + '.')


def check(a, b):
    digits = set()
    while a > 0:
        digits.add(a % 10)
        a = a // 10
    while b > 0:
        digits.add(b % 10)
        b = b // 10
    if len(digits) == 10 or (len(digits) == 9 and 0 not in digits):
        return len(digits)
    else:
        return 0


n = int(input())
while n != 0:
    solve(n)
    n = int(input())

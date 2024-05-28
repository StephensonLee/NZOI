N = int(input())
hurts = list(map(int, input().split()))
add, mul, eql = map(int, input().split())


# print(N)
# print(hurts)
# print(add, mul, eql)


def find_num(n):
    nums = str(n)
    ans = 0
    for c in nums:
        ans += hurts[int(c)]
    return ans


def find_mul(n):
    mini = find_num(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a = find_num(i)
            b = find_num(n // i)
            mini = min(mini, a + b + mul)
    return mini


def find_add_mul(n):
    mini = find_mul(n)
    for i in range(1, n):
        a = find_mul(i)
        b = find_num(n - i)
        mini = min(mini, a + b + add)
    return mini


print(find_add_mul(N) + eql)

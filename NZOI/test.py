apple = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
rest = sum(apple)
capacity.sort(reverse=True)
i = 0
while rest > 0 and i < len(capacity):
    if rest > capacity[i]:
        rest -= capacity[i]
    else:
        rest = 0
    i += 1
print(i)

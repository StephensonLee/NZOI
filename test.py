count = 0
for i in range(1, 100):
    for j in range(1, 100):
        k = 100 - i - j
        if i < j < k:
            count += 1

print(count)

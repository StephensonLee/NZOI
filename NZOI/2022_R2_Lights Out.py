n = int(input())
m = int(input())

lights = [False] * n
for step in range(1, m + 1):
    for i in range(step - 1, n, step):
        lights[i] = not lights[i]
print(lights.count(True))

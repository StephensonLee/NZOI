n = int(input())
skills = list(map(int, input().split()))
skills.sort()
pairs = []
for i in range(n // 2):
    pairs.append(skills[i] + skills[-1 - i])
pairs.sort()
print(pairs[-1] - pairs[0])

n, m, a, b = map(int, input().split())

namea = input().split()
vas = []
for i in range(a):
    vas.append(input().split())

nameb = input().split()
vbs = []
for i in range(b):
    vbs.append(input().split())

commonas = [''] * a
commonbs = [''] * b
for ida in range(len(namea)):
    if namea[ida] in nameb:
        idb = nameb.index(namea[ida])
        for i in range(a):
            commonas[i] += vas[i][ida] + ' '
        for i in range(b):
            commonbs[i] += vbs[i][idb] + ' '

common_mapb = set(commonbs)
besta = a - 1
while commonas[besta] not in common_mapb:
    besta -= 1
bestb = b - 1
while commonbs[bestb] != commonas[besta]:
    bestb -= 1

print(besta, bestb)

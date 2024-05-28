import random

n, c = 10, 10
buys = []
sells = []
for i in range(n):
    buys.append(5)
    sells.append(random.randint(1, 10))

allin = [(0, c)]
allout = [c]

for i in range(n):
    # all in
    allin_s, allin_m = allin[-1]

    # all out
    allout_m = allout[-1]

    # sell out
    allin_out_m = allin_s * sells[i] + allin_m
    if allin_out_m >= allout_m:
        allout.append(allin_out_m)
    else:
        allout.append(allout_m)

    # buy in
    allout_m = allout[-1]
    allout_in_s = allout_m // buys[i]
    allout_in_m = allout_m % buys[i]

    if allout_in_s * buys[i] + allout_in_m >= allin_s * buys[i] + allin_m:
        allin.append((allout_in_s, allout_in_m))
    else:
        allin.append((allin_s, allin_m))

print(allout[-1])

money = c
for buy, sell in zip(buys, sells[1:]):
    if buy < sell:
        money += money // buy * (sell - buy)
print(money)

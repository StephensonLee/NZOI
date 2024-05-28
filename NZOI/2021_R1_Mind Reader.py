number = input()
suit = input()

order_n = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
order_s = ['spades', 'clubs', 'diamonds', 'hearts']

rank = 13 * 4 - 1
for i in range(len(order_s)):
    if order_s[i] != suit:
        rank -= 13
    else:
        break

for i in range(len(order_n)):
    if order_n[i] != number:
        rank -= 1
    else:
        break

print(rank)

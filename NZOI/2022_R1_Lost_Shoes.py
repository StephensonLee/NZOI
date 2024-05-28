s = input()
shoe = ''
colors = {'G': 'Green', 'B': 'Black', 'R': 'Red', 'Bl': 'Blue', 'Br': 'Brown', 'M': 'Mustard'}
shoes = {'G': 0, 'B': 0, 'R': 0, 'Bl': 0, 'Br': 0, 'M': 0}

for c in s:
    if c.isupper():
        if shoe in shoes:
            shoes[shoe] += 1
        shoe = c
    else:
        shoe += c

if shoe in shoes:
    shoes[shoe] += 1

paired = True
for c, n in shoes.items():
    if n % 2:
        paired = False
        print('A {} shoe has no partner.'.format(colors[c]))
if paired:
    print('All paired up!')

shoes = list(input())
red = shoes.count('R')
if red == 0:
    print('Maybe Dorothy is in Kansas.')
elif red == 1:
    print('Hop along Dorothy and find that other shoe.')
else:
    print('Dorothy is in the classroom.')

socks = {}
for i in range(7):
    sock = input()
    if sock in socks:
        socks[sock] = not socks[sock]
    else:
        socks[sock] = True

for k, v in socks.items():
    if v:
        print(k)

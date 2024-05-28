ns = int(input())
nm = int(input())
nl = int(input())

m = max([ns, nm, nl])

rl = m - nl
rll = rl // 2
rlr = rl - rll
print('_' * rll + 'L' * nl + '_' * rlr)

rm = m - nm
rml = rm // 2
rmr = rm - rml
print('_' * rml + 'M' * nm + '_' * rmr)

rs = m - ns
rsl = rs // 2
rsr = rs - rsl
print('_' * rsl + 'S' * ns + '_' * rsr)

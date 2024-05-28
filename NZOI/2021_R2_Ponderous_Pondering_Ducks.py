h, w = map(int, input().split())
n = int(input())
routes = []

for i in range(n):
    info = list(map(int, input().split()))
    routes.append(info)


def bisearch(nums, k):
    lower = 0
    upper = len(nums) - 1
    mid = (lower + upper) // 2
    while lower <= upper:
        mid = (lower + upper) // 2
        if nums[mid] < k:
            lower = mid + 1
        elif nums[mid] > k:
            upper = mid - 1
        else:
            return mid
    if nums[mid] > k:
        return mid
    else:
        return mid + 1


rowmap = {}
colmap = {}
for route in routes:
    m = route[0]
    smooth = True
    r = 0
    c = 0
    i = 0
    while i < m:
        up = route[i * 2 + 1]
        right = route[i * 2 + 2]
        if c in colmap:
            idr = bisearch(colmap[c], r)
            idr_next = bisearch(colmap[c], r + up)
            if idr_next != idr:
                smooth = False
        r = r + up
        if r in rowmap:
            idc = bisearch(rowmap[r], c)
            idc_next = bisearch(rowmap[r], c + right)
            if idc_next != idc:
                smooth = False
        c = c + right
        i += 1

    if r in rowmap:
        idc = bisearch(rowmap[r], c)
        if idc >= len(rowmap[r]):
            rowmap[r].append(c)
        elif rowmap[r][idc] == c:
            smooth = False
        else:
            rowmap[r].insert(idc, c)
    else:
        rowmap[r] = [c]

    if c in colmap:
        idr = bisearch(colmap[c], r)
        if idr >= len(colmap[c]):
            colmap[c].append(r)
        elif colmap[c][idr] == r:
            smooth = False
        else:
            colmap[c].insert(idr, r)
    else:
        colmap[c] = [r]

    if smooth:
        print('smooth swimming')
    else:
        print('OUCH')

import random

for i in range(100):
    n = random.randint(5, 20)
    routes = []
    for i in range(n):
        m = random.randint(1, 5)
        route = [m]
        for j in range(m):
            up = random.randint(0, 5)
            right = random.randint(0, 5)
            route.append(up)
            route.append(right)
        routes.append(route)


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


    sol = []
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

            if smooth and c in colmap:
                idr = bisearch(colmap[c], r)
                idr_next = bisearch(colmap[c], r + up)
                if idr_next != idr:
                    smooth = False
            r = r + up
            if smooth and r in rowmap:
                idc = bisearch(rowmap[r], c)
                idc_next = bisearch(rowmap[r], c + right)
                if idc_next != idc:
                    smooth = False
            c = c + right
            i += 1

        # print(r,c)
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
            sol.append('smooth swimming')
        else:
            sol.append('OUCH')
        # print(rowmap)
        # print(colmap)

    pond = [[False] * 1000 for i in range(1000)]
    ans = []

    for route in routes:
        r = 0
        c = 0
        m = route[0]

        flag = False
        if pond[r][c] == True:
            flag = True
        for mi in range(m):
            up = route[mi * 2 + 1]
            right = route[mi * 2 + 2]
            for i in range(up):
                r += 1
                if not flag and pond[r][c] == True:
                    flag = True

            for i in range(right):
                c += 1
                if not flag and pond[r][c] == True:
                    flag = True

        if flag:
            ans.append('OUCH')
        else:
            ans.append('smooth swimming')
        pond[r][c] = True

    if sol != ans:
        print(n)
        print(routes)
        print(sol)
        print(ans)

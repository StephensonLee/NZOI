def combinationSum(candidates, target):
    ans = []

    def bfs(cur, nums, target):
        if target == 0:
            ans.append(cur.copy())
        for i in range(len(nums)):
            if nums[i] <= target and (not cur or nums[i] >= cur[-1]):
                cur.append(nums[i])
                bfs(cur, nums, target - nums[i])
                cur.pop()

    bfs([], candidates, target)
    print(ans)
    return ans


candidates = [2, 3, 5]
target = 8
combinationSum(candidates, target)

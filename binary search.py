def bisearch_r(nums, k):
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

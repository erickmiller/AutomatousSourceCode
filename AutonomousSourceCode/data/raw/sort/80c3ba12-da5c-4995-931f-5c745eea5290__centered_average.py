def centered_average(nums):
    sort_nums = sorted(nums)
    length = len(nums)
    if length % 2 == 0:
        return (sort_nums[length / 2 -1] + sort_nums[length / 2]) / 2
    else:
        return sort_nums[length / 2]

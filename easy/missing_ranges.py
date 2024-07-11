# this was a leetcode premium so i found it online lol
def missing_ranges(nums, lower, upper):
    res = []
    if lower < nums[0]:
        result.append(format_range(lower, nums[0] - 1))
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] > 1:  #gap bigger than 1
            result.append(format_range(nums[i] + 1, nums[i + 1] - 1))
    if nums[-1] < upper:
        result.append(format_range(nums[-1] + 1, upper))
    return result
def format_range(start, end):
    if start == end:
        return str(start)
    else:
        return f"{start}->{end}"  # Use f-string for formatting

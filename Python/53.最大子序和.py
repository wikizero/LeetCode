# 53.最大子序和问题
"""
for i in range(1, len(nums)):
    if nums[i - 1] > 0:
        nums[i] += nums[i - 1]
    return max(nums)

"""


def maxSubArray(nums):
    max_so_far = curr_so_far = nums[0]
    for i in nums:
        curr_so_far += i

        curr_so_far = max(curr_so_far, i)

        max_so_far = max(max_so_far, curr_so_far)

    return max_so_far


lst = [3, -2, 5, 4, 2, -3, 5, -6, 3]

print(maxSubArray(lst))
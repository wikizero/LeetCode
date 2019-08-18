from itertools import groupby


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = [0]
        for k, v in groupby(nums):
            if k == 1:
                lst.append(len(list(v)))

        return max(lst)

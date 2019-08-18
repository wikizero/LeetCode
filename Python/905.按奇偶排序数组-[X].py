"""
知识点： 奇数&1 =1  偶数&1=0  性能比 x % 2 好
"""


class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(A, key=lambda x: x & 1)

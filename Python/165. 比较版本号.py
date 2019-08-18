"""
比较两个版本号 version1 和 version2。
如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compare-version-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
version1 = "7.5.003"
version2 = "7.5.3"

from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        f = lambda x: map(int, x.split('.'))
        for v1, v2 in zip_longest(f(version1), f(version2), fillvalue=0):
            if v1 != v2:
                return 1 if v1 > v2 else -1
        return 0

# 妙用zip_longest解决问题

# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and (n + self.Sum_Solution(n - 1))
a=Solution()
print(a.Sum_Solution(3))
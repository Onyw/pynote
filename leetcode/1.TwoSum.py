class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = dict()
        for i, x in enumerate(nums):
            if target-x in hash_map:
                return [i, hash_map[target - x]]
            hash_map[x] = i

if __name__ == '__main__':
    a = Solution()
    result = a.twoSum([2,7,8,9,11], 9)
    print(result)
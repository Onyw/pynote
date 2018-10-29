

# class Solution:
# #     def twoSum(self, nums, target):
# #         """
# #         :type nums: List[int]
# #         :type target: int
# #         :rtype: List[int]
# #         """
# #         List = []
# #         valuelist = []
# #         for i in range(0,len(nums)-1):
# #                 for j in range(i+1,len(nums)):
# #                     if nums[i]+nums[j] == target:
# #                         if nums[i] not in valuelist:
# #                             List.append(i)
# #                         if nums[j] not in valuelist:
# #                             List.append(j)
# #                         valuelist.append(nums[i])
# #                         valuelist.append(nums[j])
# #         return List
# # def main():
# #     rList = Solution().twoSum([2, 7, 11, 15, 3, 2, 18, 6], 9)
# #     print(rList)
# # if __name__ == '__main__':
# #     main()
#两数之和 返回下标
class Solution:
    def twoSum(self, nums, target):
        # 相当于哈希表
        dic = {}
        rList = []
        valueList = []
        # 我们要求的是元素的索引，即Hash表的关键字，所以我们把数组元素作为dict的key，而把数组元素的索引作为dict的value
        for i in range(len(nums)):
            dic[nums[i]] = i
        for i in range(len(nums)):
            # 防止将同一对符合条件的值重复加入
            if i not in rList:
                # 将符合条件的两个元素成为互补元素
                # 差值是字典的key且对应互补元素的下标不是当前元素的下标
                if (target - nums[i]) in dic.keys() and dic[target - nums[i]] != i:
                    # 当前元素没有参与过之前的互补配对
                    if nums[i] not in valueList:
                        rList.append(i)
                        rList.append(dic[target - nums[i]])

                valueList.append(nums[i])
        return rList
def main():
    rList = Solution().twoSum([2, 7, 11, 15, 3, 2, 18, 6], 26)
    print(rList)
if __name__ == '__main__':
    main()
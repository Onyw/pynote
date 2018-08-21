str1 = 'hello'
nums1 = [1,2,3,4]
t1 = (123,234,345)
print(str1[0])
print(str1[-1])
print(nums1[1])
print(nums1[-2])
print(t1[2])
print(t1[-3])

nums2 = list(range(10))
print(nums2)
print(nums2[1:5])
print(nums2[6:10])
print(nums2[1:])
print(nums2[-3:-1])
print(nums2[-3:])
print(nums2[:])
print(nums2[0:10:2])
print(nums2[0:10:3])
print(nums2[0:10:-2])

str2 = 'hello'
str3 = ' world'
print(str2+str3)

nums3 = [1,2,3]
nums4 = [2,3,4]
print(nums3+nums4)
print([None]*10)
print('h'in str2)
print(1 in nums3)

print(len(nums3))
print(max(nums3))
print(min(nums3))
print(len(str2))
print(max(str2))
print(min(str2))

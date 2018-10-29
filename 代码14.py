#字符串中最长子串
class Solution:
    def lengthOfLongestSubstring(self,s):
        set2 = []
        set3 = []
        max = 0
        for i in range(len(s)):
            set1 = []
            for j in range(i,len(s)):
                if s[j] not in set1:
                    set1.append(s[j])
                else :
                    break
            set2.append(len(set1))
            if max < len(set1):
                max = len(set1)
                set3 = set1
        set2.sort(reverse = True)
        str = "".join(set3)
        return str,set2[0]
a = Solution()
print(a.lengthOfLongestSubstring('0123456789'))
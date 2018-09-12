# def count_substring(string, sub_string):
#     try:
#         string = string.replace('a',sub_string[0])
#         string = string.replace('b',sub_string[1])
#         string = string.replace('c',sub_string[2])
#         string = string.replace('d',sub_string[3])
#         string = string.replace('e',sub_string[4])
#         string = string.replace('f',sub_string[5])
#         string = string.replace('g',sub_string[6])
#         string = string.replace('h',sub_string[7])
#         string = string.replace('i',sub_string[8])
#         string = string.replace('j',sub_string[9])
#         string = string.replace('k',sub_string[10])
#         string = string.replace('l',sub_string[11])
#         string = string.replace('m',sub_string[12])
#         string = string.replace('n',sub_string[13])
#         string = string.replace('o',sub_string[14])
#         string = string.replace('p',sub_string[15])
#         string = string.replace('q',sub_string[16])
#         string = string.replace('r',sub_string[17])
#         string = string.replace('s',sub_string[18])
#         string = string.replace('t',sub_string[19])
#         string = string.replace('u',sub_string[20])
#         string = string.replace('v',sub_string[21])
#         string = string.replace('w',sub_string[22])
#         string = string.replace('x',sub_string[23])
#         string = string.replace('y',sub_string[24])
#         string = string.replace('z',sub_string[25])
#     except:
#         pass
#     # print(string)
#     count = 0
#     lenString = len(string)
#     lenSub_string = len(sub_string)
#     for i in range(0, lenString-lenSub_string+1):
#         if string[i:len(sub_string)+i] == sub_string:
#             count += 1
#     return count
#
# print(count_substring('ababcb', 'xyx'))
'''
对于仅由小写字母组成的字符串A和B，
如果分别存在一个小写字母a到z的排列，
使得将A中所有字母a替换为排列的第一个字母，所有字母b替换为排列的第二个字母……所有字母z替换为排列的最后一个字母之后，
A和B完全相同，那么称字符串A和B相似，如abcc和xyaa。
现在给定仅由小写字母组成且长度不超过105的字符串S和T，求S中有多少子串与T相似？
'''
# def  solve(S, T):
#     zistr = [S[i:i+len(T)] for i in range(0, len(S)-len(T)+1)]
#     print(zistr)
#     query = {}
#     [query.__setitem__(k, None) for k in T if k not in query.keys()]
#     ans = []
#     for ss in zistr:
#         ssx = []
#         [ssx.append(x) for x in ss if x not in ssx]
#         if len(ssx) == len(set(T)):
#             for i, k in enumerate(query.keys()):
#                 query[k] = ssx[i]
#         else:
#             continue
#         print(ssx)
#         new = ''.join([query[x] for x in T])
#         print(new)
#         ans.append(1) if ss==new else ans.append(0)
#     return sum(ans)
#
# import time
# sss = time.time()
# S = 'ababcb'
# T = 'xyx'
# x = solve(S, T)
# print(x)


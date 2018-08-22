m = input()
m_list = list(map(int, input().split()))
temp = {}
for i in m_list:
    if i in temp:
        temp[i] += 1
    else:
        temp[i] = 1
temp2 = []
for i in temp:
    if temp[i] == 1:
        temp2.append(i)
print(temp2[0])

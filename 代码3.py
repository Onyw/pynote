from collections import namedtuple
from collections import defaultdict
from collections import deque
from collections import Counter
from collections import  ChainMap
from collections import OrderedDict
#OrderedDict
#move_to_end移到最后
#pop删除
#tuple 不可变元祖
#tuple（元组） 拆包
user_tuple=('booby',29,179)
name,age,height=user_tuple
print(name,age,height)
name,*other=user_tuple
print(name,*other)
#tuple 不可变不是绝对
name_tuple=('bobby',[29,179])
name_tuple[1].append(22)
print(name_tuple)
#tuple 可哈希

#namedtuple 节省空间，拆包
User = namedtuple("user",["name","age","height",'edu'])
user = User(*user_tuple,"master")
print(user.age,user.name,user.height,user.edu)

#defaultdict
users = ["bobby1","bobby2","bobby3","bobby1","bobby2","bobby2"]
defaul_dict=defaultdict(list)

#deque GIL 是线程安全的，list不是线程安全的
user_list=["bobby1","bobby2"]
user_name=user_list.pop()
print(user_name)
user_list2=deque(['bobby1',29,198])
print(user_list2)

users_counter = Counter(users)
print(users_counter)

users1 = "abasdfbasdofijalsdfkadbnak"
users1_counter = Counter(users1)
print(users1_counter)

user_dict1 = {"a":"bobby1","b":"bobby2"}
user_dict2 = {"c":"bobby2","d":"bobby3"}

user_dict3 = ChainMap(user_dict1,user_dict2)
print(user_dict3)
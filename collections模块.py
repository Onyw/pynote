from collections import defaultdict
from collections import namedtuple
from collections import OrderedDict
from collections import Counter

d_set = defaultdict(set)
d_list = defaultdict(list)
d_set['a'].add('four')
d_set['a'].add('zero')
d_set['a'].add('one')
d_set['a'].add('two')
d_set['a'].add('three')
d_set['b'].add('one')
d_set['b'].add('two')
d_list['a'].append('four')
d_list['a'].append('one')
d_list['a'].append('one')
d_list['a'].append('two')
d_list['b'].append('one')
d_list['b'].append('four')
d_list['b'].append('one')
d_list['b'].append('one')
d_list['b'].append('two')
print(d_set)
print(d_list)

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p)

d_order = OrderedDict()
d_order['a'] = 'one'
d_order['b'] = 'two'
d_order['c'] = 'three'
d = dict([('a','one'),('b','two'),('c','three')])
print(d_order)
print(d)

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
c_C = Counter('programming')
print(c)
print(c_C)

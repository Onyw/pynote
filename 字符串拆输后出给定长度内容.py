"match是一次匹配的结果"
"Pattern对象是一个编译好的正则表达式，通过Pattern提供的一系列方法可以对文本进行匹配查找。"

"Pattern不能直接实例化，必须使用re.compile()进行构造。"
"findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags]):"
"搜索string，以列表形式返回全部能匹配的子串。"
import re
x=input("输入一段英文：")
pattern=re.compile(r'\b[a-zA-Z]{3}\b')
print(pattern.findall(x))
"import re"
"""x=input("输入一段英文：")"""
"print(re.findall(r'\b[a-zA-Z]{3}\b',x))"

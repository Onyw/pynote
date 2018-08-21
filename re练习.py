import re

match = re.search(r'[1-9]\d{4}', 'BIT 10081')
if match:
    print(match.group())

match = re.findall(r'[1-9]\d{4}','BIT10081 UUU10086')
if match:
    print(match)


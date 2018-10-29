import csv
import matplotlib.pyplot as plt
import re


def read_csv_column(path, column):
    with open(path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        return [row[column] for row in reader]


sal = read_csv_column('F:\python代码\python3.csv', 2)
salaries = []
a = []
for i in range(len(sal)):
    if not sal[i] == '面议xa0':
        salaries.append(sal[i])
for i in range(len(salaries)):
    complete = re.match('\d{4,5}', salaries[i])
    a.append(int(complete.group()))

plt.hist(a,bins=50)
plt.show()

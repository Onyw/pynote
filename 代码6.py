import os
os.chdir("F:\\大三下\\MapReduce设计模式\\网络舆情信息\\txt文件")
filenames = os.listdir("F:\\大三下\\MapReduce设计模式\\网络舆情信息\\txt文件")
f=open('result.txt','w')
for filename in filenames:

    filepath = os.path.abspath(filename)
    print("正在写入"+filepath)
    try:
        for line in open(filepath):
            f.writelines(line)
        f.write('\n')
    except  UnicodeDecodeError as e:
        f.write('error')
        f.write('\n')
f.close()
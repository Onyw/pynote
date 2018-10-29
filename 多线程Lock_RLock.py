import threading
import time
import random
class mythread(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self)
		self.name = name
	def run(self):
		global x#声明全局变量
		lock.acquire()#获取锁，进入临界区
		print('余票:%d'%(x),end=" ")
		ticket = random.randint(1,5)
		if 1==ticket :
			x-=1
			print('恭喜%s抢到了1张票'%(str(self.name)),end="\t")
		elif 2==ticket :
			x-=2
			print('恭喜%s抢到了2张票'%(str(self.name)),end="\t")
		elif 3==ticket :
			x-=3
			print('恭喜%s抢到了3张票'%(str(self.name)),end="\t")
		elif 4==ticket :
			x-=4
			print('恭喜%s抢到了4张票'%(str(self.name)),end="\t")
		else :
			x-=5
			print('恭喜%s抢到了5张票'%(str(self.name)),end="\t")
		print('还剩%s张票'%(x))
		time.sleep(1)
		lock.release()#释放锁，退出临界区
lock = threading.Lock()  #创建锁，这里也可以使用RLock
threadlist = []	#线程列表
namelist=['apple', 'pear', 'peach', 'orange', 'lemon']
for i in range(10):	#创建10个线程
	name = random.choice(namelist)
	t = mythread(name)
	threadlist.append(t)
x = random.randint(100,999)#随机生成总的票数100以上，1000以下
for i in threadlist:	#启动10个线程
	i.run()
import threading
import time
import os
import random
#定义一个类BoothThread继承自thread.Threading类
class BoothThread(threading.Thread):
	def __init__(self,tid,monitor):
		self.tid = tid
		self.monitor = monitor
		threading.Thread.__init__(self)
	def run(self):
		while True:
			monitor['lock'].acquire()#调用lock.acquire()加锁
			if monitor['tick'] != 0 :
				monitor['tick'] = monitor['tick'] - 1 #售票 售出一张减少一张
				print(self.tid,':now left',monitor['tick'])#剩下的票数
				time.sleep(2)
			else:
				print("Thread_id",self.tid," No more tickets")
				os._exit()#票售完 退出程序
				time.sleep(2)
			monitor['lock'].release()#释放锁
			time.sleep(2)
x = random.randint(100,999)
monitor = {'tick':x,'lock':threading.Lock()} #初始化票数
#总共设置了个线程
for k in range(10):
	new_thread = BoothThread(k,monitor)
	#创建线程；Python使用threading.Thread对象来代表线程类BoothThread
	new_thread.start() #调用start()方法来启动线程

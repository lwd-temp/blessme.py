import datetime
import time
count=0
while True:
    count=count+1
    bless='''
    祝LWD&ZWT考试成绩提高
    祝LWD&ZWT中考顺利
    祝LWD&ZWT中考成绩提高'''
    print("["+time.asctime(time.localtime(time.time()))+" 第"+str(count)+"次]"+bless)
    time.sleep(2)
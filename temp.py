#! /usr/bin/python
# coding = utf-8
import datetime
import time
count=0
name=input("输入姓名:")
while True:
    count=count+1
    bless='''
    祝'''+name+'''考试成绩提高
    祝'''+name+'''中考顺利
    祝'''+name+'''中考成绩提高'''
    print("["+time.asctime(time.localtime(time.time()))+" 第"+str(count)+"次]"+bless)
    time.sleep(1)
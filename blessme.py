#! /usr/bin/python
# coding = utf-8
'''blessme.py
By:LWD
重复输出文字起祝福作用
Work with Python3'''
import datetime
import time
global bless
global climit
global timeout
climit=int(5)
timeout=int(1)
bless="请输入祝福内容"
def settext(text):
    '''设置祝福文字，默认 请输入祝福内容'''
    bless=str(text)
def setcount(cl):
    global climit
    '''设置祝福次数限制(若使用 doitwithcountlimit() )，默认5次'''
    '''单位:次'''
    climit=int(cl)
def settimeout(t):
    '''设置每次祝福间隔时间，默认1s'''
    '''单位:秒'''
    timeout=int(t)
def doit():
    '''开始祝福'''
    count=0
    while True:
        count=count+1
        print("["+time.asctime(time.localtime(time.time()))+" 第"+str(count)+"次"+"]"+bless)
        time.sleep(timeout)
def doitwithcountlimit():
    '''开始祝福，带次数限制，默认5次，使用 blessme.setcount(次数) 设置'''
    count=0
    while count!=climit:
        count=count+1
        print("["+time.asctime(time.localtime(time.time()))+" 第"+str(count)
        +"次""]"+bless)
        if count==climit:
            break
        else:
            time.sleep(timeout)
if __name__ == '__main__':
    settext(input("输入祝福内容:"))
    setcount(input("设置每次祝福间隔时间 不能为0:"))
    choice=str(input("是否设置次数限制 1是 其他否:"))
    if choice==str(1):
        climit=int(input("设置次数限制:"))
        doitwithcountlimit()
    else:
        doit()
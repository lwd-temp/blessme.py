# blessme.py
作者:lwd-temp  
重复输出文字起祝福作用
## 运行平台
跨平台，Python3
## 用法
``import blessme``
或直接运行
## FUNCTIONS
    blessme.doit()
        开始祝福

    blessme.doitwithcountlimit()
        开始祝福，带次数限制，默认5次，使用 blessme.setcount(次数) 设置

    blessme.setcount(c)
        设置祝福次数限制(若使用 doitwithcountlimit() )，默认5次

    blessme.settext(text)
        设置祝福文字，默认 请输入祝福内容

    blessme.settimeout(t)
        设置每次祝福间隔时间，默认1s

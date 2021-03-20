"""
-*- coding:utf-8 -*-
 @time :2021.3.20
 @IDE : pycharm
 @autor :juzh
 @email : juzh1998@163.com

 暴力排序
 """

 #生成随机list
import random
def random_int(length,a,b):
    list=[]
    count=0
    while(count<length):
        number=random.randint(a,b)
        list.append(number)
        count=count+1
    return list


randomList=random_int(30,1,100)

print(randomList)

for i in range(1,len(randomList)):
    element_now=randomList[i]
    j=i-1
    while j>=0 and randomList[j]>element_now:
        randomList[j+1]=randomList[j]
        j=j-1
    randomList[j+1]=element_now


print(randomList)

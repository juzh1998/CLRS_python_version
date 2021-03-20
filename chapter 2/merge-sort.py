"""
-*- coding:utf-8 -*-
 @time :2021.03.20
 @IDE : pycharm
 @autor :juzh
 @email : juzh1998@163.com
 归并排序
 注意for循环截止位置
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

def merge_sort(A,low,high):
    if low<high:
        mid=int((low+high)/2)
        merge_sort(A,low,mid)
        merge_sort(A,mid+1,high)
        merge(A,low,mid,high)

def merge(A,low,mid,high):
    B=A[low:mid+1];B.append(float("inf"))

    C=A[mid+1:high+1];C.append(float("inf"))
    i=0;j=0
    for k in range(low,high+1):
        if B[i]<=C[j]:
            A[k]=B[i]
            i=i+1
        else:
            A[k]=C[j]
            j=j+1


global randomList
randomList=random_int(30,1,1000)
print(randomList)
merge_sort(randomList,0,29)
print(randomList)

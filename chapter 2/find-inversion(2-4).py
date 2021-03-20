"""
-*- coding:utf-8 -*-
 @time :2019.05.22
 @IDE : pycharm
 @autor :juzh
 @email : jzh19980807@163.com
 查找数列中的逆序对，由归并排序修改得到
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
    Count=0
    if low<high:
        mid=int((low+high)/2)
        Count1=merge_sort(A,low,mid)
        Count2=merge_sort(A,mid+1,high)
        Count3=merge(A,low,mid,high)
        Count=Count1+Count2+Count3
    return Count

def merge(A,low,mid,high):
    B=A[low:mid+1];B.append(float("inf"))
    Count=0

    C=A[mid+1:high+1];C.append(float("inf"))
    i=0;j=0
    for k in range(low,high+1):
        if B[i]<=C[j]:
            A[k]=B[i]
            i=i+1
        else:
            A[k]=C[j]
            j=j+1
            Count=Count+len(B)-1-i
    return Count


global randomList
randomList=[2,3,8,6,1]

print(randomList)
count=merge_sort(randomList,0,len(randomList)-1)

print(randomList)
print(count)

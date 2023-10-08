#热爱学习的CXQ

from random import *

list=[]

fo = open("text1.txt","w")
for i in range(0,10):
    for j in range(0,3):
        m=str(randint(1,50))
        fo.write(m)
        if j==1:
            list.append(int(m))
        fo.write(",")
    fo.write("\n")

def average(list):
    ave=0
    for i in range(0,len(list)):
        ave+=list[i]
    ave=ave/len(list)
    return ave

def max(list):
    max=list[0]
    for i in range(1,len(list)):
        if list[i]>max:
            max=list[i]
    return max

def min(list):
    list.sort()
    min = list[0]
    return min

def mid(list):
    list.sort
    if len(list)%2!=0:
        return list[(len(list-1)/2)]
    else:
        return (list[int(len(list)/2)]+list[int((len(list)/2)-1)])/2
print(list)
print("average:",average(list))
print("max",max(list))
print("min",min(list))
print("mid",mid(list))
fo.close()
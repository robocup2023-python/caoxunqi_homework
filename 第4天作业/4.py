list=[1,2,4,5,6,7,8,9]
n=len(list)
m=input()
for i in range(0,n-m):
    num=list[0]
    del list[0]
    list.append(num)
print[list]
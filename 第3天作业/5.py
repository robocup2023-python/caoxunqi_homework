flag=1
a=int(input())
if a%4!=0:
    flag=0
if a%100==0 and a%400!=0:
    flag=0
if flag==1:
    print("is lunar year")
else:
    print("not lunar year")
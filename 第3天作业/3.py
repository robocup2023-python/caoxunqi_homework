num= int(input())
num1=num
count=0
while num1//10!=0:
    num1=num1//10
    count+=1
count+=1
print("位数为",count)
str1=str(num)
count2=count
for i in range(1,count+1):
    print(str1[-1:],end="")
    str1=str1[0:count2-1]
    count2-=1
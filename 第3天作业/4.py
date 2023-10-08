num= int(input())
num1=num
count=0
while num1//10!=0:
    num1=num1//10
    count+=1
count+=1
str1=str(num)
count2=count
flag=0
for i in range(1,count+1):
    if str1[i-1:i]!=str1[count-i:count-i+1]:
        flag=1
        break
if flag==1:
    print("not huiwen number")
else:
    print("is huiwen number")
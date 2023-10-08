x0=100.0
sum=0.0
for i in range(1,11):
    sum+=(x0+x0/2)
    x0/=2
print("总路程为",sum)
print("最后一次为%d" %x0)
a,n=0,0
a=int(input("a:"))
n=int(input("n:"))
sum=0
for i in range(1,n+1):
    sum+=(a*i*(10**i-1))
print(sum)
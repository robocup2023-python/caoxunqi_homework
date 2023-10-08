ge=1
shi=1
bai=1
for i in range(100,1000):
    ge=i%10
    bai=i//100
    shi=(i-100*bai)//10
    if (ge**3+bai**3+shi**3)==i:
        print(i,end=" ")
for i in range(100,201):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
    if flag!=1:
        print(i)
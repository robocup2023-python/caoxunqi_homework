inivec=[2,5,7,8,9]
num=int(input())
if num>inivec[-1]:
    inivec.append(num)
else:
    for i in range(0,len(inivec)):
        if num>inivec[-(i+1)]:
            inivec.insert(-(i),num)
            break
print(inivec)
            
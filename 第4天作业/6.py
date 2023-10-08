list=list(range(1000))
for inde in range(999,-1,-1):
    if list[inde]%2!=0:
        list.pop(inde)

print(list)
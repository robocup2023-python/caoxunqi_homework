str="*"
for i in range(1,9,2):
    print(str.center(7))
    str=str+"**"
str=str[0:5]
len=5
for i in range(1,4):
    print(str.center(7))
    len-=2
    str=str[0:len]
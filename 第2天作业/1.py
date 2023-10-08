str="abcd"
digit=0
alpha=0
str1=input()
for n in str1:
        if n.isdigit():
            digit+=1
        if n.isalpha():
            alpha+=1
print("digit:",digit)
print("alpha:",alpha)
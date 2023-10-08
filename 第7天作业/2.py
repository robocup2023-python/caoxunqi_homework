from random import *
import string

fo = open("text.txt","w")
n = int(input("n:"))
for i in range(0,n):
    ran_str = ''.join(sample(string.ascii_letters + string.digits, 10))
    fo.write(ran_str)
    fo.write('\n')
fo.close()

fo1=open("text.txt","r")
fo2=open("text_copy.txt","w")
for i in range(0,n):
    str = fo1.readline()
    fo2.write(str)
fo1.close()
fo2.close()


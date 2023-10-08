#热爱学习的CXQ
from random import *
import string

fo = open("text.txt","r+")
fo.write("python")
fo.seek(0,2)
fo.write("python")
fo.close()
#热爱学习的CXQ
#生成需要修改的文件
from pathlib import *
import os
import threading

input_path=Path.cwd()
print(input_path)
def creat_dir(dir_path):
	if Path.joinpath(dir_path,"just").exists():
		print("文件夹已经存在")
	else:
		Path.mkdir(Path.joinpath(dir_path,"just"))

creat_dir(input_path )

new_path =Path.joinpath(input_path,"just")

for i in range(0,100):
	path=Path.joinpath(new_path,(str(i)+".txt"))
	Path.touch(path)

os.chdir(new_path)
print(os.getcwd())

file_list= os.listdir()
print(type(file_list[0]))

def rename(name0):
	name0_li=name0.split(".")
	name1=name0_li[0]+'new.txt'
	os.rename(name0,name1)

threads=[]
for i in range(0,len(file_list)):
	thread = threading.Thread(target=rename(file_list[i]))
	threads.append(thread)
	thread.start()

for thread in threads:
	thread.join()

print("end")

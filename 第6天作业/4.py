class Person:

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def personinfo(self):
        print("name:",self.name)
        print("age:",self.age)
        print("sex:%s" %self.sex)

stua=Person("cxq",100,"male")
stua.personinfo()

class Student(Person):
    def __init__(self,name,age,sex,college,classes):
        self.name=name
        self.age=age
        self.sex=sex
        self.college=college
        self.classes=classes

    def studentinfo(self):
        print(self.college)
        print(self.classes)

    def __str__(self):
        return "%s,%s" %(self.college,self.classes)

stub=Student("and",99,"male","XJTU","114514")
stub.personinfo()
stub.studentinfo()
print(stub)
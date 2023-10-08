x=1
y=1
z=1
x=input('x')
y=input('y')
z=input('z')
if x>y:
    m=y
    y=x
    x=m
if x>z:
    m=z
    z=x
    x=m
if y>z:
    m=z
    z=y
    y=m

print(x,"\t",y,"\t",z,"\t")
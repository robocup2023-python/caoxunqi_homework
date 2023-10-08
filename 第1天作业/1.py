i = 100
ge = 0
shi = 0
qian = 0
for x in range(100, 1000):
    qian = x // 100
    shi = (x - qian* 100) // 10
    ge = x % 10
    if (ge == 1 or ge == 2 or ge == 3 or ge == 4) and \
            (qian == 1 or qian == 2 or qian == 3 or qian == 4) and \
            (shi == 1 or shi == 2 or shi == 3 or shi == 4) and \
            ge != shi and ge != qian and shi != qian:
        print(x)

import random

class Universe:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]

    def show(self):
        for row in self.grid:
            print('|'.join(row))
        print('\n')

    def seed(self):
        num=self.width*self.height//4
        print(num)
        seed1=random.sample(range(0,self.height*self.width),num)
        print(seed1)
        for i in seed1:
            seed_hei=(i)//self.width
            seed_wid=i-seed_hei*self.width
            self.grid[seed_hei][seed_wid]='*'

    def alive(self, x, y):
        # 判断细胞是否存活，处理边界情况
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x] == '*'
        return False

    def neighbors(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if self.alive(x + dx, y + dy):
                    count += 1
        return count

    def next(self):
        new_grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                count = self.neighbors(x, y)
                if self.alive(x, y):
                    if count < 2 or count > 3:
                        new_grid[y][x] = ' '
                    else:
                        new_grid[y][x] = '*'
                else:
                    if count == 3:
                        new_grid[y][x] = '*'
        self.grid = new_grid


width = 10
height =10
universe1= Universe(width,height)
universe1.show()
universe1.seed()
universe1.show()
universe1.next()
universe1.show()
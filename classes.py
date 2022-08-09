class Point:
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(10, 20)
print(point1.x_coordinate)


class Person:
    def __init__(self, name):
        self.user = name

    def talk(self):
        print(f"{self.user} is talking")

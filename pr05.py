class Rectangle():

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

if __name__ == '__main__':
    r1 = Rectangle(10, 20)
    print(r1.width, r1.height)

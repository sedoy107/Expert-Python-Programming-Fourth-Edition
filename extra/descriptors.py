class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def _width_get(self):
        return self.x2 - self.x1

    def _width_set(self, value):
        self.x2 = self.x1 + value

    def _height_get(self):
        return self.y2 - self.y1

    def _height_set(self, value):
        self.y2 = self.y1 + value

    width = property(_width_get, _width_set, doc="Width of the rectangle")
    height = property(_height_get, _height_set, doc="Height of the rectangle")

    def __repr__(self):
        return f"Rectangle({self.x1}, {self.y1}, {self.x2}, {self.y2})"


if __name__ == "__main__":
    rect = Rectangle(10, 10, 20, 20)
    print(rect)
    print(rect.width, rect.height)
    rect.width = 30
    print(rect)
    print(rect.width, rect.height)
    rect.height = 40
    print(rect)
    print(rect.width, rect.height)
    rect.width = 50
    print(rect)
    print(rect.width, rect.height)

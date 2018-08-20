class Rectangle:
    def __init__(self, left, top, width, height):
        self._left = left
        self._top = top
        self._width = width
        self._height = height
        self._set_right()
        self._set_bottom()

    def get_left(self):
        return self._left

    def get_bottom(self):
        return self._bottom

    def get_top(self):
        return self._top

    def get_right(self):
        return self._right



    def _set_right(self):
        self._right = self._left + self._width

    def _set_bottom(self):
        self._bottom = self._top + self._height

    def is_inside(self, other_rect):
        isInLeft = self.get_left() >= other_rect.get_left()
        isInRight = self.get_right() <= other_rect.get_right()
        isInBottom = self.get_bottom() <= other_rect.get_bottom()
        isInTop = self.get_top() >= other_rect.get_top()

        isInside = isInLeft and isInRight and isInTop and isInBottom

        return isInside


def read_rect():
    inputData = input().split(' ')
    left = int(inputData[0])
    top = int(inputData[1])
    width = int(inputData[2])
    height = int(inputData[3])

    rectangle = Rectangle(left, top, width, height)


rect = read_rect()
other_rect = read_rect()

isInside = rect.is_inside(other_rect)

if isInside:
    print('Inside')

else:
    print('Not Inside')

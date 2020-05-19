class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                print("size must be >= 0")
                raise ValueError
        else:
            print("size must be an integer")
            raise TypeError

    def area(self):
        return self.__size ** 2
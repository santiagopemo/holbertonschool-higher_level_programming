#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                print("size must be >= 0")
                raise ValueError
        else:
            print("size must be an integer")
            raise TypeError

    def area(self):
        return self.__size ** 2

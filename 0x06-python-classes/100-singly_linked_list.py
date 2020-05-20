#!/usr/bin/python3
""" Singly linked list module """


class Node:
    """ Class Node """

    def __init__(self, data, next_node=None):
        """ Initializates the data """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Return the data of a Node instance """
        return self.__data

    @data.setter
    def data(self, value):
        """ Sets the data of a Node instance """
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ Return the next node of a Node instance """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Sets the next node of a Node instance """
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ Class SinglyLinkedList """

    def __init__(self):
        """ Initializates a Singly linked list """
        self.__head = None

    def __str__(self):
        """ Prints the linked list """
        string = ""
        tmp = self.__head
        while tmp.next_node is not None:
            string += "{}\n".format(tmp.data)
            tmp = tmp.next_node
        string += "{}".format(tmp.data)
        return string

    def sorted_insert(self, value):
        """ Adds a new node sortedly in a linked list """
        new = Node(value)
        if self.__head is None or new.data <= self.__head.data:
            if self.__head:
                new.next_node = self.__head
            self.__head = new
            return
        tmp = self.__head
        while tmp.next_node is not None:
            if new.data <= tmp.next_node.data:
                break
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
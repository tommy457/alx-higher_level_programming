#!/usr/bin/python3

"""Classes for a singly-linked list."""


class Node:
    """Define a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the singly-linked.
            next_node (Node): The next node of the singly-linked.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return data of the current Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """setting value to current Node's data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return the next_node of the singly-linked list."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Setting the value of next Node's data
           Args:
                   value (int): value of Node's data
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define a singly-linked list."""

    def __init__(self):
        """Initalization of new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        position to be sorted list.
        Args:
            value (Node): New Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the human-read representation of a SinglyLinkedList."""
        nodes = []
        curr = self.__head
        while curr is not None:
            nodes.append(str(curr.data))
            curr = curr.next_node
        return ('\n'.join(nodes))

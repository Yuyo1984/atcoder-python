class DoublyLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        head = DoublyLinkedList.Node(None)
        head.next = head
        head.prev = head
        self.size = 0
        self.head = head

    def append(self, element):
        if self.head == None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            element.prev = self.tail
            self.tail = element

    def get(self, index):
        ptr = self.head
        for i in range(index):
            ptr = ptr.next

        return ptr

    def insert(self, index, element):
        ptr = self.get(index)

        if ptr == None:
            self.append(element)
        else:
            element.prev = ptr.prev
            element.next = ptr
            if ptr.prev == None:
                self.head = element
            else:
                ptr.prev.next = element
            ptr.prev = element

    def delete(self, element):
        if element.prev == None:
            self.head = element.next
        else:
            element.prev.next = element.next
        if element.next == None:
            self.tail = element.prev
        else:
            element.next.prev = element.prev


if __name__ = '__main__':
    n, q = map(int, input().split())
    trains = []
    for i in range(q):
        query = list(map(int, input().split()))
        q_t = query[0]

        if q_t == 0:
            

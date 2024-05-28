class Deque:
    class Node:
        def __init__(self, x, y = None, z = None):
            self.data = x
            self.next = y
            self.prev = z

    def __init__(self):
        head = Deque.Node(None)
        head.next = head
        head.prev = head
        self.size = 0
        self.head = head

    def push_front(self, x):
        h = self.head
        q = h.next
        p = Deque.Node(x, q, h)
        h.next = p
        q.prev = p
        self.size += 1

    def push_back(self, x):
        h = self.head
        p = h.prev
        q = Deque.Node(x, h, p)
        h.prev = q
        p.next = q
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            raise IndexError
        h = self.head
        q = h.next
        p = q.next
        p.prev = h
        h.next = p
        self.size -= 1
        return q.data

    def pop_back(self):
        if self.size == 0:
            raise IndexError
        h = self.head
        q = h.prev
        p = q.prev
        p.next = h
        h.prev = p
        self.size -= 1
        return q.data

if __name__ == '__main__':
    q = Deque()
    Q = int(input())
    for _ in range(Q):
        query = list(input().split())
        q_t = query[0]

        if q_t == '0':
            v = query[1]
            q.push_front(v)

        elif q_t == '1':
            v = query[1]
            q.push_back(v)

        elif q_t == '2':
            try:
                print(q.pop_front())
            except IndexError:
                print('Error')
        elif q_t == '3':
            try:
                print(q.pop_back())
            except IndexError:
                print('Error')

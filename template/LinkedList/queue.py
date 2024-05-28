class Node:
    def __init__(self, value=''):
        self.next = None
        self.prev = None
        self.value = value

DL = Node()
DL.next = DL
DL.prev = DL

def enqueue(v):
    v.next = DL.next
    v.prev = DL
    DL.next = v
    (v.next).pre = v

def dequeue():
    tail = DL.prev
    if tail == DL:
        return('Error')
    else:
        ret = tail.value
        DL.prev = tail.prev
        (DL.prev).next = DL
        del tail

        return (ret)

Q = int(input())
for _ in range(Q):
    query = list(input().split())
    q_t = query[0]

    if q_t == '0':
        S = query[1]
        v = Node(S)
        enqueue(v)
    else:
        print(dequeue())

class Queue:
    def __init__(self):
        self.Q = list()

    def enqueue(self, x):
        self.Q.append(x)

    def dequeue(self):
        if len(self.Q) == 0:
            return None
        res = self.Q[0]
        del self.Q[0]
        return res

    def is_empty(self):
        return len(self.Q) == 0

    def __str__(self) -> str:
        return str(self.Q)


def main():
    que = Queue()
    que.enqueue(4)
    print(que)
    que.enqueue(8)
    print(que)
    que.enqueue(1)
    print(que)
    que.dequeue()
    print(que)
    que.enqueue(7)
    print(que)
    que.dequeue()
    print(que)


if __name__ == "__main__":
    main()

class Stack:
    def __init__(self):
        self.S = list()  # 要素を管理する配列

    def push(self, x):
        self.S.append(x)

    def pop(self):
        res = self.S[-1]
        del self.S[-1]
        return res

    def peak(self):
        return self.S[-1]

    def empty(self):
        self.S.clear()

    def size(self):
        return len(self.S)

    def __str__(self) -> str:
        return str(self.S)


def main():
    st = Stack()
    st.push(8)
    print(st)
    st.push(6)
    print(st)
    st.push(7)
    print(st)
    print(st.pop())
    print(st)
    st.push(5)
    print(st)
    print(st.pop())
    print(st)


if __name__ == "__main__":
    main()

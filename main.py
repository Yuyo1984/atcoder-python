# ノード
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 連結リスト
class LinkedList:
    # 初期化
    def __init__(self):
        self.head = None
        self.tail = None

    # データの検索
    def search_with_previous(self, data):
        current = self.head
        previous = None

        while current is not None:
            if current.data == data:
                return current, previous
            previous = current
            current = current.next

        return None, None

    def search(self, data):
        current, _ = self.search_with_previous(data)

        return current is not None

    # 挿入
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # 削除
    def remove(self, data):
        current, previous = self.search_with_previous(data)

        if current is None:
            return False

        if previous is not None:
            previous.next = current.next
        else:
            self.head = current.next

        if current.next is None:
            self.tail = previous

        return True

    # プッシュ
    def push(self, x):
        new_node = Node(x)

        new_node.data = x

        new_node.next = self.head

        self.head = new_node

    # ポップ
    def pop(self):
        if self.head is None:
            return False

        head = self.head.data

        self.head = self.head.next

        return head

    # リストの表示
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

Q = int(input())
LL = LinkedList()
for i in range(Q):
    query = list(input().split())
    q_t = query[0]
    if q_t == '0':
        LL.push(query[1])

    elif q_t == '1':
        head = LL.pop()
        if head == False:
            print("Error")
        else:
            print(head)

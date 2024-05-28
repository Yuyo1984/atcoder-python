class Node:
    def __init__(self, value=''):
        self.next = None
        self.value = value

# 初期化
LL = Node()
LL.next = LL

# 先頭への要素の挿入
def insert(v):
    v.next = LL.next
    LL.next = v

# 先頭の要素を返して削除
def erase():
    front = LL.next
    # 連結リストが空なら、Errorを返す
    if front == LL:
        return('Error')
    else:
        ret = front.value
        LL.next = front.next
        del front

        return(ret)

Q = int(input())
for _ in range(Q):
    query = list(input().split())
    q_t = query[0]

    if q_t == '0':
        S = query[1]
        v = Node(S)
        insert(v)
    else:
        print(erase())


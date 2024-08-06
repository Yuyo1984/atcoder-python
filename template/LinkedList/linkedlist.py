# 連結リストの各ノード
class Node:
    def __init__(self, value=""):
        self.next = None
        self.value = value


# 連結リストの初期化
LL = Node()
LL.next = LL


# 連結リストへ先頭への要素の挿入
def insert(v):
    v.next = LL.next
    LL.next = v


# 入力
Q = int(input())
for query in range(Q):
    typ, S = input().split()
    if typ == "0":
        # ノードを作成する
        v = Node(S)
        insert(v)
    else:
        # 先頭からk(=S)個
        v = LL
        for i in range(int(S)):
            v = v.next
            if v == LL:
                break
            print(v.value, end=" ")
        print()

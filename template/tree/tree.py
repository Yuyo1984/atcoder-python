# 森の実装
# 森とは、木の集合である。各ノードが最大で一つの親ノードを持ち、木の集合を構成する。
# 森の大きさと形は、ノードの数Nと各ノードが持つ親の番号で決まる。
# ノードにはそれぞれ0からN-1の番号が付けられる。
# 森の形状は、各ノードが持つ親へのリンクの変化によって変わる。

# 他の木構造と同様に、森のノードの列に、一次元の配列変数を関連づける。
# 木が集合を表し、ノードはある集合に属する要素とみなすことが出来る。
# ノードは二つ以上の木に属する事はないので、森は互いに素な集合を管理するデータ構造の実装に応用することができる。


class TreeNode:
    def __init__(self, value, node_id):
        self.value = value
        self.node_id = node_id
        self.children = list()

    def add_child(self, child_node):
        self.children.append(child_node)

    def find_node(self, node_id):
        if self.node_id == node_id:
            return self
        for child in self.children:
            result = child.find_node(node_id)
            if result:
                return result
        return None

    def __repr__(self, level=0):
        ret = "\t" * level + f"{self.value} (ID: {self.node_id})\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


class Tree:
    def __init__(self, root_value, root_id):
        self.root = TreeNode(root_value, root_id)

    def add_child_to_node(self, parent_id, child_value, child_id):
        parent_node = self.root.find_node(parent_id)
        if parent_node:
            parent_node.add_child(TreeNode(child_value, child_id))
        else:
            print(f"Node with ID {parent_id} not found.")

    def __repr__(self):
        return repr(self.root)


class Forest:
    def __init__(self):
        self.trees = list()
        self.next_id = 0

    def add_tree(self, root_value):
        tree = Tree(root_value, self.next_id)
        self.trees.append(tree)
        self.next_id += 1
        return tree

    def add_child_to_tree(self, tree_id, parent_id, child_value):
        if tree_id < len(self.trees):
            tree = self.trees[tree_id]
            tree.add_child_to_node(parent_id, child_value, self.next_id)
            self.next_id += 1
        else:
            print(f"Tree with ID {tree_id} not found.")

    def __repr__(self) -> str:
        ret = ""
        for tree in self.trees:
            ret += repr(tree)
        return ret


# 使用例
def main():
    forest = Forest()
    while True:
        print("1. 木を作成")
        print("2. 木に子ノードを追加")
        print("3. 森を表示")
        print("4. 操作を終了")

        query = input("操作を入力してください: ")

        if query == "1":
            root_value = int(input("作成したい木の値を入力してください: "))
            forest.add_tree(root_value)

        elif query == "2":
            tree_id = int(input("子ノードを追加したい木のIDを入力してください: "))
            parent_id = int(input("親ノードのIDを入力してください: "))
            child_value = int(input("子ノードの値を入力してください: "))
            forest.add_child_to_tree(tree_id, parent_id, child_value)

        elif query == "3":
            print(forest)

        elif query == "4":
            break

        else:
            print("不正な入力がされました。もう一度やり直してください。")


if __name__ == "__main__":
    main()

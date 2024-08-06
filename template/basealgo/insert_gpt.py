def insertion(sorted_list, value):
    # 線形探索を使用して挿入位置を見つける
    index = 0
    while index < len(sorted_list) and sorted_list[index] < value:
        index += 1

    # 挿入のためにリストを拡張
    sorted_list.append(None)  # 末尾にダミーの要素を追加

    # 挿入位置から末尾までの要素を右にシフト
    for i in range(len(sorted_list) - 1, index, -1):
        sorted_list[i] = sorted_list[i - 1]
        print(*sorted_list)

    # 挿入位置に新しい要素を追加
    sorted_list[index] = value


# 使用例
if __name__ == "__main__":
    sorted_list = [1, 2, 4, 5, 6]
    print("元のリスト:", sorted_list)

    insertion(sorted_list, 3)
    print("3を挿入後のリスト:", sorted_list)

    insertion(sorted_list, 0)
    print("0を挿入後のリスト:", sorted_list)

    insertion(sorted_list, 7)
    print("7を挿入後のリスト:", sorted_list)

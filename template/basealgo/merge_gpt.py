def merge_sorted_halves(arr):
    # 配列の中央を計算
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # インデックスの初期化
    i, j, k = 0, 0, 0

    # マージ処理
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # 残りの要素をコピー
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


# 使用例
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print("元のリスト:", arr)
    merged_arr = merge_sorted_halves(arr)
    print("マージ後のリスト:", merged_arr)

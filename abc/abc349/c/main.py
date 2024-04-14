S = input().upper() # 比較のために大文字に変換
T = input()

# コードの末尾がXの場合、残りの2文字に対して調べれば良いので取り除く
if T[-1] == 'X':
    T = T[:-1]

# 左端から比較していって、コードに使われてる文字が順番にあるか調べていく。
idx = 0
for s in S:
    if s == T[idx]:
        idx += 1

    if idx >= len(T):
        print("Yes")
        exit()

print("No")


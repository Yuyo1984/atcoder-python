# やりたいこと
# 前のレベルのカーペットを使って、周りを描画したい
# 中央だけは全て点で埋めてそれ以外はシャープで埋める
# 再帰関数を上手く使えないか？
def drawCarpet(deep):
    if deep == 0:
        return ["#"]

    base_carpet = drawCarpet(deep - 1)
    new_carpet = []
    size = len(base_carpet)

    for i in range(3):
        for line in base_carpet:
            if i == 1:
                new_carpet.append(line + "." * size + line)
            else:
                new_carpet.append(line * 3)
    return new_carpet


# input
N = int(input())
# solve
ans = drawCarpet(N)
# output
for x in ans:
    print("".join(x))

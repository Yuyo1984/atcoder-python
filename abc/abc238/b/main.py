# まず分ける
# 90 | 270 → 180 | 90, 90 → 45, 180 | 90, 45 → 60, 90, 45 | 45, 120
# 180と360超えたら切り替えないと
# mod360でどれだけ回転してるのか見る必要あり？
# 上のパターン見てよく考えてみよう
# 色々実験して分からなかったので解説AC
# ピザではなく包丁に着目
# ピザを時計回りに回転は包丁を反時計に回転と言い換えられる
# あとは切れ込みを入れてあるかbool型配列で管理
# 切り分けられたピザの大きさを見ていく
# 例)0, 120, 180なら120-0=120, 180-120=60, 360-180=180が存在する
# 最初に切れ込みを入れた位置を起点にして実装すると楽


N = int(input())
A = [*map(int, input().split())]

fl = [False] * 360
fl[0] = True
p = 0

for i in range(N):
    p += A[i]
    p %= 360
    fl[p] = True

res = 0
cur = 0
# 最初に入れた切り込みから反回転に見ていくイメージ
for i in range(361):
    if fl[i % 360]:
        res = max(res, cur)
        cur = 0
    cur += 1

print(res)

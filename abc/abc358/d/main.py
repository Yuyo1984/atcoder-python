"""貪欲法っぽい・・・
絶対に無理なパターンはまだ選んでない箱の中の菓子の数
全てを渡そうとしてる人に必要な菓子の数が上回った場合
でも、それを見ようとしてたら配列全部見なきゃいけなくならない？

"""

# input
n, m = map(int, input().split())
A = [*map(int, input().split())]
A.sort()
B = [*map(int, input().split())]
# solve
ans = 0

# output
print(ans)

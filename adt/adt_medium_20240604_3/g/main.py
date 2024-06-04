from collections import defaultdict

# input
S = input()
# solve
# 区間ごとの各数字の出現回数の偶奇を記録するための辞書を持っておく
mp = defaultdict(int)
# 各数字の出現回数の偶奇を記録しておくための配列を持っておく
cnt = [0] * 10
# 出現回数の偶奇を切り替えてその区間の個数を１増やす
mp[tuple(cnt)] += 1
for s in S:
    cnt[int(s)] ^= 1
    mp[tuple(cnt)] += 1

# 同じ出現回数から2つ選んだ組み合わせを答えに足し合わせていく
ans = 0
for v in mp.values():
    ans += v * (v - 1) // 2

# output
print(ans)

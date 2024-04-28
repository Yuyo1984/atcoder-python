# ABC113-C

# 県の総数と市の総数を入力
N, M = map(int, input().split())

# 各県に対応する市の認識番号とその認識番号をどの順番で入力したかの対応表を作成
D = [[] for i in range(N)]

# 対応表に入力していく
for i in range(M):
    p, y = map(int, input().split()) # 県の番号と市の認識番号を入力
    D[p-1].append((y, i)) # 対応表に認識番号と順番の組を入れていく

ans = [None] * M # 答えのリストを作成

for i, d in enumerate(D): # 対応表の添字と中身に対して操作
    # print(i, d)
    d.sort() # 対応表の各県の市の認識番号を年の昇順に並び替え
    for k, (y, j) in enumerate(d): # 各県の対応表に対する県の番号、市の誕生年と対応表の添字に対して操作
        # print(k, (y, j))
        ans[j] = str(i+1).zfill(6) + str(k+1).zfill(6) # ずらして1-indexedにして、zfillでゼロ埋めして、答えのリストに格納

print(*ans, sep = '\n') # リストをアンパック、改行文字で分割して出力

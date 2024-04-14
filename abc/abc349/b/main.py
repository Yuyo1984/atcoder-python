import string
S = input()

# 'abcdefghijklmnopqrstuvwxyz'の文字列を用意しておく(string.ascii_lowercaseはその為のモデュール)
lower = string.ascii_lowercase
# Sの中の文字それぞれの出現回数を管理する配列を作成
chars_cnt = [0] * 26

# 入力された文字列を左から見ていって、何の文字が出てきたかカウント
for i in range(len(S)):
    for j in range(26):
        if S[i] == lower[j]:
            chars_cnt[j] += 1

# 制約上、各文字の出現回数は1-100の範囲なので、それぞれの出現回数において、0種類か2種類になってるか確かめる
# もし、ある出現回数である文字の種類数がどちらでもない場合、その時点で条件を満たしていないので、Noを出力してプログラム終了
for i in range(1,101):
    cnt = 0 # 文字の種類数
    for j in range(26):
        #格納されてる出現回数と今調べてる出現回数が一致したら、種類数を1増やす
        if chars_cnt[j] == i:
            cnt += 1
    # 条件を満たしてるかチェック
    if cnt != 0 and cnt != 2:
        print("No")
        exit()

# 全部確かめてはじかれていないなら、条件を満たしているため、Yesを出力
print("Yes")


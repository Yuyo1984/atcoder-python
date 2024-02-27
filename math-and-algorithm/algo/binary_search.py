def binary_search(ans, x, y):
    y = (y + 1) // 2
    if ans == 'y':
        return x - y, y
    else:
        return x + y, y

print("1から100までの数字を一つ思い浮かべてください")
print("用意ができたらEnterを押してください")
input()
print("思い浮かべましたか？それではこれから私のする質問にYesかNoかで答えてください")

n = 50
mid = 50
ans = ''
while True:
    if mid == 1:
        if ans != 'y':
            n += 1
        print("その数は" + str(n) + "ですか?")
        final = input("Yesならy, Noならnと入力してください")
        if final == 'y':
            print("当てられてよかったです！また遊んでくださいね！")
            exit()
        else:
            print("何か間違えたようですね・・・もう一度試させてください！")
            n, mid = 50
    else:
        print("その数は" + str(n) + "以下ですか?")
        ans = input("Yesならy、Noならnと入力してください")
        n, mid = binary_search(ans, n, mid)

print("1から100までの数字を一つ思い浮かべてください")
print("用意ができたらEnterを押してください")
input()
print("思い浮かべましたか？それではこれから私のする質問にYesかNoかで答えてください")

low = 0
high = 100
mid = (low + high) // 2

while low <= high:
    mid = (low + high) // 2
    if low == mid:
        print("あなたの思い浮かべた数は" + str(low) + "ですね")
        exit()
    elif high == mid:
        print("あなたの思い浮かべた数は" + str(high) + "ですね") 
    else:
        print("その数は" + str(mid) + "以下ですか?")
        ans = input("Yesならy, Noならnと入力してください")
        if ans == 'y':
            high = mid
        elif ans == 'n':
            low = mid
        else:
            print("正しい回答が入力されませんでした、もう一度やり直してください")
            exit()

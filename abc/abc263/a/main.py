from sys import stdin
input = stdin.readline

cards= [*map(int, input().split())]
card1 = cards[0]
for i in cards:
    if i != card1:
        card2 = i
        break

if cards.count(card1) == 2 and cards.count(card2) == 3:
    print("Yes")
elif cards.count(card1) == 3 and cards.count(card2) == 2:
    print("Yes")
else:
    print("No")

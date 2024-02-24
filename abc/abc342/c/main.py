from string import ascii_lowercase

N = int(input())
S = input()

Q = int(input())

before_q = ascii_lowercase
after_q = ascii_lowercase

for i in range(Q):
    c, d = input().split()
    after_q = after_q.replace(c, d)

print(S.translate(str.maketrans(before_q, after_q)))

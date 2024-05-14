x, a, b = map(int, input().split())

if b - a >= x+1:
    print('dangerous')
elif 0 < b - a <= x:
    print('safe')
else:
    print('delicious')

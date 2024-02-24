from sys import stdin
input = stdin.readline

N = input().rstrip()
o = N[-1]

if (o == '2' or o == '4' or o == '5' or o == '7' or o == '9'):
    print('hon')
elif (o == '0' or o == '1' or o == '6' or o == '8'):
    print('pon')
else:
    print('bon')

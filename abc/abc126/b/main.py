S = input()

YY = int(S[:2])
MM = int(S[2:])

if 1 <= YY <= 12 and 1 <= MM <= 12:
    print('AMBIGUOUS')
elif 1 <= YY <= 12:
    print('MMYY')
elif 1 <= MM <= 12:
    print('YYMM')
else:
    print('NA')

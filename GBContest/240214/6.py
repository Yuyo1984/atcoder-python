import re
S = input()

if re.fullmatch(r'.*[I|i]+.*[C|c]+.*[T|t]+.*', S) != None:
    print('YES')
else:
    print('NO')


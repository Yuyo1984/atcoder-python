n, m = map(int, input().split())
s = input()

shirts = m
logo_shirts = 0
cnt = 0
for i in range(n):
    if s[i] == '0':
        shirts = m
        logo_shirts = cnt
    elif s[i] == '1':
        if shirts <= 0 and logo_shirts <= 0:
            logo_shirts += 1
            cnt += 1
        if shirts > 0:
            shirts -= 1
        else:
            logo_shirts -= 1
 
    else:
        if logo_shirts <= 0:
            logo_shirts += 1
            cnt += 1
        logo_shirts -= 1
    
print(cnt)

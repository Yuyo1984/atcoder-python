N = input()

ans = -1
for i in range(1 << len(N)):
    num = ""
    cnt = 0
    for j in range(len(N)):
        if i & (1 << j):
            num += N[j]
            cnt += 1
    num_digit_sum = 0

    for k in range(len(num)):
        num_digit_sum += int(num[k])
    if num_digit_sum % 3 == 0 and num_digit_sum != 0 and ans == -1:
        ans = len(N) - cnt
    elif num_digit_sum % 3 == 0 and num_digit_sum != 0 and ans != -1:
        ans = min(ans, len(N) - cnt)

print(ans)

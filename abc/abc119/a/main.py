y, m, d = input().split("/")

ans = ""
if y <= "2018":
    ans = "Heisei"
elif y == "2019" and "01" <= m <= "04":
    ans = "Heisei"
else:
    ans = "TBD"

print(ans)

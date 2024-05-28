N = int(input())
result = []
for i in range(N):
    result.append(list(input()))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if result[i][j] == "W" and result[j][i] != "L":
            print("incorrect")
            exit()
        if result[i][j] == "L" and result[j][i] != "W":
            print("incorrect")
            exit()
        if result[i][j] == "D" and result[j][i] != "D":
            print("incorrect")
            exit()

print("correct")

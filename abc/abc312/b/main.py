n, m = map(int, input().split())
code = []
for i in range(n):
    code.append(list(input()))

tak1 = [['#', '#', '#', '.'],['#', '#', '#', '.'],['#', '#', '#', '.'],['.', '.', '.', '.']]
tak2 = [['.', '.', '.', '.'],['.', '#', '#', '#'],['.', '#', '#', '#'],['.', '#', '#', '#']]
ansl = []
for i in range(n-8):
    for j in range(m-8):
        area1 = [code[j:j+4] for code in code[i:i+4]]
        area2 = [code[j+5:j+9] for code in code[i+5:i+9]]
        if area1 == tak1 and area2 == tak2:
            ansl.append([i+1, j+1])

for item in ansl:
    print(item[0], item[1])


n, x, y, z = map(int, input().split())
A = [*map(int, input().split())]
B = [*map(int, input().split())]

students_math_point = {}
students_eng_point = {}
students_total_point = {}
is_passed = [False] * (n + 1)
for i in range(n):
    a = A[i]
    b = B[i]
    students_math_point[i + 1] = a
    students_eng_point[i + 1] = b
    students_total_point[i + 1] = a + b

students_math_point = sorted(
    students_math_point.items(), key=lambda x: x[1], reverse=True
)
students_eng_point = sorted(
    students_eng_point.items(), key=lambda x: x[1], reverse=True
)
students_total_point = sorted(
    students_total_point.items(), key=lambda x: x[1], reverse=True
)


c_x = 0
for key in students_math_point:
    if c_x == x:
        break
    is_passed[key[0]] = True
    c_x += 1

c_y = 0
for key in students_eng_point:
    if c_y == y:
        break
    if not (is_passed[key[0]]):
        is_passed[key[0]] = True
        c_y += 1

c_z = 0
for key in students_total_point:
    if c_z == z:
        break
    if not (is_passed[key[0]]):
        is_passed[key[0]] = True
        c_z += 1

for i in range(1, n + 1):
    if is_passed[i]:
        print(i)

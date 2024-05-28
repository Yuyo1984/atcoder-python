n, x = map(int, input().split())
a = [*map(int, input().split())]

left = 0
right = n
mid = (left + right) // 2

while x != a[mid]:
    if x < a[mid]:
        right = mid - 1
    elif x > a[mid]:
        left = mid + 1
    mid = (left + right) // 2

print(mid+1)

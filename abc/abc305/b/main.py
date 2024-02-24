from sys import stdin
input = stdin.readline

def calc(p, q):
    pos_p = point_list.index(p)
    pos_q = point_list.index(q)
    dis_p, dis_q = 0, 0
    for i in range(pos_p+1):
        dis_p += dis_list[i]
    for i in range(pos_q+1):
        dis_q += dis_list[i]
    return abs(dis_q - dis_p)

p, q = map(str, input().split())
dis_list = [0, 3, 1, 4, 1, 5, 9]
point_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

print(calc(p, q))

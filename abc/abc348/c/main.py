import sys
input = sys.stdin.readline
import numpy as np
import math

N = int(input())
menu = []
for i in range(N):
    a, c = map(int, input().split())
    menu.append([a, c])

menu_dict = {}
for i in range(len(menu)):
    c = menu[i][1]
    a = menu[i][0]
    if c not in menu_dict or menu_dict[c] >= a:
        menu_dict[c] = a

print(max(menu_dict.values()))


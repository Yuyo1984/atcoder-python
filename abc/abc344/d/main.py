import sys
input = sys.stdin.readline
import numpy as np
import math

T = input().rstrip()
N = int(input())
ans = 1000
cnt_list = []
str_list = []
for i in range(N):
    A, *S = map(str, input().split())
    cnt_list.append(A)
    str_list.append([*S])

for i in range(N):
    S = ""
    

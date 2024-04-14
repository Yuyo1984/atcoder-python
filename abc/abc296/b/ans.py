S=[input() for _ in range(8)]
for i in range(8):
  for j in range(8):
    if S[i][j]=='*':
      print(f"{'abcdefgh'[j]}{8-i}")
      exit()

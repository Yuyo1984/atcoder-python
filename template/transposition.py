# 与えられた行列の転置行列を返す関数

def transposition(m):
    m = [list(x) for x in zip(*m)]
    return m


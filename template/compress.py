def compress(A):
    S = sorted(list(set(A)))
    ranking = {x: i + 1 for i, x in enumerate(S)}
    compressed = []
    for a in A:
        compressed.append(ranking[a])
    return compressed

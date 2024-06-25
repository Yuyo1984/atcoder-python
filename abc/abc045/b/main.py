a = list(input())
b = list(input())
c = list(input())
a.reverse()
b.reverse()
c.reverse()

n_p = "a"
while True:
    if n_p == "a":
        if len(a) == 0:
            print("A")
            exit()
        x = a.pop()
    elif n_p == "b":
        if len(b) == 0:
            print("B")
            exit()
        x = b.pop()
    else:
        if len(c) == 0:
            print("C")
            exit()
        x = c.pop()
    if x == "a":
        n_p = "a"
    elif x == "b":
        n_p = "b"
    else:
        n_p = "c"

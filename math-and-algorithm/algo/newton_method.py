def newton_method(r, a):
    for i in range(6):
        p_x = a
        p_y = a * a

        l_a = 2.0 * p_x
        l_b = p_y - l_a * p_x

        next_a = (r - l_b) / l_a
        a = next_a
    return a


r, a = map(float, input().split())
print(newton_method(r, a))

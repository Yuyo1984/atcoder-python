import time
def do_fib(n):
    start = time.time()
    print(fib(n))
    stop = time.time()
    print("elapsed: {}".format(stop-start))

def do_fib_memo(n):
    start = time.time()
    print(fib_memo(n))
    stop = time.time()
    print("elapsed: {}".format(stop-start))

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fib_memo(n):
    memo = [0] * (n+1)

    def _fib(n):
        if n <= 1:
            return n
        if memo[n] != 0:
            return memo[n]
        memo[n] = _fib(n-2) + _fib(n-1)
        return memo[n]

    return _fib(n)

if __name__ == '__main__':
    n = int(input())
    do_fib(n)
    do_fib_memo(n)


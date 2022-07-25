#509 Fibonacci sequence

def fib(self, n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return Solution().fib(n-1)+Solution().fib(n-2)
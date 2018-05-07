"""
Fibonacci Sequence
Print n numbers of sequence
"""
def fib(n):
    if(n <= 1):
        return n
    else:
        print(n)
        return fib(n-1) + fib(n-2)

print(fib(4))
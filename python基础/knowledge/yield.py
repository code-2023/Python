#!/usr/bin/python
def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1
    #return 'done'
f=fib(6)
while True:
    try:
        print(f.next())
    except StopIteration:
        break


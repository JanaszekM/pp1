n=int(input('Podaj liczbę'))

def fib(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a

print(fib(n-1))


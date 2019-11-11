
def fib(n):
    global output
    output = ''
    a,b = 0,1

    for i in range(n-1):
        a,b = b,a+b
        output+=str(a) + ' '
    return output
        

print(fib(20))


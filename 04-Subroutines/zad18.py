n=int(input('Podaj liczbe'))

def silnia(n):
    
    #0!=1 and 1!=1
    if n==0 or n==1:
        return 1

    #n! = n * (n-1)!
    if n > 1:
        return n * silnia(n-1)
  
print( f'{n}! = {silnia(n)}' )

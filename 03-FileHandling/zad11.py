import re

with open('land.txt', 'r') as f:
    liczby=re.findall('\d.*?',f.read())
    print(sum(liczby))
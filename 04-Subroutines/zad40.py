p=lambda x:x%2==0
tab=[1,2,3,4,5,6,7,8]

for x in filter(p,tab):
    print(x, end=' ')
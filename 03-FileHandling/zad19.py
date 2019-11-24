import re
z=[]

with open('universities.txt','r') as f:
    for line in f:
        x=line.replace('"','')
        y=x.replace('\n','')
        z.append(y)
        n=sorted(z)
    print(n)


    
    
    
    
    
#    for line in file:
 #       x.append(line.strip().split('\n'))
  #  while i<len(x):
   #     y=str(x[i])
    #    y.replace('\"','')
     #   i+=1
      #  print(y)
    
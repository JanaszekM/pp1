import csv
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    i=1
    for row in reader:
        
        print(i,row[1])
        i+=1
    
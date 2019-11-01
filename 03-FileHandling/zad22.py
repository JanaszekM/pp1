with open('students.txt', 'r')as file:
    for line in file:
        line = line.split(',')
        if line[2] != 'age':
            if int(line[2]) < 30:
                print(f'{line[0]} {line[1]} {line[4]}')
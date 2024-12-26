import re
file = open("input4.txt")
line = []
for lines in file:
    line.append(lines.strip())

total = 0 

for x in range(len(line)):
    for i in range(0, len(line[0])):
        try:
            #forward
            if line[x][i] + line[x][i + 1] + line[x][i + 2] + line[x][i + 3] == 'XMAS': 
                total += 1
        except IndexError: 
            pass
        try:
            #backwards
            if line[x][i] + line[x][i - 1] + line[x][i - 2] + line[x][i - 3] == 'XMAS': 
                total += 1
        except IndexError: 
            pass
        try:
            #up
            if line[x][i] + line[x + 1][i] + line[x + 2][i] + line[x + 3][i] == 'XMAS': 
                total += 1
        except IndexError: 
            pass
        try:
            #down
            if line[x][i] + line[x - 1][i] + line[x - 2][i] + line[x - 3][i] == 'XMAS': 
                total += 1
        except IndexError: 
            pass
        try:
            #diag up right
            if line[x][i] + line[x + 1][i + 1] + line[x + 2][i + 2] + line[x + 3][i + 3] == 'XMAS': 
                total += 1
        except IndexError: 
            pass
        try:
            #diag up left
            if line[x][i] + line[x + 1][i - 1] + line[x + 2][i - 2] + line[x + 3][i - 3] == 'XMAS': 
                total += 1
        except IndexError: 
            pass
        try:
            #diag up left
            if line[x][i] + line[x - 1][i + 1] + line[x - 2][i + 2] + line[x - 3][i + 3] == 'XMAS': 
                total += 1
        except IndexError: 
            pass
        try:
            #diag up left
            if line[x][i] + line[x - 1][i - 1] + line[x - 2][i - 2] + line[x - 3][i - 3] == 'XMAS': 
                total += 1
        except IndexError: 
            pass
        
print(total)
        
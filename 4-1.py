file = open("input.txt")
lines = []
for line in file:
    lines.append(line)

total = 0 
for line in lines:
    for i in range(0, len(lines)):
        try:
            if line[i] + line[i + 1] + line[i + 2] + line[i + 3] == 'XMAS': 
                total += 1
        except: 
            print("forward")
        try:
            if line[i] + line[i + 1] + line[i + 2] + line[i + 3] == 'XMAS': 
                total += 1
        except: 
            print("forward")
        try:
            if line[i] + line[i + 1] + line[i + 2] + line[i + 3] == 'XMAS': 
                total += 1
        except: 
            print("forward")
        try:
            if line[i] + line[i + 1] + line[i + 2] + line[i + 3] == 'XMAS': 
                total += 1
        except: 
            print("forward")
        
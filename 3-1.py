import re

file = open("input3.txt", 'r')
lines = []
for line in file:
    lines.append(line)

sum = 0
for line in lines:
    x = re.findall("(mul[(][\d]{ 1,3},[\d]{1,3}[)])", line)
    for item in x:
        y = re.findall("[\d]{1,3},[\d]{1,3}", item)
        print(y)
        y = y[0].split(",")
        sum += int(y[0]) * int(y[1])
print(sum)
import re

file = open("input3.txt", 'r')
lines = []
for line in file:
    lines.append(line)

sum = 0
flag = True
for line in lines:
    # x = re.sub("(don't[(][)][^>]+?(do[(][)]))|(don't[(][)][^>]+$)", "removed!" , line)
    x = re.findall("(?:mul[(][\d]{1,3},[\d]{1,3}[)])|(?:don[']t[(][)])|(?:do[(][)])", line) 
    print(x)
    for item in x:
        match item:
            case "don't()":
                flag = False
            case "do()":
                flag = True
            case _:
                if flag:
                    y = re.findall("[\d]{1,3}", item)
                    sum += int(y[0]) * int(y[1])
print(sum)
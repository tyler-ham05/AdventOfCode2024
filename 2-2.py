file = open("input2.txt", "r")
lines = []
for line in file:
  lines.append(line.strip().split(" "))


def linevalid(line):
  opp = []
  for i in range(0, len(line) - 1):
    diff = (int(line[i]) - int(line[i + 1]))
    if diff > 0:
      opp.append(1)
    else:
      opp.append(0)
    if diff > 3 or diff == 0 or diff < -3 or len(opp) > 1 and opp[i - 1] != opp[i]:
        return (1, i)
  return (0, 0) 
  
safe = len(lines)
for line in lines:
  potential = linevalid(line)
  if potential[0] == 1:
    line1 = line.copy()
    del line[potential[1]]
    del line1[potential[1] + 1]
    safe -= min(linevalid(line)[0],linevalid(line1)[0])

print(safe)
file = open("input2.txt", "r")
lines = []
for line in file:
  lines.append(line.strip().split(" "))


def line_safe(line):
  opp = []
  for i in range(0, len(line) - 1):
    diff = (int(line[i]) - int(line[i + 1]))
    if diff > 0:
      opp.append(1)
    else:
      opp.append(0)
    if diff > 3 or diff == 0 or diff < -3 or len(opp) > 1 and opp[i - 1] != opp[i]:
        return 1
  return 0
  
safe = len(lines)
for line in lines:
  safe -= line_safe(line)

print(safe)
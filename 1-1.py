file = open("input1.txt", "r")
list1 = []
list2 = []
for line in file:
  lined = line.split("   ")
  list1.append(int(lined[0]))
  list2.append(int(lined[1]))
  
list1 = sorted(list1)
list2 = sorted(list2)

sum = 0
for i in range(len(list1)):
  sum += abs(list1[i] - list2[i])
print(sum)
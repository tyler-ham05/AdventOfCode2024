file = open("input1.txt", "r")
list1 = {}
list2 = []
for line in file:
  lined = line.split("   ")
  list1[int(lined[0])] = 0
  list2.append(int(lined[1]))

  
sum = 0
list2 = sorted(list2)
for i in range(len(list2)):
  if list2[i] in list1:
    list1[list2[i]] += 1

for key in list1:
  sum += key * list1[key]
print(sum)
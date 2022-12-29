list1 = []
num = int(input())
for i in range(num):
    number = (int(i) +3) % 9
    list1.append(number)
list1[0],list1[1],list1[2],list1[3] = list1[2],list1[3],list1[0],list1[1]
print(list1)
s = ''.join(map(str,list1))
print(s)

print("this program will generate odd numbers from 1 to 1000 ")
list1 = []
for number in range(999, 0, -2):
    list1.append(number)
list1.reverse()
print(list1)

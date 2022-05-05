while True:
    print("to stop this prosses enter 0")
    try:
        y = int(input("enter number :"))
    except:
        print("please enter a number we make a default value for input is 27:")
        y = 27
    if y == 0:
        break
    list1 = []
    for i in range(0, 5):
        x = y//2
        t = y % 2
        list1.append(t)
        y = x
    list1.reverse()
    print(list1)

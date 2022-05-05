uname = input("enter your name: ")
counter = 0
file = open("data.txt", "r")
for line in file:
    detail = line.split(",")
    print(detail[0])
    answer= input("your answer is ...." )   
    if answer.strip() == detail[3]:
        print("Correct")
        counter += 1
    else:
        print("Incorrect")
    
result = open("answers.text", "a")
result.writelines("the name is "+uname+" your correct answer is:")
result.writelines(str(counter)+" of 10")
result.close()
print("the name is:"+uname,"your correct answers are:",counter," of 10")





























        ##while True:


##    print("to stop this prosses enter 0")
##    y = int(input("enter munber"))
##
##    if y == 0:
##        break
##    list1 = []
##    for i in range(0, 5):
##        x = y//2
##        t = y % 2
##        list1.append(t)
##        y = x
##    list1.reverse()
##    print(list1)

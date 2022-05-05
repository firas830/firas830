list1 = ["ali", "firas", "youshaa", "rasha",
         "mohamed", "karam", "ghadder", "hussam"]
print("when you finsh your check process please enter 'stop' to stop execute the program \n" )
while True:
    graduatename = input(
        "enter the name to check if that name is graduated or not: ")
    if graduatename.strip() == "stop":
        break
    if graduatename.strip().lower() in list1:
        print(graduatename.strip(), "is graduated")
    else:
        print("the name that you insert",graduatename," is not graduate")

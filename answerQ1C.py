list1 = ["Network", "Math", "Programming", "Physics", "Music"]
for index in range(0, len(list1)):
    words = list1[index].lower()
    if words.startswith('p'):
        print(list1[index])


import random

list1 = ["Hello", " world", " ! "]
print(list1)
print(list1[0])
print(len(list1))

list1[0] = "Hi"
list1.insert(1, " all the ")
list1.append(": )")
list1.extend(["<3", "; )"])

del list1[0]
list1.pop(0)
list1.remove(" world")

print(list1[1:3])
print(list1)

list1.clear()
print(list1)

textebizard = input("Ecris qqch : ").split(" ")
random.shuffle(textebizard)
print(textebizard)


def func1():
    print("Hello")

def func2():
    global word
    print(word)
    word = ":)"
    print(word)

word = "Hi"

def sum(num1, num2):
    result = num1 + num2 
    return result

def max(num1, num2):
    num1 = int(num1)
    num2 = int(num2)

    if num1 < num2:
        print(num2)
    else:
        print(num1)

func1()
func2()
print(sum(1, 4))

type = input("Plus grand des deux nombres : ").split(" ")
max(type[0], type[1])

# for letter in "six":
#     print(letter)
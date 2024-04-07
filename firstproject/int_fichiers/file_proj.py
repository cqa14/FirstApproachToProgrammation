
word_list = ["Hello", ": )", "<3"]

with open("firstproject\int_fichiers\int_test.txt", "w+") as file:
    for word in word_list:
        file.write(word + "\n")
    file.close
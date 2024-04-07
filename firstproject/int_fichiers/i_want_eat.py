
import os
import random

if os.path.exists("firstproject\int_fichiers\meals.txt"):
    with open("firstproject\int_fichiers\meals.txt", "r+") as file:
        meals_list = file.readlines()
        meal_choice = random.choice(meals_list)
        print(meal_choice)
        file.close

else:
    print("Document doesn't exsist")

password = input("Entrer votre mdp :")
password_length = len(password)


if password_length >= 8:
    print("mdp valide")
else:
    print("mdp non-valide")    


print(password_length)
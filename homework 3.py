# -*- coding: utf-8 -*-

import random
username = input("Please enter your username : ")
print("Welcome {}".format(username))
word_list = ["Nurse", "police", "Actor", "Lawyer", "Fisherman"]
chosen_word=random.choice(word_list)
truelist=list()
falselist=list()
chance = 6

while True:
    word = input("Please enter a letter  :")
    if(word not in chosen_word):
        if(word in falselist):
            print("You used the same letter !")
        falselist.append(word)
        print("Your letter isn't in the word")
        chance -= 1
        if (chance == 0):
            print("Your guess chance is over..")
            break
        continue
    elif (word in chosen_word):
        if (word in truelist):
            print("You used the same letter !")
        truelist.append(word)
        if (len(chosen_word) == len(truelist)):
            print("Awesome,you win!!")
            print("Choosen Word is {}".format(chosen_word))
            break
        else:
            continue
        
    
    
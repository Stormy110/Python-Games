from pet_game import Pet 
from subprocess import call
import os
import time

def clear():
    time.sleep(3)
    call('clear' if os.name == 'posix' else 'cls')

main_menu = [   
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Do nothing",
    "Give a toy",
    "Snuggle with pet",
    "Exercise your pet",
    "Give a treat",
    "Speak to pet",
    "Abandon your pet",
]

def print_menu_error():
    print("That was not a valid choice. Try again.\n\n\n")    

def choices_to_string(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    choice_string += "Please choose an option: \n"
    return choice_string

def get_user_choice(choice_list):
    choice = -1
    choice_string = choices_to_string(choice_list)
    while choice == -1:
        try:
            choice = int(input(choice_string))
            if choice <= 0 or choice > len(choice_list):
                raise ValueError
        except ValueError:
            print_menu_error()
    return choice

def main():    
    while True:
        choice = get_user_choice(main_menu)
        if pet_choice == 1:
            pet = dog 
        elif pet_choice == 2:
            pet = cat
        elif pet_choice == 3:
            pet = turtle
        elif pet_choice == 4:
            pet = snake
        elif pet_choice == 5:
            pet = fish
        else:
            pet = bird

        
        if choice == 1:
            pet.play_pet()
            pet.stay_alive()
        elif choice == 2:
            pet.feed_pet()
            pet.stay_alive()
        elif choice == 3:
            pet.get_status()
        elif choice == 4:
            pet.ignore_pet()
            pet.stay_alive()
        elif choice == 5:
            pet.give_toy()
            pet.stay_alive()
        elif choice == 6:
            pet.snuggle()
            pet.stay_alive()
        elif choice == 7:
            pet.exercise()
            pet.stay_alive()
        elif choice == 8:
            pet.treat()
            pet.stay_alive()
        elif choice == 9:
            pet.speak()
            pet.stay_alive()
        elif choice == 10:
            print("\nYou abandoned your pet like a monster. You spend the rest of your life miserable and alone!\n")
            break
        else:
            print("\nPlease choose the correct option.\n")
        if pet.sadness > 80 and pet.sadness < 100:
            print(f"\n{pet.name} is very sad. Please cheer them up!\n")
        if pet.sadness >= 100:
            print("\nYour pet died because you are a terrible person and you broke it's heart.\n")
            break
        if pet.fullness < 20 and pet.fullness > 0:
            print(f"\n{pet.name} is starving! Feed {pet.name} immediately!\n")
        if pet.fullness <= 0:
            print(f"""
{pet.name} is starving to death!
{pet.name} decides to eat you!
You are dead!
            """)
            break
        if pet.happiness < 20 and pet.happiness > 0:
            print(f"\n{pet.name} is very sad. Please cheer them up!\n")
        if pet.happiness <= 0:
            print("\nYour pet ran away because you are a terrible person and nobody will ever love you.\n")
            break
        if pet.happiness >= 150:
            print("\nYou have achieved maximum pet happiness. \nCongratulations, you win!\n")
            break
        if pet.fatness > 130 and pet.fatness < 150:
            print(f"\n{pet.name} has gotten too fat! {pet.name} needs to exercise!\n")
        if pet.fatness >= 150 or pet.fullness >= 100:
            print(f"\n{pet.name} has had a heart attack and died. Next time exercise your pet!\n")
            break
        if pet.boredom > 80 and pet.boredom < 100:
            print(f"\n{pet.name} is very bored. They are thinking about running away...\n")
        if pet.boredom >= 100:
            print(f"\n{pet.name} ran away from you because you are horribly boring!\n")
            break
        clear()


dog = Pet("Peanut WiggleButt", 60, 55, 0, 25)
cat = Pet("Chairman Meow", 60, 50, -1, 15)
turtle = Pet("Count Flufferton", 60, 50, 1, 40)
snake = Pet("Monty Python", 60, 50, 5, 25)
fish = Pet("Magikarp", 60, 50, 55, 20)
bird = Pet("Sir Tweet Tweet", 60, 50, 3, 20)


print(''' 
************* VIRTUAL PET SIMULATOR  ****************
             (press ctrl + c to quit)
''')
while True:        
    try:
        pet_choice = int(input("""
Please choose an animal.
1 - Dog
2 - Cat
3 - Turtle
4 - Snake
5 - Fish
6 - Bird
Choice: """))

        while pet_choice == 1 or pet_choice == 2 or pet_choice == 3 or pet_choice == 4 or pet_choice == 5 or pet_choice == 2:
            if pet_choice == 1:
                print(f"\nCongratulations! {dog.name} is now your pet! Treat them with care or else!\n")
            elif pet_choice == 2:
                print(f"\nCongratulations! {cat.name} is now your pet! Treat them with care or else!\n")
            elif pet_choice == 3:
                print(f"\nCongratulations! {turtle.name} is now your pet! Treat them with care or else!\n")
            elif pet_choice == 4:
                print(f"\nCongratulations! {snake.name} is now your pet! Treat them with care or else!\n")
            elif pet_choice == 5:
                print(f"\nCongratulations! {fish.name} is now your pet! Treat them with care or else!\n")
            elif pet_choice == 6:
                print(f"\nCongratulations! {bird.name} is now your pet! Treat them with care or else!\n")
                   
            main()
            break
    except ValueError:
        print_menu_error()

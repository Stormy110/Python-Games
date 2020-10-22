from pet_game import Pet 


main_menu = [   
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Do nothing",
    "Give a toy",
    "Snuggle with pet",
    "Exercise your pet",
    "Give a treat",
    "Abandon your pet"
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
            if choice == 1:
                dog.play_pet()
                dog.stay_alive()
            elif choice == 2:
                dog.feed_pet()
                dog.stay_alive()
            elif choice == 3:
                dog.get_status()
            elif choice == 4:
                dog.ignore_pet()
                dog.stay_alive()
            elif choice == 5:
                dog.give_toy()
                dog.stay_alive()
            elif choice == 6:
                dog.snuggle()
                dog.stay_alive()
            elif choice == 7:
                dog.exercise()
                dog.stay_alive()
            elif choice == 8:
                dog.treat()
                dog.stay_alive()
            elif choice == 9:
                print("You abandoned your pet. Shortly after, you were hit by a bus and sent to hell.")
                break
            else:
                print("Please choose the correct option.")
            if dog.sadness >= 100:
                print("Your pet died because you are a terrible person and you broke it's heart.")
                break
            if dog.fullness <= 0:
                print("Your pet died because it starved to death. You suck!")
                break
            if dog.happiness <= 0:
                print("Your pet died because you are a terrible person and you broke it's heart.")
                break
            if dog.happiness >= 100:
                print("You have achieved maximum pet happiness. \nCongratulations, you win!")
                break
            if dog.fatness > 80 and dog.fatness < 100:
                print(f"{dog.name} has gotten too fat! {dog.name} needs to exercise!\n")
            if dog.fatness >= 100:
                print(f"{dog.name} has had a heart attack and died. Next time exercise your pet!")
                break
        elif pet_choice == 2:
            if choice == 1:
                cat.play_pet()
                cat.stay_alive()
            elif choice == 2:
                cat.feed_pet()
                cat.stay_alive()
            elif choice == 3:
                cat.get_status()
            elif choice == 4:
                cat.ignore_pet()
                cat.stay_alive()
            elif choice == 5:
                cat.give_toy()
                cat.stay_alive()
            elif choice == 6:
                cat.snuggle()
                cat.stay_alive()
            elif choice == 7:
                cat.exercise()
                cat.stay_alive()
            elif choice == 8:
                cat.treat()
                cat.stay_alive()
            elif choice == 9:
                print("You abandoned your pet. Shortly after, you were hit by a bus and sent to hell.")
                break
            else:
                print("Please choose the correct option.")
            if cat.sadness >= 100:
                print("Your pet died because you are a terrible person and you broke it's heart.")
                break
            if cat.fullness <= 0:
                print("Your pet died because it starved to death. You suck!")
                break
            if cat.happiness <= 0:
                print("Your pet died because you are a terrible person and you broke it's heart.")
                break
            if cat.happiness >= 100:
                print("You have achieved maximum pet happiness. \nCongratulations, you win!")
                break
            if cat.fatness > 80 and cat.fatness < 100:
                print(f"{cat.name} has gotten too fat! {cat.name} needs to exercise!\n")
            if cat.fatness >= 100:
                print(f"{cat.name} has had a heart attack and died. Next time exercise your pet!")
                break
        elif pet_choice == 3:
            if choice == 1:
                turtle.play_pet()
                turtle.stay_alive()
            elif choice == 2:
                turtle.feed_pet()
                turtle.stay_alive()
            elif choice == 3:
                turtle.get_status()
            elif choice == 4:
                turtle.ignore_pet()
                turtle.stay_alive()
            elif choice == 5:
                turtle.give_toy()
                turtle.stay_alive()
            elif choice == 6:
                turtle.snuggle()
                turtle.stay_alive()
            elif choice == 7:
                turtle.exercise()
                turtle.stay_alive()
            elif choice == 8:
                turtle.treat()
                turtle.stay_alive()
            elif choice == 9:
                print("You abandoned your pet. Shortly after, you were hit by a bus and sent to hell.")
                break
            else:
                print("Please choose the correct option.")
            if turtle.sadness >= 100:
                print("Your pet died because you are a terrible person and you broke it's heart.")
                break
            if turtle.fullness <= 0:
                print("Your pet died because it starved to death. You suck!")
                break
            if turtle.happiness <= 0:
                print("Your pet died because you are a terrible person and you broke it's heart.")
                break
            if turtle.happiness >= 100:
                print("You have achieved maximum pet happiness. \nCongratulations, you win!")
                break
            if turtle.fatness > 80 and turtle.fatness < 100:
                print(f"{turtle.name} has gotten too fat! {turtle.name} needs to exercise!\n")
            if turtle.fatness >= 100:
                print(f"{turtle.name} has had a heart attack and died. Next time exercise your pet!")
                break
        elif pet_choice == 4:
            if choice == 1:
                snake.play_pet()
                snake.stay_alive()
            elif choice == 2:
                snake.feed_pet()
                snake.stay_alive()
            elif choice == 3:
                snake.get_status()
            elif choice == 4:
                snake.ignore_pet()
                snake.stay_alive()
            elif choice == 5:
                snake.give_toy()
                snake.stay_alive()
            elif choice == 6:
                snake.snuggle()
                snake.stay_alive()
            elif choice == 7:
                snake.exercise()
                snake.stay_alive()
            elif choice == 8:
                snake.treat()
                snake.stay_alive()
            elif choice == 9:
                print("You abandoned your pet. Shortly after, you were hit by a bus and sent to hell.")
                break
            else:
                print("Please choose the correct option.")
            if snake.sadness >= 100:
                print("Your pet died because you are a terrible person and you broke it's heart.")
                break
            if snake.fullness <= 0:
                print("Your pet died because it starved to death. You suck!")
                break
            if snake.happiness <= 0:
                print("Your pet died because you are a terrible person and you broke it's heart.")
                break
            if snake.happiness >= 100:
                print("You have achieved maximum pet happiness. \nCongratulations, you win!")
                break
            if snake.fatness > 80 and snake.fatness < 100:
                print(f"{snake.name} has gotten too fat! {snake.name} needs to exercise!\n")
            if snake.fatness >= 100:
                print(f"{snake.name} has had a heart attack and died. Next time exercise your pet!")
                break
        elif pet_choice == 5:
            if choice == 1:
                fish.play_pet()
                fish.stay_alive()
            elif choice == 2:
                fish.feed_pet()
                fish.stay_alive()
            elif choice == 3:
                fish.get_status()
            elif choice == 4:
                fish.ignore_pet()
                fish.stay_alive()
            elif choice == 5:
                fish.give_toy()
                fish.stay_alive()
            elif choice == 6:
                fish.snuggle()
                fish.stay_alive()
            elif choice == 7:
                fish.exercise()
                fish.stay_alive()
            elif choice == 8:
                fish.treat()
                fish.stay_alive()
            elif choice == 9:
                print("You abandoned your pet. Shortly after, you were hit by a bus and sent to hell.")
                break
            else:
                print("Please choose the correct option.")
            if fish.sadness >= 100:
                print("Your pet died because you are a terrible person and you broke it's heart.")
                break
            if fish.fullness <= 0:
                print("Your pet died because it starved to death. You suck!")
                break
            if fish.happiness <= 0:
                print("Your pet died because you are a terrible person and you broke it's heart.")
                break
            if fish.happiness >= 100:
                print("You have achieved maximum pet happiness. \nCongratulations, you win!")
                break
            if fish.fatness > 80 and fish.fatness < 100:
                print(f"{fish.name} has gotten too fat! {fish.name} needs to exercise!\n")
            if fish.fatness >= 100:
                print(f"{fish.name} has had a heart attack and died. Next time exercise your pet!")
                break
        elif pet_choice == 6:
            if choice == 1:
                bird.play_pet()
                bird.stay_alive()
            elif choice == 2:
                bird.feed_pet()
                bird.stay_alive()
            elif choice == 3:
                bird.get_status()
            elif choice == 4:
                bird.ignore_pet()
                bird.stay_alive()
            elif choice == 5:
                bird.give_toy()
                bird.stay_alive()
            elif choice == 6:
                bird.snuggle()
                bird.stay_alive()
            elif choice == 7:
                bird.exercise()
                bird.stay_alive()
            elif choice == 8:
                bird.treat()
                bird.stay_alive()
            elif choice == 9:
                print("You abandoned your pet. Shortly after, you were hit by a bus and sent to hell.")
                break
            else:
                print("Please choose the correct option.")
            if bird.sadness >= 100:
                print("Your pet died because you are a terrible person and you broke it's heart.")
                break
            if bird.fullness <= 0:
                print("Your pet died because it starved to death. You suck!")
                break
            if bird.happiness <= 0:
                print("Your pet died because you are a terrible person and you broke it's heart.")
                break
            if bird.happiness >= 100:
                print("You have achieved maximum pet happiness. \nCongratulations, you win!")
                break
            if bird.fatness > 80 and bird.fatness < 100:
                print(f"{bird.name} has gotten too fat! {bird.name} needs to exercise!\n")
            if bird.fatness >= 100:
                print(f"{bird.name} has had a heart attack and died. Next time exercise your pet!")
                break
        else:
            print("Pick the a pet.")
        
dog = Pet("Beetlejuice", 60, 50, 0, 25)
cat = Pet("Meow ZeDong", 60, 45, -1, 15)
turtle = Pet("Leonardo", 60, 45, 1, 10)
snake = Pet("Fluffy", 60, 50, 5, 5)
fish = Pet("Jaws", 60, 60, 5, 0)
bird = Pet("Frank", 60, 45, 3, 0)

pet_choice = int(input("""
Please choose an animal.
1 - Dog
2 - Cat
3 - Turtle
4 - Snake
5 - Fish
6 - Bird
Choice: """))

main()

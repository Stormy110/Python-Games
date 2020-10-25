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

        # if pet_choice == 1:
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
            print("You abandoned your pet like a monster. You spend the rest of your life miserable and alone!")
            break
        else:
            print("Please choose the correct option.")
        if pet.sadness > 80 and pet.sadness < 100:
            print(f"{pet.name} is very sad. Please cheer them up!\n")
        if pet.sadness >= 100:
            print("Your pet died because you are a terrible person and you broke it's heart.")
            break
        if pet.fullness < 20 and pet.fullness > 0:
            print(f"{pet.name} is starving! Feed {pet.name} immediately!\n")
        if pet.fullness <= 0:
            print(f"""
            {pet.name} is starving to death!
            {pet.name} eats you!
            Your fucking dead!
            """)
            break
        if pet.happiness < 20 and pet.happiness > 0:
            print(f"{pet.name} is very sad. Please cheer them up!\n")
        if pet.happiness <= 0:
            print("Your pet ran away because you are a terrible person and nobody will ever love you.")
            break
        if pet.happiness >= 150:
            print("You have achieved maximum pet happiness. \nCongratulations, you win!")
            break
        if pet.fatness > 80 and pet.fatness < 100:
            print(f"{pet.name} has gotten too fat! {pet.name} needs to exercise!\n")
        if pet.fatness >= 100 or pet.fullness >= 100:
            print(f"{pet.name} has had a heart attack and died. Next time exercise your pet!")
            break
        if pet.boredom > 80 and pet.boredom < 100:
            print(f"{pet.name} is very bored. They are thinking about running away from your boring ass.\n")
        if pet.boredom >= 100:
            print(f"{pet.name} ran away from you because you are a boring person.")
            break
        # elif pet_choice == 2:
        #     if choice == 1:
        #         cat.play_pet()
        #         cat.stay_alive()
        #     elif choice == 2:
        #         cat.feed_pet()
        #         cat.stay_alive()
        #     elif choice == 3:
        #         cat.get_status()
        #     elif choice == 4:
        #         cat.ignore_pet()
        #         cat.stay_alive()
        #     elif choice == 5:
        #         cat.give_toy()
        #         cat.stay_alive()
        #     elif choice == 6:
        #         cat.snuggle()
        #         cat.stay_alive()
        #     elif choice == 7:
        #         cat.exercise()
        #         cat.stay_alive()
        #     elif choice == 8:
        #         cat.treat()
        #         cat.stay_alive()
        #     elif choice == 9:
        #         cat.speak()
        #         cat.stay_alive()
        #     elif choice == 10:
        #         print("You abandoned your pet like a monster. You spend the rest of your life miserable and alone!")
        #         break
        #     else:
        #         print("Please choose the correct option.")
        #     if cat.sadness > 80 and cat.sadness < 100:
        #         print(f"{cat.name} is very sad. Please cheer them up!\n")
        #     if cat.sadness >= 100:
        #         print("Your pet died because you are a terrible person and you broke it's heart.")
        #         break
        #     if cat.fullness < 20 and cat.fullness > 0:
        #         print(f"{cat.name} is starving! Feed {cat.name} immediately!\n")
        #     if cat.fullness <= 0:
        #         print(f"""
        #         {cat.name} is starving to death!
        #         {cat.name} waits for you to fall asleep and then visciously attacks and eats you!
        #         You got eaten by your fucking cat!
        #         """)
        #         break
        #     if cat.happiness < 20 and cat.happiness > 0:
        #         print(f"{cat.name} is very sad. Please cheer them up!\n")
        #     if cat.happiness <= 0:
        #         print("Your pet died because you are a terrible person and you broke it's heart.")
        #         break
        #     if cat.happiness >= 150:
        #         print("You have achieved maximum pet happiness. \nCongratulations, you win!")
        #         break
        #     if cat.fatness > 80 and cat.fatness < 100:
        #         print(f"{cat.name} has gotten too fat! {cat.name} needs to exercise!\n")
        #     if cat.fatness >= 100 or cat.fullness >= 100:
        #         print(f"{cat.name} has had a heart attack and died. Next time exercise your pet!")
        #         break
        #     if cat.boredom > 80 and cat.boredom < 100:
        #         print(f"{cat.name} is very bored. They are thinking about running away from your boring ass.\n")
        #     if cat.boredom >= 100:
        #         print(f"{cat.name} ran away from you because you are a boring person.")
        #         break
        # elif pet_choice == 3:
        #     if choice == 1:
        #         turtle.play_pet()
        #         turtle.stay_alive()
        #     elif choice == 2:
        #         turtle.feed_pet()
        #         turtle.stay_alive()
        #     elif choice == 3:
        #         turtle.get_status()
        #     elif choice == 4:
        #         turtle.ignore_pet()
        #         turtle.stay_alive()
        #     elif choice == 5:
        #         turtle.give_toy()
        #         turtle.stay_alive()
        #     elif choice == 6:
        #         turtle.snuggle()
        #         turtle.stay_alive()
        #     elif choice == 7:
        #         turtle.exercise()
        #         turtle.stay_alive()
        #     elif choice == 8:
        #         turtle.treat()
        #         turtle.stay_alive()
        #     elif choice == 9:
        #         turtle.speak()
        #         turtle.stay_alive()
        #     elif choice == 10:
        #         print("You abandoned your pet like a monster. You spend the rest of your life miserable and alone!")
        #         break
        #     else:
        #         print("Please choose the correct option.")
        #     if turtle.sadness > 80 and turtle.sadness < 100:
        #         print(f"{turtle.name} is very sad. Please cheer them up!\n")
        #     if turtle.sadness >= 100:
        #         print("Your pet died because you are a terrible person and you broke it's heart.")
        #         break
        #     if turtle.fullness < 20 and turtle.fullness > 0:
        #         print(f"{turtle.name} is starving! Feed {turtle.name} immediately!\n")
        #     if turtle.fullness <= 0:
        #         print(f"""
        #         {turtle.name} is starving to death!
        #         {turtle.name} breaks out of his cage, kicks you in the face and fucking eats you!
        #         You got eaten by a fucking turtle!
        #         """)
        #         break
        #     if turtle.happiness < 20 and turtle.happiness > 0:
        #         print(f"{turtle.name} is very sad. Please cheer them up!\n")
        #     if turtle.happiness <= 0:
        #         print("Your pet died because you are a terrible person and you broke it's heart.")
        #         break
        #     if turtle.happiness >= 150:
        #         print("You have achieved maximum pet happiness. \nCongratulations, you win!")
        #         break
        #     if turtle.fatness > 80 and turtle.fatness < 100:
        #         print(f"{turtle.name} has gotten too fat! {turtle.name} needs to exercise!\n")
        #     if turtle.fatness >= 100 or turtle.fullness >= 100:
        #         print(f"{turtle.name} has had a heart attack and died. Next time exercise your pet!")
        #         break
        #     if turtle.boredom > 80 and turtle.boredom < 100:
        #         print(f"{turtle.name} is very bored. They are thinking about running away from your boring ass.\n")
        #     if turtle.boredom >= 100:
        #         print(f"{turtle.name} ran away from you because you are a boring person.")
        #         break
        # elif pet_choice == 4:
        #     if choice == 1:
        #         snake.play_pet()
        #         snake.stay_alive()
        #     elif choice == 2:
        #         snake.feed_pet()
        #         snake.stay_alive()
        #     elif choice == 3:
        #         snake.get_status()
        #     elif choice == 4:
        #         snake.ignore_pet()
        #         snake.stay_alive()
        #     elif choice == 5:
        #         snake.give_toy()
        #         snake.stay_alive()
        #     elif choice == 6:
        #         snake.snuggle()
        #         snake.stay_alive()
        #     elif choice == 7:
        #         snake.exercise()
        #         snake.stay_alive()
        #     elif choice == 8:
        #         snake.treat()
        #         snake.stay_alive()
        #     elif choice == 9:
        #         snake.speak()
        #         snake.stay_alive()
        #     elif choice == 10:
        #         print("You abandoned your pet like a monster. You spend the rest of your life miserable and alone!")
        #         break
        #     else:
        #         print("Please choose the correct option.")
        #     if snake.sadness > 80 and snake.sadness < 100:
        #         print(f"{snake.name} is very sad. Please cheer them up!\n")
        #     if snake.sadness >= 100:
        #         print("Your pet died because you are a terrible person and you broke it's heart.")
        #         break
        #     if snake.fullness < 20 and snake.fullness > 0:
        #         print(f"{snake.name} is starving! Feed {snake.name} immediately!\n")
        #     if snake.fullness <= 0:
        #         print(f"""
        #         {snake.name} is starving to death!
        #         {snake.name} breaks out of his cage and eats you!
        #         You got eaten by a fucking snake!
        #         """)
        #         break
        #     if snake.happiness < 20 and snake.happiness > 0:
        #         print(f"{snake.name} is very sad. Please cheer them up!\n")
        #     if snake.happiness <= 0:
        #         print("Your pet died because you are a terrible person and you broke it's heart.")
        #         break
        #     if snake.happiness >= 150:
        #         print("You have achieved maximum pet happiness. \nCongratulations, you win!")
        #         break
        #     if snake.fatness > 80 and snake.fatness < 100:
        #         print(f"{snake.name} has gotten too fat! {snake.name} needs to exercise!\n")
        #     if snake.fatness >= 100 or snake.fullness >= 100:
        #         print(f"{snake.name} has had a heart attack and died. Next time exercise your pet!")
        #         break
        #     if snake.boredom > 80 and snake.boredom < 100:
        #         print(f"{snake.name} is very bored. They are thinking about running away from your boring ass.\n")
        #     if snake.boredom >= 100:
        #         print(f"{snake.name} ran away from you because you are a boring person.")
        #         break
        # elif pet_choice == 5:
        #     if choice == 1:
        #         fish.play_pet()
        #         fish.stay_alive()
        #     elif choice == 2:
        #         fish.feed_pet()
        #         fish.stay_alive()
        #     elif choice == 3:
        #         fish.get_status()
        #     elif choice == 4:
        #         fish.ignore_pet()
        #         fish.stay_alive()
        #     elif choice == 5:
        #         fish.give_toy()
        #         fish.stay_alive()
        #     elif choice == 6:
        #         fish.snuggle()
        #         fish.stay_alive()
        #     elif choice == 7:
        #         fish.exercise()
        #         fish.stay_alive()
        #     elif choice == 8:
        #         fish.treat()
        #         fish.stay_alive()
        #     elif choice == 9:
        #         fish.speak()
        #         fish.stay_alive()
        #     elif choice == 10:
        #         print("You abandoned your pet like a monster. You spend the rest of your life miserable and alone!")
        #         break
        #     else:
        #         print("Please choose the correct option.")
        #     if fish.sadness > 80 and fish.sadness < 100:
        #         print(f"{fish.name} is very sad. Please cheer them up!\n")
        #     if fish.sadness >= 100:
        #         print("Your pet died because you are a terrible person and you broke it's heart.")
        #         break
        #     if fish.fullness < 20 and fish.fullness > 0:
        #         print(f"{fish.name} is starving! Feed {fish.name} immediately!\n")
        #     if fish.fullness <= 0:
        #         print(f"""
        #         {fish.name} was starving to death!
        #         {fish.name} jumped out of his bowl and ate you!
        #         You got eaten by a fucking goldfish.
        #         """)
        #         break
        #     if fish.happiness <= 0:
        #         print("Your pet died because you are a terrible person and you broke it's heart.")
        #         break
        #     if fish.happiness < 20 and fish.happiness > 0:
        #         print(f"{fish.name} is very sad. Please cheer them up!\n")
        #     if fish.happiness >= 150:
        #         print("You have achieved maximum pet happiness. \nCongratulations, you win!")
        #         break
        #     if fish.fatness > 80 and fish.fatness < 100:
        #         print(f"{fish.name} has gotten too fat! {fish.name} needs to exercise!\n")
        #     if fish.fatness >= 100 or fish.fullness >= 100:
        #         print(f"{fish.name} has had a heart attack and died. Next time exercise your pet!")
        #         break
        #     if fish.boredom > 80 and fish.boredom < 100:
        #         print(f"{fish.name} is very bored. They are thinking about running away from your boring ass.\n")
        #     if fish.boredom >= 100:
        #         print(f"{fish.name} ran away from you because you are a boring person.")
        #         break
        # elif pet_choice == 6:
        #     if choice == 1:
        #         bird.play_pet()
        #         bird.stay_alive()
        #     elif choice == 2:
        #         bird.feed_pet()
        #         bird.stay_alive()
        #     elif choice == 3:
        #         bird.get_status()
        #     elif choice == 4:
        #         bird.ignore_pet()
        #         bird.stay_alive()
        #     elif choice == 5:
        #         bird.give_toy()
        #         bird.stay_alive()
        #     elif choice == 6:
        #         bird.snuggle()
        #         bird.stay_alive()
        #     elif choice == 7:
        #         bird.exercise()
        #         bird.stay_alive()
        #     elif choice == 8:
        #         bird.treat()
        #         bird.stay_alive()
        #     elif choice == 9:
        #         bird.speak()
        #         bird.stay_alive()
        #     elif choice == 10:
        #         print("YYou abandoned your pet like a monster. You spend the rest of your life miserable and alone!")
        #         break
        #     else:
        #         print("Please choose the correct option.")
        #     if bird.sadness > 80 and bird.sadness < 100:
        #         print(f"{bird.name} is very sad. Please cheer them up!\n")
        #     if bird.sadness >= 100:
        #         print("Your pet died because you are a terrible person and you broke it's heart.")
        #         break
        #     if bird.fullness < 20 and bird.fullness > 0:
        #         print(f"{bird.name} is starving! Feed {bird.name} immediately!\n")
        #     if bird.fullness <= 0:
        #         print(f"""
        #         {bird.name} was starving to death!
        #         {bird.name} broke out of it's cage and ate you!
        #         You got eaten by a fucking parakeet.
        #         """)
        #         break
        #     if bird.happiness < 20 and bird.happiness > 0:
        #         print(f"{bird.name} is very sad. Please cheer them up!\n")
        #     if bird.happiness <= 0:
        #         print("Your pet died because you are a terrible person and you broke it's heart.")
        #         break
        #     if bird.happiness >= 150:
        #         print("You have achieved maximum pet happiness. \nCongratulations, you win!")
        #         break
        #     if bird.fatness > 80 and bird.fatness < 100 :
        #         print(f"{bird.name} has gotten too fat! {bird.name} needs to exercise!\n")
        #     if bird.fatness >= 100 or bird.fullness >= 100:
        #         print(f"{bird.name} has had a heart attack and died. Next time exercise your pet!")
        #         break
        #     if bird.boredom > 80 and bird.boredom < 100:
        #         print(f"{bird.name} is very bored. They are thinking about running away from your boring ass.\n")
        #     if bird.boredom >= 100:
        #         print(f"{bird.name} ran away from you because you are a boring person.")
        #         break
        else:
            print("Pick a pet.")
        
dog = Pet("Beetlejuice", 60, 55, 0, 25)
cat = Pet("Meow ZeDong", 60, 50, -1, 15)
turtle = Pet("Leonardo", 60, 50, 1, 40)
snake = Pet("Fluffy", 60, 50, 5, 25)
fish = Pet("Jaws", 60, 50, 55, 20)
bird = Pet("Frank", 60, 50, 3, 20)


pet_choice = int(input("""
Please choose an animal.
1 - Dog
2 - Cat
3 - Turtle
4 - Snake
5 - Fish
6 - Bird
Choice: """))


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
else:
    print("\nYou did not choose a pet.\n")
    
main()


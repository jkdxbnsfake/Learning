import random

print("Welcome to Hangman !")

movies_list = ["Inception", "The Avengers", "The Dhoom"]
chosen_movie_name = list(str(random.choice(movies_list)).lower())
#print(chosen_movie_name)
print("\n")

new_list =["_" for x in range(len(chosen_movie_name))]
end_of_game = False................

while not end_of_game:
    user_guess = input("What letters do you think the movie name has ?\t")
    for n in range(0, len(chosen_movie_name)):
        if chosen_movie_name[n] == " ":
            new_list[n] = " "
        elif user_guess == chosen_movie_name[n]:
            new_list[n] = user_guess

    print(f"movie name is : {(''.join(new_list)).capitalize()}")
    print("\n")
    if "_" in list(new_list):
        end_of_game = False
    elif "_" not in list(new_list):
        end_of_game = True

print("CONGRATULATIONS ,YOU HAVE WON !")


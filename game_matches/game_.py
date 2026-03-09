import time

import numpy as np
import random
global_array_for_game = np.ones((15,3))
award = 0.5
punish = -1.5
system_win_number = 0
user_win_number = 0

#Funkcje
def user_move(x):
    user_choice = random.randint(1, min(3, x))
    new_global_count = x - user_choice
    return new_global_count, user_choice

def system_move(y):
    max_choice = min(3, y) #To trzeba poprawić
    if (np.argmax((global_array_for_game[y - 1]),axis=0)) + 1 == 1:
        system_choose_matches = 1
    if (np.argmax((global_array_for_game[y - 1]), axis=0)) + 1 == 2:
        system_choose_matches = 2
    if (np.argmax((global_array_for_game[y - 1]), axis=0)) + 1 == 3:
        system_choose_matches = 3
    new_global_count = y - system_choose_matches
    new_list_with_system_choice.append(tuple([y, system_choose_matches]))
    return new_global_count, system_choose_matches

for game_number in range(1000):
    game_count = global_array_for_game.shape[0]
    new_list_with_system_choice = list()
    system_win = False
    game_tour = 1


    #Do momentu kiedy zapałek jest więcej niż 0
    while game_count > 0:
        print(f"---- GRA NUMER {game_number} ------")
        print(f"---- Tura {game_tour} -----")
        print(f"Aktualny stan zapałek: {game_count}")
        print("--------------------")

        #Ruch użytkownika:
        game_count, user_choice = user_move(game_count)
        print(f"Użytkownik wybrał: {user_choice}")

        #Sprawdź czy użytkownik zakończył grę
        if game_count == 0:
            #print("Użytkownik wygrał, przegrał system")
            system_win = False
            user_win_number+=1
            break
        if game_count < 0:
           #print("Użytkownik przegrał, wygrał system")
            system_win = True
            system_win_number+=1
            break

        #Ruch systemu:
        game_count, number_of_matches = system_move(game_count)
        print(f"System wybrał: {number_of_matches} \n")

        # Sprawdź czy system zakończył grę
        if game_count == 0:
            #print("System wygrał, użytkownik przegrał")
            system_win = True
            system_win_number+=1
            break
        if game_count < 0:
           #print("System przegrał, użytkownik wygrał")
            system_win = False
            user_win_number+=1
            break
        #Zlicze tury
        game_tour+=1

    print(f"Ruchy systemu: {new_list_with_system_choice}")
    print("--------------------"'\n')
    print(global_array_for_game)

    for number_of_matches, choice in new_list_with_system_choice:
        if system_win:
            global_array_for_game[number_of_matches - 1][choice - 1] += award
        else:
            global_array_for_game[number_of_matches - 1][choice - 1] += punish
    print("--------------------")
    print(f"Wygrana użytkownika: {user_win_number}")
    print("--------------------")
    print(f"Wygrana systemu: {system_win_number}")
    print("--------------------"'\n')








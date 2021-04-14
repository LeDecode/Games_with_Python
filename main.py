import copy

pavizdys = [[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],["-", "-", "-","|","-", "-", "-","|","-", "-", "-"],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],["-", "-", "-","|","-", "-", "-","|","-", "-", "-"],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "]]
tiktaktoe = [[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],["-", "-", "-","|","-", "-", "-","|","-", "-", "-"],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],["-", "-", "-","|","-", "-", "-","|","-", "-", "-"],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "]]
destroy = [[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],["-", "-", "-","|","-", "-", "-","|","-", "-", "-"],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],["-", "-", "-","|","-", "-", "-","|","-", "-", "-"],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "],[" ", " ", " ","|"," ", " ", " ","|"," ", " ", " "]]
sulauzytas = []
pavizdys[1][1] = "7"
pavizdys[1][5] = "8"
pavizdys[1][9] = "9"
pavizdys[5][1] = "4"
pavizdys[5][5] = "5"
pavizdys[5][9] = "6"
pavizdys[9][1] = "1"
pavizdys[9][5] = "2"
pavizdys[9][9] = "3"

def display(row1):
    for n in row1:
        listToStr = (' '.join([str(elem) for elem in n]))
        print(listToStr)
def user_choice(empty_placement):
    choice = "Nepasirinkote skaiciaus"
    acceptable_range = range(1, 10)
    within_range = False
    tuscia_vieta = False
    while choice.isdigit() == False or within_range == False or tuscia_vieta == False:
        choice = input("Pasirinkite vieta klaviaturoje :")
        if choice.isdigit() == False:
            print("Kazkur ne ten paspaudete")
        if choice.isdigit() == True:
           if int(choice) == 0 or int(choice) > 9:
               print("Tikriausiai paspaudete 0 arba du kartus, pabandykite dar karta")
           if int(choice) in acceptable_range:
                within_range = True
                choose = int(choice)-1
                if empty_placement[choose] == " ":
                    tuscia_vieta = True
                else:
                    print("Kaip matote cia jau yra zenkliukas")
    return int(choice)
def rewriteX (sulauzytas, user_input):
    game_table = sulauzytas
    if user_input == 7:
        game_table[1][1] = "X"
    if user_input == 8:
        game_table[1][5] = "X"
    if user_input == 9:
        game_table[1][9] = "X"
    if user_input == 4:
        game_table[5][1] = "X"
    if user_input == 5:
        game_table[5][5] = "X"
    if user_input == 6:
        game_table[5][9] = "X"
    if user_input == 1:
        game_table[9][1] = "X"
    if user_input == 2:
        game_table[9][5] = "X"
    if user_input == 3:
        game_table[9][9] = "X"
    return game_table
def rewriteO (sulauzytas, user_input):
    game_table = sulauzytas
    if user_input == 7:
        game_table[1][1] = "O"
    if user_input == 8:
        game_table[1][5] = "O"
    if user_input == 9:
        game_table[1][9] = "O"
    if user_input == 4:
        game_table[5][1] = "O"
    if user_input == 5:
        game_table[5][5] = "O"
    if user_input == 6:
        game_table[5][9] = "O"
    if user_input == 1:
        game_table[9][1] = "O"
    if user_input == 2:
        game_table[9][5] = "O"
    if user_input == 3:
        game_table[9][9] = "O"
    return game_table
def check_if_winner(tiktaktoe):
    if (tiktaktoe[1][1] == tiktaktoe[1][5] == tiktaktoe[1][9]) and tiktaktoe[1][9] != " ":
        print("Congratulations you have won!")
        return False
    if tiktaktoe[5][1] == tiktaktoe[5][5] == tiktaktoe[5][9] and tiktaktoe[5][9] != " ":
        print("Congratulations you have won!")
        return False
    if tiktaktoe[9][1] == tiktaktoe[9][5] == tiktaktoe[9][9] and tiktaktoe[9][9] != " ":
        print("Congratulations you have won!")
        return False
    if tiktaktoe[1][1] == tiktaktoe[5][1] == tiktaktoe[9][1] and tiktaktoe[9][1] != " ":
        print("Congratulations you have won!")
        return False
    if tiktaktoe[1][5] == tiktaktoe[5][5] == tiktaktoe[9][5] and tiktaktoe[9][5] != " ":
        print("Congratulations you have won!")
        return False
    if tiktaktoe[1][9] == tiktaktoe[5][9] == tiktaktoe[9][9] and tiktaktoe[9][9] != " ":
        print("Congratulations you have won!")
        return False
    if tiktaktoe[1][1] == tiktaktoe[5][5] == tiktaktoe[9][9] and tiktaktoe[9][9] != " ":
        print("Congratulations you have won!")
        return False
    if tiktaktoe[1][9] == tiktaktoe[5][5] == tiktaktoe[9][1] and tiktaktoe[9][1] != " ":
        print("Congratulations you have won!")
        return False
    else:
        return True
def play_again():
    taip_arba_ne = ["Y", "y", "n", "N"]
    user_input = "belekas"
    while user_input not in taip_arba_ne:
        user_input = input("Do you want to play again? (Y/N)")
        if user_input == "Y" or user_input == "y":
            return True
        elif user_input == "N" or user_input == "n":
            return False
        else:
            print("Kazka ne ta paspaudet")

sulauzytas = copy.deepcopy(destroy)
empty_placement = [sulauzytas[9][1],sulauzytas[9][5],sulauzytas[9][9],sulauzytas[5][1],sulauzytas[5][5],sulauzytas[5][9],sulauzytas[1][1],sulauzytas[1][5],sulauzytas[1][9]]
game_continue = True
game_is_on = True
while game_continue == True:
    if game_is_on == False:
        display(sulauzytas)
        sulauzytas.clear()
        sulauzytas = copy.deepcopy(destroy)
        empty_placement = [sulauzytas[9][1], sulauzytas[9][5], sulauzytas[9][9], sulauzytas[5][1], sulauzytas[5][5], sulauzytas[5][9], sulauzytas[1][1], sulauzytas[1][5], sulauzytas[1][9]]
        game_is_on = play_again()
        game_continue = game_is_on

    else:
        while game_is_on == True:
            if game_is_on is not False:
                display(sulauzytas)
                pasirinkimas = user_choice(empty_placement)
                sulauzytas = rewriteX(sulauzytas, pasirinkimas)
                empty_placement = [sulauzytas[9][1], sulauzytas[9][5], sulauzytas[9][9], sulauzytas[5][1], sulauzytas[5][5],sulauzytas[5][9], sulauzytas[1][1], sulauzytas[1][5], sulauzytas[1][9]]
                game_is_on = check_if_winner(sulauzytas)
            if game_is_on is not False:
                display(sulauzytas)
                pasirinkimas = user_choice(empty_placement)
                sulauzytas = rewriteO(sulauzytas, pasirinkimas)
                empty_placement = [sulauzytas[9][1], sulauzytas[9][5], sulauzytas[9][9], sulauzytas[5][1], sulauzytas[5][5],sulauzytas[5][9], sulauzytas[1][1], sulauzytas[1][5], sulauzytas[1][9]]
                game_is_on = check_if_winner(sulauzytas)
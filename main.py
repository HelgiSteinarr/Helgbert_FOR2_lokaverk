# Helgi Steinarr Júlíusson <-> 081200-3270  |  Albert Elías Arason <-> 140600-3180
import csv
from random import randint, shuffle
from time import sleep

# ------------------------Info--------------------------#
__copyright__ = "WTFPL - http://www.wtfpl.net/about/"
__credit__ = ["Helgi", "Albert"]
# ------------------------------------------------------#


def test_if_number(text, float_or_int):
    # Function that tests if the value entered is a number or not.
    while True:
        try:
            # If the input gets an error (e.g. string entered) the code will stop and "return" wont run.
            question = float_or_int(input(text))
            return question
        except ValueError:
            # When the code stops "except" will run and tells the user to try again and there it loops again.
            print("Ekki tala... Reyndu aftur..")


def run_again():
    # Function that asks the user if he wants to run the just executed code again
    yes_list = ["ja", "já", "jamm", "j", "jam", "y", "ye", "yes", "ya", "mhm", "yep"]  # Both Icelandic and English
    no_list = ["nei", "ne", "na", "n", "no", "huh", "nje", "nah", "nop", "nope"]  # Both Icelandic and English
    while True:
        question = input("\nViltu keyra forritið aftur?[J/N]: ")
        # The code checks if the entered value is in one of the lists and return either 1 or 0 depending on the results.
        if question.lower() in yes_list:
            p_nr = 1
            return p_nr
        elif question.lower() in no_list:
            p_nr = 0
            return p_nr
        else:
            print("Skil þig ekki...")


def distribute_cards():
    # Function that opens the file with the card data and distributes it between the players
    # We open the file with all the card data here
    with open("cards.txt", "r", encoding='utf8') as file:
        card_list = []
        # We use the csv library to make a list out of every line in the file
        data = csv.reader(file, delimiter=";")
        for card in data:
            if len(card) != 9:
                # Tests if the card it found is correct in the file
                print("VILLA Í GÖGNUM", card)
            # Here we turn the needed strings into float values
            formatted_data = [card[0], float(card[1]), float(card[2]), float(card[3]), float(card[4]), float(card[5]),
                              float(card[6]), float(card[7]), float(card[8])]
            card_list.append(formatted_data)

        # shuffle is a function from the random library that mixes up the order in the list
        shuffle(card_list)

        nr_cards_a_person = len(card_list) // 2

        # From the first up to the max a person
        player1 = card_list[0:nr_cards_a_person]
        # From the max a person to the end
        player2 = card_list[nr_cards_a_person:nr_cards_a_person * 2]

        return player1, player2

p1, p2 = distribute_cards()


def select_category():
    # Function that shows the user the values on his top card and makes him select what category to play in
    cat_name_list = ["Nafn: ", "1. Þyngd:", "2. Mjólkurlagni dætra:", "3. Einkunn ullar:", "4. Fjöldi Afkvæma:",
                     "5. Einkunn læris:", "6. Frjósemi:", "7. Gerð bakvöðva:", "8. Einkunn fyrir malir:"]
    for i in range(len(cat_name_list)):
        # Prints the category name with the value after it
        print(cat_name_list[i], p1[0][i])
    cat = test_if_number("Sláðu inn nr flokksins[1-8]: ", int)
    if 0 < cat > 9:
        print("Þessi tala er ekki frá 1-8..")
        select_category()  # Runs the function again
    return cat


def cp_select_category():
    # Selects what category the computer (cp) is going to play in
    cp_cat = randint(1, 8)
    return cp_cat

temp_storage = []  # List that stores the cards when a tie happens


def compare_cards(cat):
    # Function that compares the user's top card with the computers (cp) card
    print("Ber", p1[0][cat], "saman við", p2[0][cat])
    if p1[0][cat] > p2[0][cat]:
        # If the user wins ↓
        p1.append(p2[0])  # Adds the opponent's card into the back of the user's deck
        p2.pop(0)   # Pop's the same card out of the opponent's deck
        p1.append(p1.pop(0))  # pops the top card and appends it back into the back
        print("Þú vannst þessa umferð og þú fékkst spil tölvunnar")
        if len(temp_storage) > 0:
            # Checks if there are cards in the temporary storage for the cards that were tied
            for card in temp_storage:
                p1.append(card)  # Appends the cards into the back of the user's deck
                for i in range(len(temp_storage)):
                    temp_storage.pop(0)  # pops the cards out of the temp list
    elif p2[0][cat] > p1[0][cat]:
        # If the Computer (cp) wins ↓
        p2.append(p1[0])
        p1.pop(0)
        p2.append(p2.pop(0))
        # All of this is explained where the user wins ↑
        print("Talvan vann í þessari umferð og fékk spilið þitt")
        if len(temp_storage) > 0:
            for card in temp_storage:
                p2.append(card)
                for i in range(len(temp_storage)):
                    temp_storage.pop(0)
    else:
        print("Tölurnar voru jafn háar \nSá sem vinnur næstu umferð fær jafnteflisspilin úr þessari umferð")
        temp_storage.append(p1[0])  # Appends the top cards into the temporary card storage list
        temp_storage.append(p2[0])
        p1.pop(0)  # pops the top cards out of both decks
        p2.pop(0)

main_bool = 1
while main_bool == 1:
    # Main loop that runs the functions in the right order
    print("\n" + "#" * 18 + "\n# Umferð Spilara #\n" + "#"*18)
    cat = select_category()
    # Sleep from the time library adds delay so the data displayed is readable
    sleep(1)
    compare_cards(cat)
    sleep(1)
    print("spilafjöldi í stokkum:", "\nSpilari:", len(p1), "\nTalvan:", len(p2))
    sleep(1)
    print("\n" + "#" * 16 + "\n# Umferð Tölvu #\n" + "#" * 16)
    cp_cat = cp_select_category()
    sleep(1)
    compare_cards(cp_cat)
    sleep(1)
    print("spilafjöldi í stokkum:", "\nSpilari:", len(p1), "\nTalvan:", len(p2))
    sleep(1)
    if len(p1) <= 0:
        print("Þú hefur tapað :(")
        main_bool = run_again()  # Function that asks if the user want's to play again
    if len(p2) <= 0:
        print("Þú hefur unnið :)")
        main_bool = run_again()  # Function that asks if the user want's to play again

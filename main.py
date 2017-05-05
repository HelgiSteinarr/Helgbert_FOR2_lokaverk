import csv
from random import randint, shuffle
from time import sleep


def test_if_number(text, float_or_int):
    # Function that tests if the value entered is a number or not.
    while True:
        try:
            # If the input gets an error (e.g. string entered) the code will stop and "return" wont run.
            question = float_or_int(input(text))
            return question
        except ValueError:
            # When the code stops "except" will run and tells the user to try again and there it loops again.
            # This way the code wont crash of the user enters something i don't want.
            print("Not a number.. Try again.")


def run_again():
    # Function that asks the user if he wants to run the just executed code again
    yes_list = ["ja", "já", "jamm", "j", "jam", "y", "ye", "yes", "ya", "mhm", "yep"]  # Both Icelandic and English
    no_list = ["nei", "ne", "na", "n", "no", "huh", "nje", "nah", "nop", "nope"]  # Both Icelandic and English
    while True:
        question = input("\nDo you want to run that code again?[Y/N]: ")
        # The code checks if the entered value is in one of the lists and return either 1 or 0 depending on the results.
        if question.lower() in yes_list:
            p_nr = 1
            return p_nr
        elif question.lower() in no_list:
            p_nr = 0
            return p_nr
        else:
            print("Don't understand you...")


def distribute_cards():
    with open("cards.txt", "r") as file:
        card_list = []
        data = csv.reader(file, delimiter=";")
        for card in data:
            if len(card) != 9:
                print("VILLA Í GÖGNUM", card)
            formatted_data = [card[0], float(card[1]), float(card[2]), float(card[3]), float(card[4]), float(card[5]),
                              float(card[6]), float(card[7]), float(card[8])]
            card_list.append(formatted_data)

        shuffle(card_list)

        nr_cards_a_person = len(card_list) // 2

        player1 = card_list[0:nr_cards_a_person]
        player2 = card_list[nr_cards_a_person:nr_cards_a_person * 2]

        return player1, player2

p1, p2 = distribute_cards()


def select_category():
    cat_name_list = ["Nafn: ", "1. Þyngd:", "2. Mjólkurlagni dætra:", "3. Einkunn ullar:", "4. Fjöldi Afkvæma:",
                     "5. Einkunn læris:", "6. Frjósemi:", "7. Gerð bakvöðva:", "8. Einkunn fyrir malir:"]
    for i in range(len(cat_name_list)):
        print(cat_name_list[i], p1[0][i])
    cat = test_if_number("Sláðu inn nr flokksins[1-8]: ", int)
    if 0 < cat > 9:
        print("Þessi tala er ekki frá 1-8..")
        select_category()
    return cat


def cp_select_category():
    cp_cat = randint(1, 8)
    return cp_cat

temp_storage = []


def compare_cards(cat):
    print("Ber", p1[0][cat], "saman við", p2[0][cat])
    if p1[0][cat] > p2[0][cat]:
        p1.append(p2[0])
        p2.pop(0)
        p1.append(p1.pop(0))
        print("Þú vannst þessa umferð og þú fékkst spil tölvunnar")
        if len(temp_storage) > 0:
            for card in temp_storage:
                p1.append(card)
                for i in range(len(temp_storage)):
                    temp_storage.pop(0)
    elif p2[0][cat] > p1[0][cat]:
        p2.append(p1[0])
        p1.pop(0)
        p2.append(p2.pop(0))
        print("Talvan vann í þessari umferð og fékk spilið þitt")
        if len(temp_storage) > 0:
            for card in temp_storage:
                p2.append(card)
                for i in range(len(temp_storage)):
                    print("i", i)
                    print("len t", len(temp_storage))
                    temp_storage.pop(i)
    else:
        print("Tölurnar voru jafn háar \nSá sem vinnur næstu umferð fær jafnteflisspilin úr þessari umferð")
        temp_storage.append(p1[0])
        temp_storage.append(p2[0])
        p1.pop(0)
        p2.pop(0)

main_bool = 1
while main_bool == 1:
    print("\n" + "#" * 18 + "\n# Umferð Spilara #\n" + "#"*18)
    cat = select_category()
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
        main_bool = run_again()
    if len(p2) <= 0:
        print("Þú hefur unnið :)")
        main_bool = run_again()

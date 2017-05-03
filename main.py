import csv
from random import randint


def distribute_cards(player_amount):
    with open("cards.txt", "r") as file:
        card_list = []
        data = csv.reader(file, delimiter="\n")
        for i in data:
            card_list.append(i)
        nr_cards_a_person = len(card_list) // player_amount

        player1 = []
        player2 = []
        # player3 = []
        # player4 = []

        # print("card_list len -", len(card_list) // 2 * 2)
        # print("nr_card_a_person", nr_cards_a_person)

        """
        for i in range(len(card_list) // 2 * 2):

            ran_nr = randint(0,len(card_list) // 2 * 2)
            print("ran:",ran_nr)
            print("nr_ca", nr_cards_a_person)
            print("i =", i)
            if card_list[ran_nr] not in player1 and card_list[ran_nr] not in player2 and i < nr_cards_a_person:
                player1.append(card_list[ran_nr])
            elif card_list[ran_nr] not in player1 and card_list[ran_nr] not in player2 and i > nr_cards_a_person:
                player2.append(card_list[ran_nr])
            elif card_list[ran_nr] in player1 and card_list[ran_nr] in player2:
                test.append(card_list[ran_nr])
        """


        ran0 = 0
        ran1 = 0
        for i in range(len(card_list) // 2 * 2):
            ran = randint(0,1)

            if ran == 0:
                if ran0 >= nr_cards_a_person:
                    player2.append(card_list[i])
                else:
                    player1.append(card_list[i])
                    ran0 += 1

            if ran == 1:
                if ran1 >= nr_cards_a_person :
                    player1.append(card_list[i])
                else:
                    player2.append(card_list[i])
                    ran1 += 1

        both = []
        both.append(player1)
        both.append(player2)
        return both



"""

with open ("sheeptest.txt", "r", encoding="utf-8") as file:
    data = csv.reader(file, delimiter=";")
    for i in data:
        print(i[4])

"""

both = distribute_cards(player_amount=2)
print(both[0])
print(both[1])

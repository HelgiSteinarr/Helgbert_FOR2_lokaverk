

class Card:
    nr_of_rams = 0

    def __init__(self, card_type, name, weight, milk, wool, child_nr, leg_score, fertility, meat, butt_score):
        self.card_type = card_type
        self.name = name
        self.weight = weight
        self.milk = milk
        self.wool = wool
        self.child_nr = child_nr
        self.leg_score = leg_score
        self.fertility = fertility
        self.meat = meat
        self.butt_score = butt_score

        Card.nr_of_rams += 1

    def find_card_data(self):
        pass
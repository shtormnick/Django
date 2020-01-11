from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():

    def __init__(self):
        print("Creating New Order Deck")
        self.allcards = [(s,r) for r in RANKS for s in SUITE]

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return(self.allcards[:26],self.allcards[:26])

class Hand():

    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_cards(self):
        return self.cards.pop()

class Player():

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        dawn_card = self.hand.remove_cards()
        print("{} has placed: {}".format(self.name,dawn_card))
        print('\n')
        return dawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):

        return len(self.hand.cards) != 0


print ("Welcime to War, let's degin...")

#Create new deck and split in half
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

#Create Both Players
comp = Player("Comp",Hand(half1))
name = input("What is your name, player?")
user = Player(name,Hand(half2))

#set round count
total_rounds = 0
war_count = 0
#gameplay
while user.still_has_cards() and comp.still_has_cards():
    total_rounds = 1
    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(user.name+" count: "+str(len(user.hand.cards)))
    print(comp.name+" count: "+str(len(comp.hand.cards)))
    print("Both players play card!")
    print("\n")

    table_cards = []

    c_cards = comp.play_card()
    u_cards = user.play_card()

    table_cards.append(c_cards)
    table_cards.append(u_cards)

    #check war
    if c_cards[1] == u_cards[1]:
        war_count += 1
        print("We hav a match, time for war")
        print("Each plyer removes a 3 cards 'face down'and then one card face up ")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())
        #check rank of cards
        if RANKS.index(c_cards[1]) < RANKS.index(u_cards[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand")
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_cards[1]) < RANKS.index(u_cards[1]):
            print(user.name+" has the higher card, adding to hand")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand")
            comp.hand.add(table_cards)
print("Greate Game, it leasted: "+str(total_rounds))
print("A war accured "+str(war_count)+" times")

import random
values = {"Two": 2, "Three": 3, 'Four': 4, 'Five': 5, "Six": 6, "Seven": 7,
          "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
# Card
# Suit,Rank,Value


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# two_hearts = Card("Hearts", "Two")
# print(two_hearts)
# print(values[two_hearts.rank])


# ? Deck Class

class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # // Create the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)
        # // in place,so it does not return anything

    def deal_one(self):
        return self.all_cards.pop()


# new_deck = Deck()
# first_card = new_deck.all_cards[0]
# last_card = new_deck.all_cards[-1]
# print(first_card)
# print(last_card)
# new_deck.shuffle_deck()

# for card_object in new_deck.all_cards:
#     print(card_object)

# my_card = new_deck.deal_one()
# print(my_card)


class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # // list of multiple card objects
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            # // for a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


# new_player = Player("Hammad")
# print(new_player.add_cards(my_card))
# print(new_player)
# print(new_player.all_cards[-1])
# print(new_player.all_cards[0])
# print(new_player.add_cards([my_card, my_card, my_card]))

# for k in new_player.all_cards:
#     print(k)
# print(new_player)


# // Game Setup
player_one = Player("One")
player_two = Player("Two")
new_deck = Deck()
new_deck.shuffle_deck()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
# ? while game_on
while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One,out of cards !Player Two Wins")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two,out of cards !Player One Wins")
        game_on = False
        break

    # ? Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_one.remove_one())

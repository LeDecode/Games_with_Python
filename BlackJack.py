import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
class Card:
    def __init__(self, suits, rank):
        self.suit = suits
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    def add_cards(self,new_cards):
        self.all_cards.append(new_cards)
    def clear_cards(self):
        self.all_cards.clear()
    def show_card(self):
        print(f"{self.name} got {self.all_cards[-1]}")
    def __str__(self):
        return f" Player:\t\t {self.name}"
class PlayerChips:
    def __init__(self, chips = 0):
        self.chips = chips
    def blackjack (self,instant_win):
        self.chips = self.chips + instant_win*2 + instant_win*0.5
    def chips_won(self, won_chips):
        self.chips = self.chips + won_chips*2
    def bet(self, bet):
        self.chips = self.chips - bet
    def __str__(self):
        return f"Chips left:\t {self.chips}"


player_name = input("What is your name, sir?")
player_money = int(input("How much money would you like to desposit?"))
if player_money > 1000:
    print("Aren't you a little spender?")
print("First of all, don't spend all your money at once! I wish you a good luck!")

player = Player(player_name)
dealer = Player("Dealer")
chips = PlayerChips(player_money)
#adding cards to the player hand

print(player, "\n", chips)
game_on = True
one_more_time = True
while one_more_time:
    new_deck = Deck()
    new_deck.shuffle()
    if game_on is False:
        print(player, "\n", chips)
        will_play = input("Would you like to play again? (Y/N)?")
        if will_play == "Y" or will_play == "y":
            player.clear_cards()
            game_on = True
        else:
            one_more_time = False
    else:
        while game_on:
            betting = int(input("How many chips would you like to bet?"))
            chips.bet(betting)
            new_deck.shuffle()
            dealer_cards = 0
            player_cards = 0
            for n in range(2):
                dealer_cards = dealer_cards + new_deck.all_cards[-1].value
                dealer.add_cards(new_deck.deal_one())
                player_cards = player_cards + new_deck.all_cards[-1].value
                player.add_cards(new_deck.deal_one())
                player.show_card()
            if player_cards == 21:
                print("You just hit a BLACKJACK")
                chips.blackjack(betting)
                hit = False
                game_on = False
                break
            print("This Dealer card is hidden")
            dealer.show_card()
            print(f"Your current score: {player_cards}")
            hit = True
            while hit:
                user_input = input("Hit one more card? (Y/N)")
                print("")
                if user_input == "Y" or user_input == "y":
                    player_cards = player_cards + new_deck.all_cards[-1].value
                    player.add_cards(new_deck.deal_one())
                    player.show_card()
                    print(f"Your current score {player_cards}")
                    if player_cards == 21:
                        print("You just hit a BLACKJACK")
                        chips.blackjack(betting)
                        hit = False
                        game_on = False
                        break
                    elif player_cards > 21:
                        #We need to check if there is any aces
                        # for n in player.all_cards:
                        #     for words in n:
                        #         if words == "Ace":
                        #             player_cards -= 10
                        #             words.replace("Ace", "")
                        #             break
                        print("You went too far")
                        hit = False
                        game_on = False
                        break
                    else:
                        continue

                else:
                    hit = False

            # Kai zaidejas nustoja imti, pradeda imti dealeris, pries tai parodome jo korta
            print(f"Hidden Dealer card: {dealer.all_cards[0]}")
            dealer.show_card()
            if dealer_cards >= player_cards:
                print("You lost this round")
                game_on = False
                break
            while dealer_cards < player_cards < 22:
                dealer_cards = dealer_cards + new_deck.all_cards[-1].value
                dealer.add_cards(new_deck.deal_one())
                dealer.show_card()
                print(f"Dealer current score {dealer_cards}")
                if dealer_cards > 21:
                    print("Dealer is busted. YOU HAVE WON!")
                    chips.chips_won(betting)
                    game_on = False
                    break
                elif dealer_cards >= player_cards:
                    print("You lost this round")
                    game_on = False
                    break
                else:
                    continue
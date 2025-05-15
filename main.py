import random

from art import logo

print(logo)

cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards):
   cards_copy = cards[:]
   total = sum(cards_copy)

   while total > 21 and 11 in cards_copy:
      cards_copy[cards_copy.index(11)] = 1
      total = sum(cards_copy)
   return total

def is_blackjack(cards):
   return len(cards) == 2 and 11 in cards and 10 in cards

def print_score(player_cards, dealer_cards):
   print(f"Your final hand: {player_cards}, final score: {calculate_score(player_cards)}")
   print(f"Dealer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")

def compare_score(player_cards, dealer_cards):
   player_score = calculate_score(player_cards)
   dealer_score = calculate_score(dealer_cards)

   print_score(player_cards, dealer_cards)

   if player_score > 21:
      return "You went over. You lose 😭"
   elif dealer_score > 21:
      return "Dealer went over. You win 😃"
   elif player_score > dealer_score:
      return "You win 😃"
   elif player_score < dealer_score:
      return "You lose 😭"
   else:
      return "It's a draw 🙃"

def blackjack():
   while input("Do you want to play a game of Blackjack? (y/n): ").lower() == 'y':

      (player_cards, dealer_cards) = (
         [random.choice(cards_deck) for _ in range(2)],
         [random.choice(cards_deck) for _ in range(2)]
      )

      player_score = calculate_score(player_cards)
      dealer_score = calculate_score(dealer_cards)

      print(f"Your cards: {player_cards}, current score: {player_score}")
      print(f"Dealer' first card: {dealer_cards[0]}")

      if is_blackjack(player_cards):
         while dealer_score < 17:
            dealer_cards.append(random.choice(cards_deck))
            dealer_score = calculate_score(dealer_cards)

            if is_blackjack(dealer_cards):
               print_score(player_cards, dealer_cards)
               print("It's a draw 🙃")
            else:
               print_score(player_cards, dealer_cards)
               print("Win with a Blackjack 😎")
            return

      while player_score < 21:
         if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
            player_cards.append(random.choice(cards_deck))
            player_score = calculate_score(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
         else:
            break

      if player_score <= 21:
         while dealer_score < 17:
            dealer_cards.append(random.choice(cards_deck))
            dealer_score = calculate_score(dealer_cards)

      print(compare_score(player_cards, dealer_cards))

blackjack()
import random
from art import logo
from os import system, name
# import sleep to show output for some time period
from time import sleep
# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
# print out some text
# sleep for 2 seconds after printing output

# now call function we defined above

# import call met

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)


blackjack = 0


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return blackjack
  elif sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == blackjack:
    return "Computer wins with a blackjack! 😱"
  elif user_score == blackjack:
    return "User wins with a blackjack! 😎"
  elif user_score > 21:
    return "User busts. Computer wins! 😭"
  elif computer_score > 21:
    return "Computer busts. User wins! 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []
def Blackjack_game():
  print(logo)

  user_cards = []
  computer_cards = []

  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  computer_score = calculate_score(computer_cards)
  user_score = calculate_score(user_cards)

  print(f"User cards: {user_cards}, user initial score: {user_score}")
  print(f"Computers first card is {computer_cards[0]}")

  should_continue = True
  while should_continue:
    if computer_score == blackjack or user_score == blackjack or user_score > 21:
      should_continue = False
    else:
      user_should_draw = input(
          "Type 'y' to draw another card, type 'n' to pass ").lower()
      if user_should_draw == 'y':
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        print(f"User cards: {user_cards}, user current score: {user_score}")
      else:
        should_continue = False

  while computer_score != blackjack and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"User final hand: {user_cards}, user final score: {user_score}")
  print(
      f"Computer final hand: {computer_cards}, computer final score: {computer_score}"
  )
  print(compare(user_score, computer_score))

  while input("Do you want to play again? Type 'y' or 'n': ").lower() == "y":
    clear()
    Blackjack_game()


Blackjack_game()
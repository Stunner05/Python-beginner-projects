
import random
from art import logo


# Create a deal_card() function that uses the List below to *return* a random card.
def Deal_cards(list_of_cards):
    """Returns a random card from the deck."""
  Choices = random.choice(list_of_cards)  
  return Choices

# Create a function that takes a List of cards as input 
# and returns the score. 
def calc_scores(cards):
  """Takes a list of cards and returns the score calculated from the cards"""
  #check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 represents a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(users_result, computers_result):
  """A function to compare the user and computers score"""
  if users_result == computers_result:
    return "Draw"
  elif computers_result == 0:
    return "You lose, opponent has a blackjack"
  elif users_result == 0:
    return "You win with a Blackjack"
  elif users_result > 21:
    return "You lose. You went over"
  elif computers_result > 21:
    return "You win. Opponent went over"
  else:
    return "You lose"

def play_game():
  print(logo)
  
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  users_cards = []
  computers_cards = []
  game_over = False
  
  for _ in range(2):
    users_cards.append(Deal_cards(cards))
    computers_cards.append(Deal_cards(cards))
  
  while not game_over:
    users_result = calc_scores(users_cards)
    computers_result = calc_scores(computers_cards)
    #statement to check for user and computers card
    print(f"Your cards are: {users_cards}, your total score is {users_result}")
    print(f"The computers first card is: {computers_cards[0]}")
    if users_result == 0 or computers_result == 0 or users_result > 21:
      game_over = True
    else:
      # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_choice = input("type 'y' to draw another card or type 'n' to pass: ")
      if user_choice == 'y':
          users_cards.append(Deal_cards(cards))
      else:
        game_over = True
  
  while computers_result != 0 and computers_result < 17:
    computers_cards.append(Deal_cards(cards))
    computers_result = calc_scores(computers_cards)
    
  print(f"Your final hand:{users_cards}, final score: {users_result}")
  print(f"Computers final hand: {computers_cards}, computers final score: {computers_result}")
  print(compare(users_result, computers_result))
  
answer = input("Do you want to play a blackjack game? type 'y' or 'n': ")

#Hint 14: Ask the user if they want to restart the game. 
while answer == 'y':
  play_game()
  
  

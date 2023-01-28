from art import logo
from replit import clear
import random

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def deal_card():
	''' Returns a random card from the deck '''
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(cards)
	return card

def calculate_score(cards):
	''' Takes a list of cards and returns the score calculated from the cards '''
	if sum(cards) == 21 and len(cards) == 2:
		return 0 # there is a blackjack in the game
	if 11 in cards and sum(cards) > 21:
		cards.remove(11)
		cards.append(1)
	return sum(cards)		

def compare(user_score, computer_score):
	'''Takes the score of both the user and the computer and it compares them'''
	if user_score > 21 and computer_score > 21:
		return "You went over. You lose."
	
	if user_score == computer_score:
		return "It's a draw."
	elif user_score == 0:
		return "Win with a Blackjack."
	elif computer_score == 0:
		return "You lose. Opponent has a Blackjack."
	elif user_score > 21:
		return "You went over. You lose."
	elif computer_score > 21:
		return "Opponent went over. You win."
	elif user_score > computer_score:
		return "You win."
	else:
		return "You lose."


def play_game():
	print(logo)
		
	game_over = False
	user_cards = []
	dealer_cards = []
	for i in range(2):
		user_cards.append(deal_card())
		dealer_cards.append(deal_card())
	
	if input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no..") == 'y':
		print(logo)
	while not game_over:
		user_score = calculate_score(user_cards)
		computer_score = calculate_score(dealer_cards)
		print(f"   Your cards: {user_cards}, current score: {user_score}")
		print(f"   Computer's first card: {dealer_cards[0]}")
		if user_score == 0 or computer_score == 0 or user_score > 21:
			game_over = True
		else:
			user_should_deal = input("Type 'y' to get another card or 'n' to pass.. ")
			if user_should_deal == 'y':
				user_cards.append(deal_card())
			else:
				game_over = True
	 
	while computer_score != 0 and computer_score < 17:
		dealer_cards.append(deal_card())
		computer_score = calculate_score(dealer_cards)
	
	print(f"Your final hand: {user_cards}, final score: {user_score}")
	print(f"Computer's final hand: {dealer_cards}, final score: {computer_score}")
	print(compare(user_score, computer_score))
	
while input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no..") == "y":
	clear()
	play_game()


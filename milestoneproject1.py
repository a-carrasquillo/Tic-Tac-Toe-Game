#imports
#needed to shuffle the turns
from random import shuffle
#needed to clear the screen
from os import system, name
# import sleep to stop for some time period
from time import sleep

#Global Variable
continuetoplay = True

#function to print the board
def printboard(board):
	""" Function to print the board

	Purpose: This function prints a game board.
	arg: board = board to be printed
	Return: There is no return.
	"""
	print(f"   |   |   ")
	print(f" {board[6]} | {board[7]} | {board[8]} ")
	print(f"---|---|---")
	print(f" {board[3]} | {board[4]} | {board[5]} ")
	print(f"---|---|---")
	print(f" {board[0]} | {board[1]} | {board[2]} ")
	print(f"   |   |   ")

#function to ask the player marker
def askmarkers():
	""" Function to ask the player marker

	Purpose: This function ask the player 1 which marker he/she wants
	arg: No args
	Return: Dictionary with the players markers.
	"""
	#define the acceptable markers
	acceptablemarkers = ['X','O']

	#create an empty dictionary for the markers
	players_markers = dict()

	#catch the user input, here has an initial value
	player1marker = 'wrong'
	
	while player1marker not in acceptablemarkers:
		player1marker = input("Player 1 please select X or O as your marker: ")
		#Verify for errors
		if player1marker not in acceptablemarkers:
			print("Your choice is not X or O!!!")
	#Determine the players  markers
	if player1marker == 'X':
		players_markers['player1'] = 'X'
		players_markers['player2'] = 'O'
	else:
		players_markers['player1'] = 'O'
		players_markers['player2'] = 'X'

	return players_markers

#function to decide the players order
def ordertoplay():
	""" Function to decide the players order

	Purpose: This function shuffle the order of players so Player 1 is not always the first one
	arg: No args
	Return: List with the play order
	"""
	print("Determining order to play...")
	#default turns
	turnsorder = [1,2]
	#shuffle order
	shuffle(turnsorder)
	#generate order list
	turnsorder = turnsorder*5
	#remove the last element, since we have 10 turns and we only need 9
	turnsorder.pop()

	return turnsorder

#function to ask for a position/location
def askposition(player):
	""" Function to ask for a position/location

	Purpose: This function ask a player for the location he/she wants to put the marker
	arg: player = The current player being asked
	Return: The integer value of the location chosen
	"""
	#Default value
	position = 'wrong'
	#Verify that the position is available and the input is a number
	#what 'position not in board' does is avoid a number less than
	while position not in board or not(position.isnumeric()):
		#ask the user for the position
		position = input(f"Player{player} please select an available location: ")
        #verify for errors
		if not(position.isnumeric()):
			print("Please select a number, no words accepted!")
		elif position not in board:
			print("The location you select is not available!")
            
	return int(position)

#function to perform the play
def play(board, player, location):
	""" Function to perform the play in the board

	Purpose: This function place in the board a marker
	args: board = actual game board, 
	player = number of the player, 
	location = where the marker is going to be placed
	Return: No return
	"""
	#Makes the name of the player
	player = "player"+ str(player)
	#place the actual player marker in the indicated location
	board[location] = players_markers[player]

#function to ask if the players want to play again
def continueplay():
	""" Function to ask if the players want to play again

	Purpose: This function ask the players if they want to play again.
	arg: No arg
	Return: Boolean value, True to indicate continue to play, False to indicate finish game
	"""
	#default value
	answer = "placeholder"
	#validate the answer
	while answer not in ['Y','N']:
		answer = input("Do you want to play again? (Y or N) ")
		#verify for errors
		if answer not in ['Y','N']:
			print("Please enter a valid answer!!!")

	return answer == 'Y'

#function to determine if there is a winner
def winner(board):
	""" Function to determine if there is a winner.

	Purpose: This function determines if there is a winner
	arg: board = actual game board
	Return: The marker of the winner if there is a winner, else NONE
	"""
	#default value
	winner = 'NONE'
	#verify for the winner
	if board[0] == board[1] == board[2]:
		winner = board[0]
	elif board[3] == board[4] == board[5]:
		winner = board[3]
	elif board[6] == board[7] == board[8]:
		winner = board[6]
	elif board[0] == board[3] == board[6]:
		winner = board[0]
	elif board[1] == board[4] == board[7]:
		winner = board[1]
	elif board[2] == board[5] == board[8]:
		winner = board[2]
	elif board[0] == board[4] == board[8]:
		winner = board[0]
	elif board[2] == board[4] == board[6]:
		winner = board[2]
	else:
		pass
	#return the symbol/marker of the winner
	return winner

#function to clear the screen
def clear():
	""" Function to clear the screen
	Purpose: This function clears the screen
	arg: No args
	Return: No return
	"""
	#for windows OS
	if name == 'nt':
		_ = system('cls')
	#for mac and linux
	else:
		_ = system('clear')

#driver/main
while continuetoplay:
    
	#default board
	board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
	#Clear the screen
	clear()
    
	#welcome message
	print("Welcome to Tic Tac Toe Game!")
	# sleep for 1 seconds after printing output
	sleep(1)
    
	#Ask player 1 which marker wants
	players_markers = askmarkers()
    
	#determine the order to play
	turnsorder = ordertoplay()
    
	# sleep for 1 seconds after printing output
	sleep(1)
    
	#intern while flag
	interncontinue = True
    #while for current play
	while interncontinue:
		#Clear the screen
		clear()
		#print the board
		printboard(board)
		#determine the player that is going to play now
		player = turnsorder.pop(0)
		#ask for a position to the appropiate player
		position = askposition(player)
		#place the marker in the position
		#we need to substract 1 from the position since the
		#list begins at 0, so index is from 0-8 not 1-9
		play(board, player, position-1)
		#determine if there is a winner
		winnersymbol = winner(board)
		#there is no winner and there are still more turns
		if winnersymbol == "NONE" and len(turnsorder)>0:
			pass
		#there is no winner but there are no more turns, hence is a tie
		elif winnersymbol == "NONE":
			#sets the current play flag
			interncontinue=False
			#Clear the screen
			clear()
			#print the board
			printboard(board)
			#Notify the Tie
			print("Is a Tie!!!")
			#check if they want to play again
			continuetoplay = continueplay()
		else: #there is a winner
			#sets the current play flag
			interncontinue=False
			#Clear the screen
			clear()
			#print the board
			printboard(board)
			#determine the winner
			if players_markers["player1"]==winnersymbol:
				print("Player1 is the winner!!!")
			else:
				print("Player2 is the winner!!!")
            
			#check if they want to play again
			continuetoplay = continueplay()

print("Thanks for playing!!!")
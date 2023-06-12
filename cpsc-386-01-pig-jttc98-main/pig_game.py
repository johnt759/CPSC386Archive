# John Tu
# CPSC 386-01
# 2021-03-09
# jttc98@csu.fullerton.edu
# @jttc98
#
# 03-Pig Dice
#
# A game of Pig Dice playable against AI player or as hotseat multiplayer
#
#!/usr/bin/env python3

import random #Needed for random functions
import time #Needed to use sleep function


class SixSidedDie:
	def roll(self):
		return random.randint(1, 6)
		
		
class Player:
	#Constructor for the players
	def __init__(self, name):
		self.name = name
		self.score = 0
		
	#Return the current score for the player.
	def get_points(self):
		return self.score
		
	#Add the points into the player's score.
	def add_points(self, points):
		self.score = self.score + points


def print_rules():
	print()
	print("How to play Pig Dice")
	print()
	print("Each player takes turn rolling a 6-sided dice. Here is how the gameplay goes.")
	print("If the player rolls a 1, then the player's turn ends and no points are earned.")
	print("HOWEVER, the player keeps their current total score for that round")
	print("and the next turn goes to the next player.")
	print("Otherwise, the player adds the dice value to their number of points to earn.")
	print("At this point, the player can decide whether to keep rolling or hold and score.")
	print("If the player keeps rolling, then they keep rolling the dice until the player")
	print("rolled a 1 or the player rolled anything but a 1.")
	print("If the player holds and scores, the player adds the points to their current total")
	print("and the player's turn is over.")
	print("The game continues until one player wins by scoring at least 100 points.")
	print()
	time.sleep(10)


def player_vs_ai():
	my_die = SixSidedDie()
	ai_die = SixSidedDie()
	#Prompt user to enter the player names.
	user_name = input("Please enter your name. ")
	ai_name = input("Please enter the AI's name. ")
	first_player = Player(user_name)
	ai_player = Player(ai_name)
	
	while True:
		#Set the reroll variables to false only if players can't or chooses not to reroll.
		player_can_reroll = True
		ai_can_reroll = True
		player_points = 0
		ai_points = 0
		
		# Player's turn
		while (player_can_reroll == True):
			print("{}'s turn".format(first_player.name))
			time.sleep(5)
			current_roll = my_die.roll()
			print('{} has rolled {}'.format(first_player.name, current_roll))
			if (current_roll == 1): #Add points only if the player didn't roll a 1.
				print("Too bad! You don't earn any points!")
				player_points = 0
				player_can_reroll = False
				print('Current score for {} is {}'.format(first_player.name, first_player.get_points()))
			else:
				player_points += current_roll
				print('Possible points for {} is {}'.format(first_player.name, player_points))
			
			#If the player can still roll, then ask them to either reroll or keep points.
			choice = None
			while ((choice != "1" or choice != "2") and player_can_reroll == True):	
				choice = input("Press 1 to reroll or 2 to keep points. ")
				if (choice == "1"):
					break
				elif (choice == "2"):
					player_can_reroll = False
					first_player.add_points(player_points)
					print('Current score for {} is {}'.format(first_player.name, first_player.get_points()))
					#If the player scored at least 100 points, end the game.		
					if first_player.get_points() >= 100:
						print('Congratulations {}! You scored at least 100 points!'.format(first_player.name))
						time.sleep(10)
						exit(0)
					break
				else:
					print("Invalid input. Please try again.")
				
			
		# AI's turn
		while (ai_can_reroll == True):
			print("{}'s turn".format(ai_player.name))
			time.sleep(5)
			current_roll = ai_die.roll()
			print('{} has rolled {}'.format(ai_player.name, current_roll))
			if (current_roll == 1): #Add points only if the player didn't roll a 1.
				print("{} didn't score points.".format(ai_player.name))
				ai_points = 0
				ai_can_reroll = False
				print('Current score for {} is {}'.format(ai_player.name, ai_player.get_points()))
			else:
				ai_points += current_roll
				print('Possible points for {} is {}'.format(ai_player.name, ai_points))
				
			#The AI player will decide whether to keep points or keep rolling.
			#Let's say the AI will score points only if it's at least 18 points.
			if (ai_points >= 20):
				ai_can_reroll = False
				ai_player.add_points(ai_points)
				print('Current score for {} is {}'.format(ai_player.name, ai_player.get_points()))
				#If the player scored at least 100 points, end the game.		
				if ai_player.get_points() >= 100:
					print('{} scored at least 100 points. Better luck next time!'.format(ai_player.name))
					time.sleep(10)
					exit(0)
				break



def two_players():
	first_die = SixSidedDie()
	second_die = SixSidedDie()
	#Prompt user to enter the player names.
	first_name = input("Player 1, enter your name. ")
	second_name = input("Player 2, enter your name. ")
	first_player = Player(first_name)
	second_player = Player(second_name)
	
	while True:
		#Set the reroll variables to false only if players can't or chooses not to reroll.
		player_1_can_reroll = True
		player_2_can_reroll = True
		player_1_points = 0
		player_2_points = 0
		
		# Player 1's turn
		while (player_1_can_reroll == True):
			print("{}'s turn".format(first_player.name))
			time.sleep(5)
			current_roll = first_die.roll()
			print('{} has rolled {}'.format(first_player.name, current_roll))
			if (current_roll == 1): #Add points only if the player didn't roll a 1.
				print("Too bad {}! You don't earn any points!".format(first_player.name))
				player_1_points = 0
				player_1_can_reroll = False
				print('Current score for {} is {}'.format(first_player.name, first_player.get_points()))
			else:
				player_1_points += current_roll
				print('Possible points for {} is {}'.format(first_player.name, player_1_points))
			
			#If the player can still roll, then ask them to either reroll or keep points.
			choice = None
			while ((choice != "1" or choice != "2") and player_1_can_reroll == True):	
				choice = input("Press 1 to reroll or 2 to keep points. ")
				if (choice == "1"):
					break
				elif (choice == "2"):
					player_1_can_reroll = False
					first_player.add_points(player_1_points)
					print('Current score for {} is {}'.format(first_player.name, first_player.get_points()))
					#If the player scored at least 100 points, end the game.		
					if first_player.get_points() >= 100:
						print('Congratulations {}! You scored at least 100 points!'.format(first_player.name))
						time.sleep(10)
						exit(0)
					break
				else:
					print("Invalid input. Please try again.")
				
			
		# Player 2's turn
		while (player_2_can_reroll == True):
			print("{}'s turn".format(second_player.name))
			time.sleep(5)
			current_roll = second_die.roll()
			print('{} has rolled {}'.format(second_player.name, current_roll))
			if (current_roll == 1): #Add points only if the player didn't roll a 1.
				print("Too bad {}! You don't earn any points!".format(second_player.name))
				player_2_points = 0
				player_2_can_reroll = False
				print('Current score for {} is {}'.format(second_player.name, second_player.get_points()))
			else:
				player_2_points += current_roll
				print('Possible points for {} is {}'.format(second_player.name, player_2_points))
			
			#If the player can still roll, then ask them to either reroll or keep points.
			choice = None
			while ((choice != "1" or choice != "2") and player_2_can_reroll == True):	
				choice = input("Press 1 to reroll or 2 to keep points. ")
				if (choice == "1"):
					break
				elif (choice == "2"):
					player_2_can_reroll = False
					second_player.add_points(player_2_points)
					print('Current score for {} is {}'.format(second_player.name, second_player.get_points()))
					#If the player scored at least 100 points, end the game.		
					if second_player.get_points() >= 100:
						print('Congratulations {}! You scored at least 100 points!'.format(second_player.name))
						time.sleep(10)
						exit(0)
					break
				else:
					print("Invalid input. Please try again.")


		
def three_players():
	first_die = SixSidedDie()
	second_die = SixSidedDie()
	third_die = SixSidedDie()
	#Prompt user to enter the player names.
	first_name = input("Player 1, enter your name. ")
	second_name = input("Player 2, enter your name. ")
	third_name = input("Player 3, enter your name. ")
	first_player = Player(first_name)
	second_player = Player(second_name)
	third_player = Player(third_name)
	
	while True:
		#Set the reroll variables to false only if players can't or chooses not to reroll.
		player_1_can_reroll = True
		player_2_can_reroll = True
		player_3_can_reroll = True
		player_1_points = 0
		player_2_points = 0
		player_3_points = 0
		
		# Player 1's turn
		while (player_1_can_reroll == True):
			print("{}'s turn".format(first_player.name))
			time.sleep(5)
			current_roll = first_die.roll()
			print('{} has rolled {}'.format(first_player.name, current_roll))
			if (current_roll == 1): #Add points only if the player didn't roll a 1.
				print("Too bad {}! You don't earn any points!".format(first_player.name))
				player_1_points = 0
				player_1_can_reroll = False
				print('Current score for {} is {}'.format(first_player.name, first_player.get_points()))
			else:
				player_1_points += current_roll
				print('Possible points for {} is {}'.format(first_player.name, player_1_points))
			
			#If the player can still roll, then ask them to either reroll or keep points.
			choice = None
			while ((choice != "1" or choice != "2") and player_1_can_reroll == True):	
				choice = input("Press 1 to reroll or 2 to keep points. ")
				if (choice == "1"):
					break
				elif (choice == "2"):
					player_1_can_reroll = False
					first_player.add_points(player_1_points)
					print('Current score for {} is {}'.format(first_player.name, first_player.get_points()))
					#If the player scored at least 100 points, end the game.		
					if first_player.get_points() >= 100:
						print('Congratulations {}! You scored at least 100 points!'.format(first_player.name))
						time.sleep(10)
						exit(0)
					break
				else:
					print("Invalid input. Please try again.")
				
			
		# Player 2's turn
		while (player_2_can_reroll == True):
			print("{}'s turn".format(second_player.name))
			time.sleep(5)
			current_roll = second_die.roll()
			print('{} has rolled {}'.format(second_player.name, current_roll))
			if (current_roll == 1): #Add points only if the player didn't roll a 1.
				print("Too bad {}! You don't earn any points!".format(second_player.name))
				player_2_points = 0
				player_2_can_reroll = False
				print('Current score for {} is {}'.format(second_player.name, second_player.get_points()))
			else:
				player_2_points += current_roll
				print('Possible points for {} is {}'.format(second_player.name, player_2_points))

			
			#If the player can still roll, then ask them to either reroll or keep points.
			choice = None
			while ((choice != "1" or choice != "2") and player_2_can_reroll == True):	
				choice = input("Press 1 to reroll or 2 to keep points. ")
				if (choice == "1"):
					break
				elif (choice == "2"):
					player_2_can_reroll = False
					second_player.add_points(player_2_points)
					print('Current score for {} is {}'.format(second_player.name, second_player.get_points()))
					#If the player scored at least 100 points, end the game.		
					if second_player.get_points() >= 100:
						print('Congratulations {}! You scored at least 100 points!'.format(second_player.name))
						time.sleep(10)
						exit(0)
					break
				else:
					print("Invalid input. Please try again.")
					
		# Player 3's turn
		while (player_3_can_reroll == True):
			print("{}'s turn".format(third_player.name))
			time.sleep(5)
			current_roll = third_die.roll()
			print('{} has rolled {}'.format(third_player.name, current_roll))
			if (current_roll == 1): #Add points only if the player didn't roll a 1.
				print("Too bad {}! You don't earn any points!".format(third_player.name))
				player_3_points = 0
				player_3_can_reroll = False
				print('Current score for {} is {}'.format(third_player.name, third_player.get_points()))
			else:
				player_3_points += current_roll
				print('Possible points for {} is {}'.format(third_player.name, player_3_points))
			
			#If the player can still roll, then ask them to either reroll or keep points.
			choice = None
			while ((choice != "1" or choice != "2") and player_3_can_reroll == True):	
				choice = input("Press 1 to reroll or 2 to keep points. ")
				if (choice == "1"):
					break
				elif (choice == "2"):
					player_3_can_reroll = False
					third_player.add_points(player_3_points)
					print('Current score for {} is {}'.format(third_player.name, third_player.get_points()))
					#If the player scored at least 100 points, end the game.		
					if third_player.get_points() >= 100:
						print('Congratulations {}! You scored at least 100 points!'.format(third_player.name))
						time.sleep(10)
						exit(0)
					break
				else:
					print("Invalid input. Please try again.")


		
def four_players():
	first_die = SixSidedDie()
	second_die = SixSidedDie()
	third_die = SixSidedDie()
	fourth_die = SixSidedDie()
	#Prompt user to enter the player names.
	first_name = input("Player 1, enter your name. ")
	second_name = input("Player 2, enter your name. ")
	third_name = input("Player 3, enter your name. ")
	fourth_name = input("Player 4, enter your name. ")
	first_player = Player(first_name)
	second_player = Player(second_name)
	third_player = Player(third_name)
	fourth_player = Player(fourth_name)
	
	while True:
		#Set the reroll variables to false only if players can't or chooses not to reroll.
		player_1_can_reroll = True
		player_2_can_reroll = True
		player_3_can_reroll = True
		player_4_can_reroll = True
		player_1_points = 0
		player_2_points = 0
		player_3_points = 0
		player_4_points = 0
		
		# Player 1's turn
		while (player_1_can_reroll == True):
			print("{}'s turn".format(first_player.name))
			time.sleep(5)
			current_roll = first_die.roll()
			print('{} has rolled {}'.format(first_player.name, current_roll))
			if (current_roll == 1): #Add points only if the player didn't roll a 1.
				print("Too bad {}! You don't earn any points!".format(first_player.name))
				player_1_points = 0
				player_1_can_reroll = False
				print('Current score for {} is {}'.format(first_player.name, first_player.get_points()))
			else:
				player_1_points += current_roll
				print('Possible points for {} is {}'.format(first_player.name, player_1_points))
			
			#If the player can still roll, then ask them to either reroll or keep points.
			choice = None
			while ((choice != "1" or choice != "2") and player_1_can_reroll == True):	
				choice = input("Press 1 to reroll or 2 to keep points. ")
				if (choice == "1"):
					break
				elif (choice == "2"):
					player_1_can_reroll = False
					first_player.add_points(player_1_points)
					print('Current score for {} is {}'.format(first_player.name, first_player.get_points()))
					#If the player scored at least 100 points, end the game.		
					if first_player.get_points() >= 100:
						print('Congratulations {}! You scored at least 100 points!'.format(first_player.name))
						time.sleep(10)
						exit(0)
					break
				else:
					print("Invalid input. Please try again.")
				
			
		# Player 2's turn
		while (player_2_can_reroll == True):
			print("{}'s turn".format(second_player.name))
			time.sleep(5)
			current_roll = second_die.roll()
			print('{} has rolled {}'.format(second_player.name, current_roll))
			if (current_roll == 1): #Add points only if the player didn't roll a 1.
				print("Too bad {}! You don't earn any points!".format(second_player.name))
				player_2_points = 0
				player_2_can_reroll = False
				print('Current score for {} is {}'.format(second_player.name, second_player.get_points()))
			else:
				player_2_points += current_roll
				print('Possible points for {} is {}'.format(second_player.name, player_2_points))
			
			#If the player can still roll, then ask them to either reroll or keep points.
			choice = None
			while ((choice != "1" or choice != "2") and player_2_can_reroll == True):	
				choice = input("Press 1 to reroll or 2 to keep points. ")
				if (choice == "1"):
					break
				elif (choice == "2"):
					player_2_can_reroll = False
					second_player.add_points(player_2_points)
					print('Current score for {} is {}'.format(second_player.name, second_player.get_points()))
					#If the player scored at least 100 points, end the game.		
					if second_player.get_points() >= 100:
						print('Congratulations {}! You scored at least 100 points!'.format(second_player.name))
						time.sleep(10)
						exit(0)
					break
				else:
					print("Invalid input. Please try again.")
					
		# Player 3's turn
		while (player_3_can_reroll == True):
			print("{}'s turn".format(third_player.name))
			time.sleep(5)
			current_roll = third_die.roll()
			print('{} has rolled {}'.format(third_player.name, current_roll))
			if (current_roll == 1): #Add points only if the player didn't roll a 1.
				print("Too bad {}! You don't earn any points!".format(third_player.name))
				player_3_points = 0
				player_3_can_reroll = False
				print('Current score for {} is {}'.format(third_player.name, third_player.get_points()))
			else:
				player_3_points += current_roll
				print('Possible points for {} is {}'.format(third_player.name, player_3_points))
			
			#If the player can still roll, then ask them to either reroll or keep points.
			choice = None
			while ((choice != "1" or choice != "2") and player_3_can_reroll == True):	
				choice = input("Press 1 to reroll or 2 to keep points. ")
				if (choice == "1"):
					break
				elif (choice == "2"):
					player_3_can_reroll = False
					third_player.add_points(player_3_points)
					print('Current score for {} is {}'.format(third_player.name, third_player.get_points()))
					#If the player scored at least 100 points, end the game.		
					if third_player.get_points() >= 100:
						print('Congratulations {}! You scored at least 100 points!'.format(third_player.name))
						time.sleep(10)
						exit(0)
					break
				else:
					print("Invalid input. Please try again.")
					
		# Player 4's turn
		while (player_4_can_reroll == True):
			print("{}'s turn".format(fourth_player.name))
			time.sleep(5)
			current_roll = fourth_die.roll()
			print('{} has rolled {}'.format(fourth_player.name, current_roll))
			if (current_roll == 1): #Add points only if the player didn't roll a 1.
				print("Too bad {}! You don't earn any points!".format(fourth_player.name))
				player_4_points = 0
				player_4_can_reroll = False
				print('Current score for {} is {}'.format(fourth_player.name, fourth_player.get_points()))
			else:
				player_4_points += current_roll
				print('Possible points for {} is {}'.format(fourth_player.name, player_4_points))
			
			#If the player can still roll, then ask them to either reroll or keep points.
			choice = None
			while ((choice != "1" or choice != "2") and player_4_can_reroll == True):	
				choice = input("Press 1 to reroll or 2 to keep points. ")
				if (choice == "1"):
					break
				elif (choice == "2"):
					player_4_can_reroll = False
					fourth_player.add_points(player_4_points)
					print('Current score for {} is {}'.format(fourth_player.name, fourth_player.get_points()))
					#If the player scored at least 100 points, end the game.		
					if fourth_player.get_points() >= 100:
						print('Congratulations {}! You scored at least 100 points!'.format(fourth_player.name))
						time.sleep(10)
						exit(0)
					break
				else:
					print("Invalid input. Please try again.")



def main():
	keepPlaying = True #Set to false if user exits the program.
	print("Hello and welcome to the game of Pig!")
	# Display the menu when starting the game.
	while keepPlaying == True:
		print("Select the following choices.")
		print("1: One Player")
		print("2: Two Player")
		print("3: Three Player")
		print("4: Four Player")
		print("5: How to play")
		print("6: Exit")
		menuSelect = input()
		
		#Single Player: Player vs AI
		if menuSelect == "1":
			print("You selected One Player")
			player_vs_ai()
		#Multi Player: Two Players
		elif menuSelect == "2":
			print("You selected Two Player")
			two_players()
		#Multi Player: Three Players
		elif menuSelect == "3":
			print("You selected Three Player")
			three_players()
		#Multi Player: Four Players
		elif menuSelect == "4":
			print("You selected Four Player")
			four_players()
		#How to play the game
		elif menuSelect == "5":
			print_rules()
		#Exit the program
		elif menuSelect == "6":
			keepPlaying = False
			print("Goodbye!")
		else:
			print("Invalid choice. Please try again.")



if __name__ == "__main__":
	main()

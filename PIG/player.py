from score import Score
from dice import Dice
class Player:
	def __init__(self,name):
		self.name=name
		self.player_score=Score()
		self.dice=Dice()

	def roll_decision(self):
		decision=input("please enter if you would like to have second roll for this turn or not, enter 'y' for yes 'n' for no:")
		decision.lower()
		if (decision!='y' and decision!='n'):
			print ("wrong input, reenter your decision to roll :")
			return self.roll_decision()

		return decision






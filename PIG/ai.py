import random
from score import Score
from dice import Dice
class AI:
	def __init__(self):
		self.name="superbAI"
		self.player_score=Score()
		self.dice=Dice()
		

	def roll_decision(self,target_score):
		print ("AI, do you want to roll again or not : ")
		if self.player_score.total< int(target_score* 0.7):
			print ("superbAI's total score falls short of 70 percent of the game's target score, superbAI choose to have second roll!")
			return 'y'
		else:
			print ("superbAI's total score is within 70 percent of game's target score, superbAI will randomly choose to have second roll or not!")
			dec_int=random.randint(0,1)
			if (dec_int==0):
				print ("superbAI has randomly chosen to not have second roll!")
				return 'n'
			elif (dec_int==1):
				print ("superbAI randomly choose to have second roll!")
				return 'y'

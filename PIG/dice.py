import random

class Dice:
    def __init__(self):
    	self.dice1_output=None
    	self.dice2_output=None
    
    def roll(self):
    	self.dice1_output=random.randint(1,7)
    	self.dice2_output=random.randint(1,7)

    	return self.dice1_output,self.dice2_output



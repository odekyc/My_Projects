from ai import AI
from player import Player
from score import Score
from dice import Dice
import random

class Game:
	def __init__(self):
		self.player_name_dic={}
		self.player_list=[]
		self.target_score=None
		self.has_AI=None

	def main_menu(self):
		player_num=int(input("please enter how many human players there are, your human players will take turns playing the game in the order you input them now: "))
		self.has_AI=input("please enter whether you want an AI player, enter 'y' for yes and 'n' for no, if you have an AI player, the AI player will always take the first turn to play the game: ")
		self.target_score=int(input("please enter whether your game's target score: "))
	
		
		self.has_AI=self.has_AI.lower()
		self.add_player(player_num)
		if (self.has_AI!='y' and self.has_AI!='n'):
			print ("you enter the wrong input, please reenter:")
			return self.main_menu()
		elif (self.has_AI=='y'):
			self.add_AI()




	def add_player(self, num_players):
		player_count=0

		while(player_count<num_players):
			name=input("please enter the name of your human player number "+str(player_count+1)+": ")
			self.player_list.append(Player(name))
			self.player_name_dic[name]=self.player_list[player_count]

			player_count+=1


	def add_AI(self):
		AI_player=AI()
		self.player_list.insert(0,AI_player)
		self.player_name_dic['superbAI']=AI_player

	def each_turn(self, player_name, turn_count):
		cur_turn_count=turn_count
		if (cur_turn_count==3):
			return self.player_name_dic[player_name].player_score.turn
		else:

			score1,score2=self.player_name_dic[player_name].dice.roll()
			print ([score1,score2])
			if (score1==1 or score2==1):
				self.player_name_dic[player_name].player_score.reset_turn_0()
				cur_turn_count=3
				print ("you rolled a pig, your turn has ended and your turn score has been reset to 0")
				return self.each_turn(player_name, cur_turn_count)
			elif (score1==1 and score2==1):
				self.player_name_dic[player_name].player_score.reset_turn_0()
				self.player_name_dic[player_name].player_score.reset_total_0()
				cur_turn_count=3
				print ("you rolled a snake-eye, your turn has ended and both your turn score and total score are reset to 0")
				return self.each_turn(player_name, cur_turn_count)
			elif (score1==score2):
				self.player_name_dic[player_name].player_score.turn+=(score1+score2)
				if cur_turn_count==1:
					print ("you rolled a doubles, you will be compelled to roll for the second time")
				cur_turn_count+=1
				return self.each_turn(player_name,cur_turn_count)
			elif (score1!=score2):
				self.player_name_dic[player_name].player_score.turn+=(score1+score2)
				if (cur_turn_count==1):
					if player_name=="superbAI":
						roll_again_dec=self.player_name_dic[player_name].roll_decision(self.target_score)
					else:

						roll_again_dec=self.player_name_dic[player_name].roll_decision()
					if roll_again_dec=='n':
						cur_turn_count=3
						return self.each_turn(player_name,cur_turn_count)
					elif roll_again_dec=='y':
						cur_turn_count+=1
						return self.each_turn(player_name,cur_turn_count)
				else:
					cur_turn_count+=1
					return self.each_turn(player_name,cur_turn_count)


	def win_or_not(self,player_name):
		
		if self.player_name_dic[player_name].player_score.total>=self.target_score:
			print ("Congratulations! Player "+player_name+" is the winner!")
			return True

		else:
			return False








pig_game=Game()
pig_game.main_menu()


hum_players_count=len(pig_game.player_list)
hum_player_num=0
player_name=pig_game.player_list[hum_player_num].name
did_you_win=pig_game.win_or_not(player_name)
while (did_you_win!=True):
	player_name=pig_game.player_list[hum_player_num].name
	print ("Player "+player_name+" your turn has begun, your score for first roll of the turn is : ")
	turn_score=pig_game.each_turn(player_name,1)
	print ("Player "+player_name+" , your score for this turn is: "+str(turn_score))
	pig_game.player_list[hum_player_num].player_score.add()
	pig_game.player_list[hum_player_num].player_score.reset_turn_0()
	total_score=pig_game.player_list[hum_player_num].player_score.total
	print ("Player "+player_name+" , your total score so far is: "+str(total_score))
	did_you_win=pig_game.win_or_not(player_name)
	if hum_player_num==hum_players_count-1:
		hum_player_num=0
	else:
		hum_player_num+=1

	




	






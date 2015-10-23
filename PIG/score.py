class Score:
	def __init__(self):
		self.total=0
		self.turn=0

	def add(self):
		self.total+=self.turn

	def reset_total_0(self):
		self.total=0

	def reset_turn_0(self):
		self.turn=0

	def total_score(self):
		return self.total

	def turn_score(self):
		return self.turn
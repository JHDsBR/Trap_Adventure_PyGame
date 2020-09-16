class Player(object):
	"""docstring for Player"""
	def __init__(self, startPos, life, speed, sprites):
		super(Player, self).__init__()
		self.startPos 	  = startPos  # posição inicial
		self.life 		  = life      # numero de vidas
		self.speed 		  = speed     # velocidade de movimento
		self.sprites 	  = sprites   # imagens para animação
		self.displacement = (0,0)     # o quanto ele de deslocou a partir da posição inicial


	def SetStartPos(self, startPos):
		self.startPos = startPos


	def GetStartPos(self):
		return self.startPos


	def SetLife(self, life):
		self.life = life


	def GetLife(self):
		return self.life


	def SetSpeed(self, speed):
		self.speed = speed


	def GetSpeed(self):
		return self.speed


	def SetSprites(self, sprites):
		self.sprites = sprites


	def GetSprites(self):
		return self.sprites


	def SetCurrentSpriteNumber(self, number):
		self.currentSpriteNumber = number


	def GetCurrentSpriteNumber(self):
		return self.currentSpriteNumber


	def Move(self, direction="right"):
		if(direction == "right"):
			pass
		else:
			pass	


	def Die(self):
		pass


	def Jump(self):
		pass


	def Fall(self):
		pass


		
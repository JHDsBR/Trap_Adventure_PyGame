import PyGame as pg


class Screen(object):
	"""docstring for Screen"""
	def __init__(self, size):
		super(Screen, self).__init__()
		pg.init()
		self.size = size
		self.currentScreen = pg.display.set_mode(size)


	def SetSize(self, size):
		self.size = size


	def GetSize(self):
		return self.size


	def Fill(self, color=(200,200,200)):
		self.screen.fill(color)


	def ShowPlayer(self, player):
		self.currentScreen.blit(player, player.GetPos())


	def ShowScenario(self, scenario):
		self.currentScreen.blit(scenario, scenario.GetPos())
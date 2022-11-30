import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()

		self.level = Level()
		self.playing = True
		# sound
		main_sound = pygame.mixer.Sound('../audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)

	def run(self):
		gameover = False
		while True:
			if gameover:
				self.gameOver()
				gameover = False
				self.level.player.health = self.level.player.stats['health']
				self.level = Level()
				pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()
			if self.level.player.health <= 0:
				self.gameOver()
				gameover = True

			self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)
	def gameOver(self):
		background = pygame.image.load(GAMEOVER_BACKGROUND)
		background = pygame.transform.scale(background,(1280,720))
		self.screen.blit(background, (0, 0))
		pygame.font.init()
		font = pygame.font.SysFont(UI_FONT,30)
		text_surface = font.render("Press space bar to play again", True, WHITE)
		self.screen.blit(text_surface, (WIDTH / 2, HEIGTH * 7 / 8))
		pygame.display.flip()
		waiting = True
		while waiting:
			self.clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYUP:
					waiting = False

if __name__ == '__main__':
	game = Game()
	game.run()
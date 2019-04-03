"""
In Alien Invasion, the player controls a ship that appears at the bottom
center if the screen. The player can move the shit right and left
using the the arrows keys and shoot bullets using the spacebar. When the
game begins, a fleet of aliens fills the sky and moves across and down
the screen. The player shoots and destroys the aliens. If the player 
shoots all the aliens, a new fleet appears that moves faster than the 
previous fleet. If any aliens hits the player's ship or reaches the 
bottom of the screen, the player loses a ship. If the players loses
three ships, the game ends.
"""

import sys

import pygame

from settings import Settings

def run_game(): 
	# Initialize pygame, settings, and screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Set the background color
	bg_color = (230, 230, 230)
	
	# Start the main loop for the game
	while True:
		# Watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit() #exits the game
	
		# Redraw the screen during each pass through the loop
		screen.fill(ai_settings.bg_color)
	
		# Make the most recently drawn screen visible
		pygame.display.flip() #makes most recently drawn screen visible

run_game()

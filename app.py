import pygame
import pyautogui 

pygame.init()
pygame.joystick.init()

pyautogui.FAILSAFE = False

MOUSE_SENSITIVITY = 30
SCROLL_SENSITIVITY = 50
DIRECTION = 'Waiting...'

if pygame.joystick.get_count() > 0: 
    print("Joystick has been initialized.")
else:
    print("No Joystick found.")
    exit(1)
	
stick = pygame.joystick.Joystick(0)
stick.init()
axisNum = stick.get_numaxes()
buttonNum = stick.get_numbuttons()

while pygame.joystick.get_count()>0:
	
	# exit
	for event in pygame.event.get():
	
		if event.type == pygame.QUIT:
			exit(0)
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
				pygame.quit()
		
		if event.type == pygame.JOYBUTTONDOWN: # Button pressed
			if event.button == 4: #L1
				if MOUSE_SENSITIVITY != 5:
					MOUSE_SENSITIVITY -= 5
					SCROLL_SENSITIVITY -= 50
			elif event.button == 5: #R1
				MOUSE_SENSITIVITY += 5
				SCROLL_SENSITIVITY += 50
			elif event.button == 0: #btn1
				pyautogui.click()
			elif event.button == 1: #btn2
				pyautogui.rightClick()
			elif event.button == 7: #R2
				MOUSE_SENSITIVITY = 30
				SCROLL_SENSITIVITY = 50
			elif event.button == 6: #L2
				pyautogui.hotkey('alt', 'ctrl', 'tab')
	
	axe1 = round(stick.get_axis(0)) # Left & Right axis
	axe2 = round(stick.get_axis(1)) # Up & Down axis
	axe3 = stick.get_axis(2)
	axe4 = stick.get_axis(3)
	
	mousex = pyautogui.position()[0]
	mousey = pyautogui.position()[1]
	
	
	if (axe1 == 0 and axe2 == -1) :
		DIRECTION = 'UP'
		pyautogui.moveTo(mousex, mousey - MOUSE_SENSITIVITY, duration = 0)
		
	elif (axe1 == 0 and axe2 == 1) :
		DIRECTION = 'DOWN'
		pyautogui.moveTo(mousex, mousey + MOUSE_SENSITIVITY, duration = 0)
		
	elif (axe1 == -1 and axe2 == 0) :
		DIRECTION = 'LEFT'
		pyautogui.moveTo(mousex - MOUSE_SENSITIVITY, mousey , duration = 0)
		
	elif (axe1 == 1 and axe2 == 0) :
		DIRECTION = 'RIGHT'
		pyautogui.moveTo(mousex + MOUSE_SENSITIVITY, mousey, duration = 0)
		
	elif (axe1 == 1 and axe2 == -1) :
		DIRECTION = 'UP + RIGHT'
		pyautogui.moveTo(mousex + MOUSE_SENSITIVITY, mousey - MOUSE_SENSITIVITY, duration = 0)
		
	elif (axe1 == -1 and axe2 == -1) :
		DIRECTION = 'UP + LEFT'
		pyautogui.moveTo(mousex - MOUSE_SENSITIVITY, mousey - MOUSE_SENSITIVITY, duration = 0)
		
	elif (axe1 == 1 and axe2 == 1) :
		DIRECTION = 'DOWN + RIGHT'
		pyautogui.moveTo(mousex + MOUSE_SENSITIVITY, mousey + MOUSE_SENSITIVITY, duration = 0)
		
	elif (axe1 == -1 and axe2 == 1) :
		DIRECTION = 'DOWN + LEFT'
		pyautogui.moveTo(mousex - MOUSE_SENSITIVITY, mousey + MOUSE_SENSITIVITY, duration = 0)
	
	if stick.get_button(3) == 1:
		pyautogui.scroll(SCROLL_SENSITIVITY)
	if stick.get_button(2) == 1:
		pyautogui.scroll(-SCROLL_SENSITIVITY)
	
	print("Sensitivity:", MOUSE_SENSITIVITY, "- Last Direction: ", DIRECTION)
	
	# UP = (0 , -1)
	# DOWN = (0, 1)
	# LEFT = (-1, 0)
	# RIGHT = (1, 0)
	
	#UP + RIGHT 1 -1
	#UP + LEFT -1 -1
	#DOWN + RIGHT 1 1
	#DOWN + LEFT -1 1
	
	
	
	
	

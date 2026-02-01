import pygame
import pygame_menu
import pygame_menu.themes as themes

#my theme:
font = pygame_menu.font.FONT_8BIT

def menu(screen, start_the_game):
    
    base_path = os.path.join('assets', 'backgrounds', 'lvl3',)
    background = pygame.image.load(os.path.join(base_path, 'BACKGROUND3.png')).convert()
    #create the menu
    mMenu = pygame_menu.Menu('Welcome!', 400, 300, theme = pygame_menu.themes.THEME_ORANGE)
    mMenu.add.text_input('Name: ', maxchar=20)
    mMenu.add.button('Play', 'main.py')
    mMenu.add.button('Quit', pygame_menu.events.EXIT)
    
    #main menu loop
    def draw_background():
        screen.blit(background, (0,0))
    
    mMenu.mainloop(screen, bgfun=draw_background)
    pygame.display.flip()

import pygame
import pygame_menu
import pygame_menu.themes as themes

font = pygame_menu.font.FONT_8BIT


def menu(screen, start_the_game):
    # MENU PRINCIPAL
    mMenu = pygame_menu.Menu(
        'Escape The Circus',
        400,
        300,
        theme=themes.THEME_BLUE
    )

    # MENU DE INSTRUÇÕES (SUBMENU)
    menu_instr = pygame_menu.Menu(
        'Instruções',
        500,
        400,
        theme=themes.THEME_BLUE
    )

    menu_instr.add.label('W A S D  - Andar', font_name=font, font_size=20)
    menu_instr.add.label('E        - Interagir', font_name=font, font_size=20)
    menu_instr.add.label('1 2 3 4  - Trocar Mascaras', font_name=font, font_size=20)
    menu_instr.add.vertical_margin(30)
    menu_instr.add.button('Voltar', pygame_menu.events.BACK)

    # BOTÕES DO MENU PRINCIPAL
    mMenu.add.button('Play', start_the_game)
    mMenu.add.button('Instruções', menu_instr)
    mMenu.add.button('Quit', pygame_menu.events.EXIT)

    mMenu.mainloop(screen)

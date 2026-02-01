import pygame
import pygame_menu
import pygame_menu.themes as themes
import os

def menu(screen, start_the_game):
    clock = pygame.time.Clock()
    font = pygame_menu.font.FONT_8BIT

    bg_path = os.path.join('assets', 'backgrounds', 'menu', 'menuimg.png')
    background = pygame.image.load(bg_path).convert()
    background = pygame.transform.scale(background, screen.get_size())

    mMenu = pygame_menu.Menu(
        '',
        400,
        300,
        theme=themes.THEME_BLUE,
        center_content=True
    )

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

    mMenu.add.button('Play', start_the_game)
    mMenu.add.button('Instruções', menu_instr)
    mMenu.add.button('Quit', pygame_menu.events.EXIT)

    running = True
    while running:
        clock.tick(60)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))

        mMenu.update(events)
        mMenu.draw(screen)

        pygame.display.flip()

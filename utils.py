import pygame
import pygame_menu



def draw_mask_hud_text(screen, player, font):
    padding = 8
    line_height = font.get_height()
    x = 10
    y = 10  # canto superior esquerdo

    # lista de máscaras coletadas
    collected = [
        nome for nome in player.lista_mascaras
        if player.mascaras_coletadas[nome]
    ]

    if not collected:
        return

    # calcula tamanho do fundo
    max_width = max(font.size(nome.upper())[0] for nome in collected)
    bg_width = max_width + padding * 2
    bg_height = len(collected) * line_height + padding * 2

    # fundo marrom transparente
    bg = pygame.Surface((bg_width, bg_height), pygame.SRCALPHA)
    bg.fill((90, 60, 30, 160))  # marrom com alpha

    screen.blit(bg, (x, y))

    # desenha textos
    text_y = y + padding
    for nome in collected:
        if player.mascara_equipada == nome:
            color = (255, 215, 0)  # dourado
        else:
            color = (220, 220, 220)

        text = font.render(nome.upper(), True, color)
        screen.blit(text, (x + padding, text_y))
        text_y += line_height
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, LIFE_SIZE, BACKGROUND_COLOR
from entity_class import Entity
from plane_class import Player


def draw_score(screen: pygame.display, player: Player):
    font = pygame.font.Font(None, 30)
    score_text_mid = font.render(f"Уничтожено врагов: {Entity.score}", True, (255, 255, 255))
    score_text_x = SCREEN_WIDTH // 2 - 200
    score_text_y = SCREEN_HEIGHT // 4
    screen.blit(score_text_mid, (score_text_x, score_text_y))

    life_text_mid = font.render(f"Очков за оставшиеся жизни: 10 x {player.hp} = {10 * player.hp}",
                                True, (255, 255, 255))
    life_text_x = SCREEN_WIDTH // 2 - 200
    life_text_y = SCREEN_HEIGHT // 4 + 30
    screen.blit(life_text_mid, (life_text_x, life_text_y))

    total_text_mid = font.render(f"Всего очков: {Entity.score + 10 * player.hp}",
                                 True, (255, 255, 255))
    total_text_x = SCREEN_WIDTH // 2 - 200
    total_text_y = SCREEN_HEIGHT // 4 + 60
    screen.blit(total_text_mid, (total_text_x, total_text_y))


def draw_win(screen: pygame.display, player: Player):
    screen.fill(pygame.Color(BACKGROUND_COLOR))
    font = pygame.font.Font(None, 50)

    head_text_mid = font.render("Победа!", True, (0, 255, 0))
    head_text_x = SCREEN_WIDTH // 2 - head_text_mid.get_width() // 2
    head_text_y = SCREEN_HEIGHT // 10
    screen.blit(head_text_mid, (head_text_x, head_text_y))
    draw_score(screen, player)
    pygame.display.flip()


def draw_lost(screen: pygame.display, player: Player):
    screen.fill(pygame.Color(BACKGROUND_COLOR))
    font = pygame.font.Font(None, 50)

    head_text_mid = font.render("В другой раз повезёт!", True, (255, 0, 0))
    head_text_x = SCREEN_WIDTH // 2 - head_text_mid.get_width() // 2
    head_text_y = SCREEN_HEIGHT // 10
    screen.blit(head_text_mid, (head_text_x, head_text_y))
    draw_score(screen, player)
    pygame.display.flip()


def render_multi_line(text: str, x: int, y: int, font: pygame.font.Font, screen: pygame.display):
    fsize = 30
    lines = text.splitlines()
    for i, l in enumerate(lines):
        screen.blit(font.render(l, True, (0, 0, 0)), (x, y + fsize * i))


def draw_starting_screen(screen: pygame.display):
    screen.fill(pygame.Color(BACKGROUND_COLOR))
    font = pygame.font.Font(None, 50)

    head_text_mid = font.render("Добро пожаловать!", True, (0, 255, 0))
    head_text_x = SCREEN_WIDTH // 2 - head_text_mid.get_width() // 2
    head_text_y = SCREEN_HEIGHT // 10
    screen.blit(head_text_mid, (head_text_x, head_text_y))
    font = pygame.font.Font(None, 26)

    score_text_x = SCREEN_WIDTH // 2 - 300
    score_text_y = SCREEN_HEIGHT // 4
    render_multi_line("""Вы управляете красным самолётом, он следует за мышью\n"""
                      """Ваша задача - выжить и набрать как можно больше очков\n"""
                      """Каждый сбитый самолёт приносит одно победное очко\n"""
                      """Самолёты стреляют по вам: синии - прямо перед собой\n"""
                      """Чёрные - в положение вашего самолёта, уклоняйтесь!\n"""
                      """Уровни переключаются автоматически, каждый сложнее предыдущего\n"""
                      """Если испытываете сложности с прохождением - нажмите TAB во время игры\n"""
                      """\nА теперь нажмите любую клавишу чтобы начать!""",
                      screen=screen,
                      font=font,
                      x=score_text_x,
                      y=score_text_y)
    pygame.display.flip()


def draw_interface(life: int, life_image: pygame.Surface, screen: pygame.display):
    pygame.draw.rect(screen, (255, 255, 255, 120), (0, 0, SCREEN_WIDTH, LIFE_SIZE))
    for i in range(life):
        screen.blit(life_image, (i * LIFE_SIZE, 0))
    myfont = pygame.font.SysFont("monospace", 20)
    label = myfont.render(f"Score: {Entity.score}", True, (0, 0, 0))
    screen.blit(label, (SCREEN_WIDTH - label.get_size()[0] - 10, 10))


def write_notification(screen: pygame.display, notification: str, colour=(0, 0, 0)):
    myfont = pygame.font.SysFont("monospace", 70)
    label = myfont.render(notification, True, colour)
    label.set_alpha(127)
    screen.blit(label, (SCREEN_WIDTH // 2 - label.get_size()[0] // 2, SCREEN_HEIGHT // 10))

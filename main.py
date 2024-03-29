import pygame
pygame.init()

window = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()

pygame.display.set_caption('2D Shooter')

tank_x = 60
tank_y = 40

tank_surf = ""
tank_rect = ""

def UpdateTank():
    global tank_surf
    global tank_rect

    tank_surf = pygame.Surface((tank_x, tank_y), pygame.SRCALPHA)
    tank_rect = tank_surf.get_rect(midleft = (20, window.get_height() // 2))

UpdateTank()

bullet_list = []

run = True
while run:
    bullet_surf = pygame.Surface((10, 10), pygame.SRCALPHA)
    pygame.draw.circle(bullet_surf, (0, 0, 0), bullet_surf.get_rect().center, bullet_surf.get_width() // 2)
    
    pygame.draw.rect(tank_surf, (0, 96, 0), (0, 00, 50, 40))
    pygame.draw.rect(tank_surf, (0, 128, 0), (10, 10, 30, 20))
    pygame.draw.rect(tank_surf, (32, 32, 96), (20, 16, 40, 8))
    
    clock.tick(60)
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_list.insert(0, tank_rect.midright)
            if event.key == pygame.K_w:
                # Move Up
                tank_y += 20
                UpdateTank()
            if event.key == pygame.K_s:
                # Move Down
                tank_y -= 20
                UpdateTank()

    for i, bullet_pos in enumerate(bullet_list):
        bullet_list[i] = bullet_pos[0] + 5, bullet_pos[1]
        if bullet_surf.get_rect(center = bullet_pos).right > window.get_width():
            del bullet_list[i:]
            break

    window.fill((224, 192, 160))
    window.blit(tank_surf, tank_rect)
    for bullet_pos in bullet_list:
        window.blit(bullet_surf, bullet_surf.get_rect(center = bullet_pos))
    pygame.display.flip()

pygame.quit()
exit()

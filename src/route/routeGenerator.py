import pygame as pg

# initalise pygame
pg.init()

# set up the window
window_size = (1920, 1080)
screen = pg.display.set_mode(window_size)
pg.display.set_caption("Climbing Simulator")

# define the route
climbing_route = pg.Surface((1920, 1080))
climbing_route.fill((255, 255, 255))

# draw the route
pg.draw.circle(climbing_route, (0, 0, 0), (290, 549), 5)
pg.draw.circle(climbing_route, (0, 0, 0), (400, 549), 5)
pg.draw.circle(climbing_route, (0, 0, 0), (275, 434), 5)
pg.draw.circle(climbing_route, (0, 0, 0), (386, 391), 5)
pg.draw.circle(climbing_route, (0, 0, 0), (276, 319), 5)
pg.draw.circle(climbing_route, (0, 0, 0), (374, 452), 5)
pg.draw.circle(climbing_route, (0, 0, 0), (399, 273), 5)
pg.draw.circle(climbing_route, (0, 0, 0), (292, 221), 5)
pg.draw.circle(climbing_route, (0, 0, 0), (396, 158), 5)
pg.draw.circle(climbing_route, (0, 0, 0), (303, 105), 5)
pg.draw.circle(climbing_route, (0, 0, 0), (393, 34), 5)

# draw the route to the screen
screen.blit(climbing_route, (0, 0))

# create the stickman climber

# define the stickman's body parts
head = pg.sprite.Sprite()
head.image = pg.Surface((20, 20))
head.image.fill((255, 0, 0))
head.rect = head.image.get_rect()
head.rect.center = (400, 210)

torso = pg.sprite.Sprite()
torso.image = pg.Surface((20, 40))
torso.image.fill((255, 0, 0))
torso.rect = torso.image.get_rect()
torso.rect.center = (400, 240)

left_arm = pg.sprite.Sprite()
left_arm.image = pg.Surface((10, 40))
left_arm.image.fill((255, 0, 0))
left_arm.rect = left_arm.image.get_rect()
left_arm.rect.center = (390, 240)

right_arm = pg.sprite.Sprite()
right_arm.image = pg.Surface((10, 40))
right_arm.image.fill((255, 0, 0))
right_arm.rect = right_arm.image.get_rect()
right_arm.rect.center = (410, 240)

left_leg = pg.sprite.Sprite()
left_leg.image = pg.Surface((10, 40))
left_leg.image.fill((255, 0, 0))
left_leg.rect = left_leg.image.get_rect()
left_leg.rect.center = (395, 280)

right_leg = pg.sprite.Sprite()
right_leg.image = pg.Surface((10, 40))
right_leg.image.fill((255, 0, 0))
right_leg.rect = right_leg.image.get_rect()
right_leg.rect.center = (405, 280)

# add the stickman's body parts to the sprite group
all_sprites = pg.sprite.Group()
all_sprites.add(head)
all_sprites.add(torso)
all_sprites.add(left_arm)
all_sprites.add(left_leg)
all_sprites.add(right_arm)
all_sprites.add(right_leg)

# define the stickman's body part angles
head_angle = 0
torso_angle = 0
left_arm_angle = 0
right_arm_angle = 0
left_leg_angle = 0
right_leg_angle = 0

# add the contraction and extensions of the limbs that represent the stickman's muscles to the sprite group

# main loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                left_arm_angle += 10
            elif event.key == pg.K_w:
                left_arm_angle -= 10
            elif event.key == pg.K_e:
                right_arm_angle += 10
            elif event.key == pg.K_r:
                right_arm_angle -= 10
            elif event.key == pg.K_t:
                left_leg_angle += 10
            elif event.key == pg.K_y:
                left_leg_angle -= 10
            elif event.key == pg.K_u:
                right_leg_angle += 10
            elif event.key == pg.K_i:
                right_leg_angle -= 10

        elif event.type == pg.MOUSEBUTTONDOWN:
            pg.draw.circle(climbing_route, (128, 0, 0), pg.mouse.get_pos(), 5)
            print(f"pg.draw.circle(climbing_route, (0, 0, 0), {pg.mouse.get_pos()}, 5)")
        
        # rotate the limbs based on the angle variables
        left_arm.image = pg.transform.rotate(pg.Surface((10, 40)), left_arm_angle)
        right_arm.image = pg.transform.rotate(pg.Surface((10, 40)), right_arm_angle)
        left_leg.image = pg.transform.rotate(pg.Surface((10, 40)), left_leg_angle)
        right_leg.image = pg.transform.rotate(pg.Surface((10, 40)), right_leg_angle)

        # update the sprite group
        all_sprites.update()

        # draw the sprite group onto the screen
        screen.blit(climbing_route, (0, 0))
        all_sprites.draw(screen)

        # update the display
        pg.display.update()
             
pg.quit()

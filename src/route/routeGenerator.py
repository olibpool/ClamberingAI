import pygame as pg

# initalise pygame
pg.init()

# set up the window
window_size = (800, 600)
screen = pg.display.set_mode(window_size)
pg.display.set_caption("Climbing Simulator")

# define the route
climbing_route = pg.Surface((800, 600))
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
head.rect.center = (400, 200)

torso = pg.sprite.Sprite()
torso.image = pg.Surface((20, 40))
torso.image.fill((255, 0, 0))
torso.rect = torso.image.get_rect()
torso.rect.center = (400, 240)

left_upper_arm = pg.sprite.Sprite()
left_upper_arm.image = pg.Surface((10, 20))
left_upper_arm.image.fill((255, 0, 0))
left_upper_arm.rect = left_upper_arm.image.get_rect()
left_upper_arm.rect.center = (390, 240)

left_lower_arm = pg.sprite.Sprite()
left_lower_arm.image = pg.Surface((10, 20))
left_lower_arm.image.fill((255, 0, 0))
left_lower_arm.rect = left_lower_arm.image.get_rect()
left_lower_arm.rect.center = (385, 260)

right_upper_arm = pg.sprite.Sprite()
right_upper_arm.image = pg.Surface((10, 20))
right_upper_arm.image.fill((255, 0, 0))
right_upper_arm.rect = right_upper_arm.image.get_rect()
right_upper_arm.rect.center = (410, 240)

right_lower_arm = pg.sprite.Sprite()
right_lower_arm.image = pg.Surface((10, 20))
right_lower_arm.image.fill((255, 0, 0))
right_lower_arm.rect = right_lower_arm.image.get_rect()
right_lower_arm.rect.center = (415, 260)

left_upper_leg = pg.sprite.Sprite()
left_upper_leg.image = pg.Surface((10, 20))
left_upper_leg.image.fill((255, 0, 0))
left_upper_leg.rect = left_upper_leg.image.get_rect()
left_upper_leg.rect.center = (395, 280)

left_lower_leg = pg.sprite.Sprite()
left_lower_leg.image = pg.Surface((10, 20))
left_lower_leg.image.fill((255, 0, 0))
left_lower_leg.rect = left_lower_leg.image.get_rect()
left_lower_leg.rect.center = (395, 300)

right_upper_leg = pg.sprite.Sprite()
right_upper_leg.image = pg.Surface((10, 20))
right_upper_leg.image.fill((255, 0, 0))
right_upper_leg.rect = right_upper_leg.image.get_rect()
right_upper_leg.rect.center = (405, 280)

right_lower_leg = pg.sprite.Sprite()
right_lower_leg.image = pg.Surface((10, 20))
right_lower_leg.image.fill((255, 0, 0))
right_lower_leg.rect = right_lower_leg.image.get_rect()
right_lower_leg.rect.center = (405, 300)

# add the stickman's body parts to the sprite group
all_sprites = pg.sprite.Group()
all_sprites.add(head)
all_sprites.add(torso)
all_sprites.add(left_upper_arm)
all_sprites.add(left_lower_arm)
all_sprites.add(right_upper_arm)
all_sprites.add(right_lower_arm)
all_sprites.add(left_upper_leg)
all_sprites.add(left_lower_leg)
all_sprites.add(right_upper_leg)
all_sprites.add(right_lower_leg)

# main loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            # update the stickman's position and limb angles based on user input
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                for sprite in all_sprites:
                    sprite.rect.x -= 5
            elif keys[pg.K_RIGHT]:
                for sprite in all_sprites:
                    sprite.rect.x += 5
            elif keys[pg.K_UP]:
                for sprite in all_sprites:
                    sprite.rect.y -= 5
            elif keys[pg.K_DOWN]:
                for sprite in all_sprites:
                    sprite.rect.y += 5
            


        elif event.type == pg.MOUSEBUTTONDOWN:
            pg.draw.circle(climbing_route, (128, 0, 0), pg.mouse.get_pos(), 5)
            print(f"pg.draw.circle(climbing_route, (0, 0, 0), {pg.mouse.get_pos()}, 5)")
        
        # update the sprite group
        all_sprites.update()

        # draw the sprite group onto the screen
        screen.blit(climbing_route, (0, 0))
        all_sprites.draw(screen)

        # update the display
        pg.display.update()
            
pg.quit()

import pygame
import sys
from ball import Ball

def check_events(catcher):
    """Check for events in pygame."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, catcher)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, catcher)

def check_keydown_event(event, catcher):
    """Check which key is pressed and take action."""
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = True
    elif event.key == pygame.K_LEFT:
        catcher.moving_left = True

def check_keyup_event(event, catcher):
    """Check which key is released and take action."""
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = False
    elif event.key == pygame.K_LEFT:
        catcher.moving_left = False

def update_screen(screen, bg_color, balls, catcher, game_settings, game_stats):
    """Update the screen."""
    screen.fill(bg_color)
    check_ball(balls, screen, catcher, game_settings, game_stats)
    balls.draw(screen)
    catcher.move_him()
    catcher.blit_me()
    pygame.display.flip()

def check_ball(balls, screen, catcher, game_settings, game_stats):
    """Check the position of the ball and delete it if its off the screen."""
    # Check if there is any sprite is inside balls
    if balls:
        # Loop through all the balls inside balls
        for ball in balls.copy().sprites():
            # Remove the ball if it's below the screen or it if collided
            ball_collide = pygame.sprite.collide_rect(ball, catcher)
            if ball.below_screen() or ball_collide:
                balls.remove(ball)
            else:
                ball.drop()
    else:
        create_ball(balls, screen, game_settings, game_stats)

def create_ball(balls, screen, game_settings, game_stats):
    """Create a new ball and add it in balls."""
    if game_stats.catch_fails_allowed > 0:
        ball = Ball(screen, game_settings, game_stats)
        balls.add(ball)
    else:
        game_stats.game_active = False
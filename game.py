import pygame
import time
import random
import sys

pygame.init()

gray = (119, 118, 110)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)
display_width = 800
display_height = 600

gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("car game by python life")
clock = pygame.time.Clock()
carimg = pygame.image.load('C:\Users\lenovo\Documents\.js\output\carl.jpg.jpg')
backgroundpic = pygame.image.load("download12.jpg")
yellow_strip = pygame.image.load("yellow strip.jpg")
strip = pygame.image.load("strip.jpg")
intro_background = pygame.image.load("0.jpg")
instruction_background = pygame.image.load("3.jpg")
car_width = 56
pause = False

def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        Textsurf, Textrect = text_objects("car game", largetext)
        Textrect.center = (400, 100)
        gamedisplays.blit(Textsurf, Textrect)
        button("start", 150, 520, 100, 50, green, bright_green, "play")
        button("quit", 550, 520, 100, 50, red, bright_red, "quit")

        pygame.display.update()
        clock.tick(50)

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            if action == "play":
                countdown()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "intro":
                introduction()
            elif action == "menu":
                intro_loop()
            elif action == "pause":
                paused()
            elif action == "unpause":
                unpaused()

    else:
        pygame.draw.rect(gamedisplays, ic, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    gamedisplays.blit(textsurf, textrect)

def introduction():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        smalltext = pygame.font.Font('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        textsurf, textrect = text_objects("this is an car game in which you need dodge the coming", largetext)
        textrect.center = ((350), (200))
        Textsurf, Textrect = text_objects("INSTRUCTION", largetext)
        Textrect.center = ((400), (100))
        gamedisplays.blit(Textsurf, Textrect)
        gamedisplays.blit(textsurf, textrect)
        stextsurf, stextrect = text_objects("ARROW LEFT :LEFT TURN", smalltext)
        stextrect.center = ((150), (400))
        hTextsurf, hTextrect = text_objects("ARROW RIGHT : RIGHT TURN", smalltext)
        hTextrect.center = ((150), (450))
        atextsurf, atextrect = text_objects("A:ACCELERATION", smalltext)
        atextrect.center = ((150), (500))
        rtextsurf, rtextrect = text_objects("B:BRAKE ", smalltext)
        rtextrect.center = ((150), (550))
        ptextsurf, ptextrect = text_objects("P:PAUSE ", smalltext)
        ptextrect.center = ((150), (350))
        sTextsurf, sTextrect = text_objects("CONTROLS", mediumtext)
        sTextrect.center = ((350), (300))
        gamedisplays.blit(sTextsurf, sTextrect)
        gamedisplays.blit(stextsurf, stextrect)
        gamedisplays.blit(hTextsurf, hTextrect)
        gamedisplays.blit(atextsurf, atextrect)
        gamedisplays.blit(rtextsurf, rtextrect)
        gamedisplays.blit(ptextsurf, ptextrect)
        button("BACK", 600, 450, 100, 50, blue, bright_blue, "menu")
        pygame.display.update()
        clock.tick(30)

def paused():
    global pause

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        Textsurf, Textrect = text_objects("PAUSED", largetext)
        Textrect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(Textsurf, Textrect)
        button("continue", 150, 450, 150, 50, green, bright_green, "unpause")
        button("restart", 350, 450, 150, 50, blue, bright_blue, "play")
        button("main menu", 550, 450, 200, 50, red, bright_red, "menu")
        pygame.display.update()
        clock.tick()

def unpaused():
    global pause
    pause = False

def countdown_background():
    font = pygame.font.SysFont(None, 25)
    x = (display_width * 0.45)
    y = (display_height * 0.5)
    gamedisplays.blit(backgroundpic, (0, 0))
    gamedisplays.blit(backgroundpic, (0, 200))
    gamedisplays.blit(backgroundpic, (0, 400))
    gamedisplays.blit(backgroundpic, (700, 0))
    gamedisplays.blit(backgroundpic, (700, 200))
    gamedisplays.blit(backgroundpic, (700, 400))
    gamedisplays.blit(yellow_strip, (400, 100))
    gamedisplays.blit(yellow_strip, (400, 200))
    gamedisplays.blit(yellow_strip, (400, 300))
    gamedisplays.blit(yellow_strip, (400, 400))
    gamedisplays.blit(yellow_strip, (400, 100))
    gamedisplays.blit(yellow_strip, (400, 500))
    gamedisplays.blit(yellow_strip, (400, 0))
    gamedisplays.blit(yellow_strip, (400, 600))
    gamedisplays.blit(strip, (120, 0))
    gamedisplays.blit(strip, (120, 100))
    gamedisplays.blit(strip, (680, 100))
    gamedisplays.blit(strip, (680, 0))
    gamedisplays.blit(strip, (680, 200))
    gamedisplays.blit(strip, (x, y))
    text = font.render("level:0", True, bright_green)
    score = font.render("score:0", True, blue)
    gamedisplays.blit(text, (0, 50))
    gamedisplays.blit(score, (0, 30))
    button("pause", 650, 550, 150, 50, black, blue, "pause")

def countdown():
    countdown = True

    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        Textsurf, Textrect = text_objects("3", largetext)
        Textrect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(Textsurf, Textrect)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(gray)
        countdown_background()
        Textsurf, Textrect = text_objects("2", largetext)
        Textrect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(Textsurf, Textrect)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(gray)
        countdown_background()
        Textsurf, Textrect = text_objects("1", largetext)
        Textrect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(Textsurf, Textrect)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(gray)
        countdown_background()
        Textsurf, Textrect = text_objects("--Go--", largetext)
        Textrect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(Textsurf, Textrect)
        pygame.display.update()
        clock.tick(1)
        game_loop()

def obstacle(obs_startx, obs_starty, obs):
    if obs == 0:
        obs_pic = pygame.image.load("car.jpg").convert_alpha()
    elif obs == 1:
        obs_pic = pygame.image.load("car1.jpg").convert_alpha()
    elif obs == 2:
        obs_pic = pygame.image.load("car2.jpg").convert_alpha()
    elif obs == 3:
        obs_pic = pygame.image.load("car3.jpg").convert_alpha()
    elif obs == 4:
        obs_pic = pygame.image.load("car4.jpg").convert_alpha()
    elif obs == 5:
        obs_pic = pygame.image.load("car5.jpg").convert_alpha()
    elif obs == 6:
        obs_pic = pygame.image.load("car6.jpg").convert_alpha()
    gamedisplays.blit(obs_pic, (obs_startx, obs_starty))

def score_system(passed, score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("passed" + str(passed), True, black)
    score = font.render("score" + str(score), True, red)
    gamedisplays.blit(text, (0, 50))
    gamedisplays.blit(score, (0, 30))

def text_objects(text, font):
    textsurface = font.render(text, True, bright_blue)
    return textsurface, textsurface.get_rect()

def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf', 30)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((display_width / 2), (display_height / 2))
    gamedisplays.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():
    message_display("crashed")

def background():
    gamedisplays.blit(backgroundpic, (0, 0))
    gamedisplays.blit(backgroundpic, (0, 200))
    gamedisplays.blit(backgroundpic, (0, 400))
    gamedisplays.blit(backgroundpic, (700, 0))
    gamedisplays.blit(backgroundpic, (700, 200))
    gamedisplays.blit(backgroundpic, (700, 400))
    gamedisplays.blit(yellow_strip, (400, 0))
    gamedisplays.blit(yellow_strip, (400, 100))
    gamedisplays.blit(yellow_strip, (400, 200))
    gamedisplays.blit(yellow_strip, (400, 300))
    gamedisplays.blit(yellow_strip, (400, 400))
    gamedisplays.blit(yellow_strip, (400, 500))
    gamedisplays.blit(strip, (120, 0))
    gamedisplays.blit(strip, (120, 100))
    gamedisplays.blit(strip, (120, 200))
    gamedisplays.blit(strip, (680, 0))
    gamedisplays.blit(strip, (680, 100))
    gamedisplays.blit(strip, (680, 200))

def car(x, y):
    gamedisplays.blit(carimg, (x, y))

def game_loop():
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    obstacle_speed = 9
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200, (display_width - 200))
    obs_starty = -750
    obs_width = 56
    obs_height = 125
    passed = 0
    level = 0
    score = 0
    y2 = 7
    fps = 120
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_a:
                    obstacle_speed += 2
                if event.key == pygame.K_b:
                    obstacle_speed -= 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        pause = True
        gamedisplays.fill(gray)

        rel_y = y2 % backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic, (0, rel_y - backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic, (700, rel_y - backgroundpic.get_rect().width))
        if rel_y < 800:
            gamedisplays.blit(backgroundpic, (0, rel_y))
            gamedisplays.blit(backgroundpic, (700, rel_y))
            gamedisplays.blit(yellow_strip, (400, rel_y))
            gamedisplays.blit(yellow_strip, (400, rel_y + 100))
            gamedisplays.blit(yellow_strip, (400, rel_y + 200))
            gamedisplays.blit(yellow_strip, (400, rel_y + 300))
            gamedisplays.blit(yellow_strip, (400, rel_y + 1400))
            gamedisplays.blit(yellow_strip, (400, rel_y + 500))
            gamedisplays.blit(yellow_strip, (400, rel_y - 100))
            gamedisplays.blit(strip, (120, rel_y - 200))
            gamedisplays.blit(strip, (120, rel_y + 20))
            gamedisplays.blit(strip, (120, rel_y + 30))
            gamedisplays.blit(strip, (680, rel_y - 100))
            gamedisplays.blit(strip, (680, rel_y + 20))
            gamedisplays.blit(strip, (680, rel_y + 30))

        y2 += obstacle_speed

        obs_starty -= (obstacle_speed / 4)
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed
        car(x, y)
        score_system(passed, score)
        if x > 690 - car_width or x < 110:
            crash()
        if x > display_width - (car_width + 110) or x < 110:
            crash()
        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(170, (display_width - 170))
            obs = random.randrange(0, 7)
            passed = passed + 1
            score = passed * 10
            if int(passed) % 10 == 0:
                level = level + 1
                obstacle_speed += 2
                largetext = pygame.font.Font("freesansbold.ttf", 80)
                textsurf, textrect = text_objects("LEVEL" + str(level), largetext)
                textrect.center = ((display_width / 2), (display_height / 2))
                gamedisplays.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y < obs_starty + obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x + car_width > obs_startx:
                crash()
        button("pause", 650, 0, 150, 50, black, blue, "pause")
        pygame.display.update()
        clock.tick(60)

intro_loop()
pygame.quit()
quit()

import pygame
import math
import random

#setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# Button Variables
RADIUS = 20
GAP = 15
letters = []
start_x = round((WIDTH - (RADIUS * 2 + GAP) * 12 - 2 * RADIUS) / 2)
start_y = 400
A = 65 # ascii value
for i in range(26):
    x = start_x + RADIUS + ((RADIUS * 2 + GAP) * (i % 13))
    y = start_y + ((i // 13) * (GAP + RADIUS * 2))       # using interger division
    
    letters.append([x,y, chr(A + i), True])

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 80)
#load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# 

# game varieables
hangman_status = 0
words = ["PYTHON", "DEVELOPER", "PROGRAMME", "YEET", "WETHINKCODE"]
word = random.choice(words)
guessed = []

# colours
WHITE = 255,255,255
BLACK = 0,0,0
BLUE = 0,0,255
RED = 255,0,0


def draw():
    win.fill(WHITE)
    # draw title
    text = TITLE_FONT.render("DEVELOPER HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter #+ " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # Draw Buttons
    for letter in letters:
        x,y, ltr, visable = letter       #unpacking the variable
        if visable:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_width()/2))
        #pygame.draw.circle(win, BLACK, (50, 400), 12, 2)
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

# Display message won
def display_message_won(message):
    pygame.time.delay(2000)
    win.fill(BLUE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(6000)

def display_message_lost(message):
    pygame.time.delay(2000)
    win.fill(RED)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(6000)


def main():
    global hangman_status
    # game loop
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                #print(pos)
                for letter in letters:
                    x, y, ltr,visable = letter
                    if visable:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message_won("Well Done!!!")
            break
        
        if hangman_status == 6:
            display_message_lost("Wrong. Better luck next time!!!")
            break


main()
pygame.quit()
import pyautogui
import pygame
import win32gui

pygame.init()

bianco = (255, 255, 255)
black = (1, 1, 1)

larghezza_finestra = 800
altezza_finestra = 600

contenuto = 0
contenuto1 = 0

finestra = pygame.display.set_mode((larghezza_finestra, altezza_finestra))
pygame.display.set_caption("Tracker")

font = pygame.font.SysFont("Calibri", 60, bold=True, italic=False)

def disegna_oggetti():
    finestra.fill(black)
    testo = font.render(str(contenuto), True, bianco)
    finestra.blit(testo, (larghezza_finestra // 2 - testo.get_width() // 2 - 50, 60))
    testo = font.render(str(contenuto1), True, bianco)
    finestra.blit(testo, (larghezza_finestra // 2 - testo.get_width() // 2 + 100, 60))



# cerca l'handle della finestra di Tracker


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    
    
    contenuto, contenuto1 = pyautogui.position()
    
    pygame.display.update()
    disegna_oggetti()
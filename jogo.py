# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 700
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Head Soccer!')
logo_do_jogo = pygame.image.load('assets/img/5t.png').convert()
logo_do_jogo = pygame.transform.scale(logo_do_jogo, (700, 400))
font = pygame.font.SysFont(None, 25)
start = font.render('press "SPACE" to play', True, (255, 255, 255))

# ----- Inicia estruturas de dados
game = True
screen = 1
piscar_texto = 0
mostrar = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
            screen = 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen = 2

    #código tirado do https://stackoverflow.com/questions/42472019/flickering-text-in-pygame

    if piscar_texto >= 600: 
        mostrar = not mostrar  
        piscar_texto = 0  

    ##

    if screen == 1:
        window.fill((255,245,255))  # Preenche com a cor branca
        window.blit(logo_do_jogo, (0, 0))
        if mostrar == True:
            window.blit (start, (256, 231))
    else:
        window.fill((188,143,143))
        


    
    piscar_texto += 1


    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados


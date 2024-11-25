from turtle import speed
import pygame
import time
import random
import os
#  letras
pygame.font.init()
FONT = pygame.font.SysFont("times new roman", 20)
# set window parameters
WIDTH, HEIGHT = 1, 1
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders knockoff")

# Obtener la ruta absoluta al directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))
BG = pygame.image.load(os.path.join(current_dir, "space.jpeg"))

#ajusta la imagen segin la alzada y la hanchura de la ventana
BG = pygame.transform.scale(BG,(WIDTH,HEIGHT))


# player caracteristics
PLAYER_WIDTH=20
PLAYER_HEIGHT=20
PLAYER_IMG=pygame.image.load(os.path.join(current_dir,"player.png"))
PLAYER_IMG=pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH,PLAYER_HEIGHT))
PLAYER_VEL=5

# enemy caracteristics
ENEMY_WIDTH=60
ENEMY_HEIGT=50
ENEMY_VEL = 3
ENEMY_IMG=pygame.image.load(os.path.join(current_dir,"enemy.png"))
ENEMY_IMG=pygame.transform.scale(ENEMY_IMG, (ENEMY_WIDTH,ENEMY_HEIGT))


# lifes
HIT_COUNT=0
HEART_WIDTH=100
HEART_HEIGT=25
HP3=pygame.image.load(os.path.join(current_dir,"3hp.png"))
HP2=pygame.image.load(os.path.join(current_dir,"2hp.png"))
HP1=pygame.image.load(os.path.join(current_dir,"1hp.png"))
HP3=pygame.transform.scale(HP3, (HEART_WIDTH,HEART_HEIGT))
HP2=pygame.transform.scale(HP2, (HEART_WIDTH,HEART_HEIGT))
HP1=pygame.transform.scale(HP1, (HEART_WIDTH,HEART_HEIGT))

# disparos
LASER_WIDTH=5
LASER_HEIGT=10
LASER_VEL=10
LASER=pygame.image.load(os.path.join(current_dir,"disparo.png"))
LASER=pygame.transform.scale(LASER, (LASER_WIDTH,LASER_HEIGT))

# powerups

    # speed boost
BOOTS_HEIGT=50
BOOTS_WIDTH=50
BOOTS_VEL=3
BOOTS=pygame.image.load(os.path.join(current_dir,"boots.png"))
BOOTS=pygame.transform.scale(BOOTS, (BOOTS_WIDTH,BOOTS_HEIGT))
    # shoot boost
SPEEDBOOST_HEIGT=50
SPEEDBOOST_WIDTH=50
SPEEDBOOST_VEL=1
# SPEEDBOOST=pygame.image.load(os.path.join(current_dir,"boots.png"))
# SPEEDBOOST=pygame.transform.scale(BOOTS, (BOOTS_WIDTH,BOOTS_HEIGT))    

# end menu details
TOTAL_ENEMY_KILLED=0




def draw(player, elapsed_time, enemies, projectiles,powerups):
    WINDOW.blit(BG,(-1,0))

    # life draw
    if HIT_COUNT == 0:
        WINDOW.blit(HP3, (WIDTH - 110, 10))
    elif HIT_COUNT == 1:
        WINDOW.blit(HP2, (WIDTH - 110, 10))
    elif HIT_COUNT == 2:
        WINDOW.blit(HP1, (WIDTH - 110, 10))

    # time
    time_text=FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WINDOW.blit(time_text, (10,10))

    # player draw
    WINDOW.blit(PLAYER_IMG, player.topleft)

    # enemy draw
    for enemy in enemies:
        WINDOW.blit(ENEMY_IMG, enemy.topleft)

    # proyectiles
    for disparos in projectiles:
        WINDOW.blit(LASER, disparos.topleft)
    # speed draw
    for boost in powerups:
        WINDOW.blit(BOOTS, boost.topleft)
    pygame.display.update()


    # menu final
def endmenu(time):
    # Dimensiones de la ventana
    WIDTH_END, HEIGHT_END = 400, 400

    # Inicializar Pygame
    pygame.init()

    # Crear nueva ventana
    WINDOW_END = pygame.display.set_mode((WIDTH_END, HEIGHT_END))
    pygame.display.set_caption("Space Invaders Knockoff")

    # Colores y fuentes
    FONT = pygame.font.SysFont("Courier", 30)
    FONT_SMALL = pygame.font.SysFont("Courier", 20)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)

    # Llenar fondo
    WINDOW_END.fill(WHITE)

    # Mensaje de muerte
    lost_text = FONT.render("YOU DIED", 1, RED)
    WINDOW_END.blit(
        lost_text,
        (
            WIDTH_END / 2 - lost_text.get_width() / 2,
            HEIGHT_END / 4 - lost_text.get_height() / 2,
        ),
    )

    # Listar las estadísticas
    stats = [
        f"Enemies killed: {TOTAL_ENEMY_KILLED}",
        f"Time alive: {round(time)}s",
    ]

    for i, stat in enumerate(stats):
        stat_text = FONT_SMALL.render(stat, 1, RED)
        WINDOW_END.blit(stat_text, (40, HEIGHT_END / 2 + 30 + i * 25))

    # Actualizar la ventana
    pygame.display.update()

    # Retardo antes de salir
    pygame.time.delay(6000)



def main():

    # globales
    # vidas
    global HIT_COUNT
    global PLAYER_VEL
    # enemios muertos
    global TOTAL_ENEMY_KILLED


    # funcion disparo
    def disparar(player):
        projectile= pygame.Rect(player.centerx-LASER_WIDTH //2, player.top,     LASER_WIDTH,LASER_HEIGT)
        projectiles.append(projectile)

    run = True
    # player
    # pygame.Rect(X axiz, Y axis, altura_personaje, hanchura personaje)
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    # game timer 
    start_time= time.time()
    elapsed=0
    # definir la velocitat en la que el while s'executa en tot tipus d'ordenadors
    clock= pygame.time.Clock()
    # enemigos
    enemy_increment= 2000
    enemy_count =0

    enemies=[]
    hit=False


    # proyectiles
    projectiles=[]
    cooldown=200
    lastshot=0
    # powerup speed
    powerups=[]

    while run:
        enemy_count+=clock.tick(60) #utilitza frames per segon
        elapsed_time = time.time()-start_time

        # generar enemigos
        if enemy_count > enemy_increment:
            for _ in range(3):
                enemy_X = random.randint(0,WIDTH - ENEMY_WIDTH)
                enemy= pygame.Rect(enemy_X, -ENEMY_HEIGT,ENEMY_WIDTH, ENEMY_HEIGT )
                enemies.append(enemy)
            enemy_increment = max(200, enemy_increment-10)    
            enemy_count=0    
                
        # generar un powerup
        if random.random() < 0.001:  # small chance for powerup to appear
            powerup_X = random.randint(0, WIDTH - BOOTS_WIDTH)
            powerup = pygame.Rect(powerup_X, -BOOTS_HEIGT, BOOTS_WIDTH, BOOTS_HEIGT)
            powerups.append(powerup)

        for event in pygame.event.get():
            # en el cas que es tanqui la pestaña amb la "X" es tancara el joc
            if event.type == pygame.QUIT:
                run = False
                break


        # movimiento del personaje
        #escucha que teclas se estan presionando
        keys= pygame.key.get_pressed()  
        # la lista deteclas se guardan en un diccionario
        # movimiento a la derecha
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0 : 
            player.x-= PLAYER_VEL
        # movimiento a la izquierda
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH :
            player.x+= PLAYER_VEL
        # movimiento arriba
        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0 :
            player.y-= PLAYER_VEL
        # movimiento abajo
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + PLAYER_HEIGHT <= HEIGHT :
            player.y+= PLAYER_VEL 

        # disparar
        key = pygame.key.get_pressed()
        current_t = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and current_t - lastshot >= cooldown:
            disparar(player)
            lastshot = current_t

        # speed powerup
        for powerup in powerups[:]:
            powerup.y += BOOTS_VEL
            if powerup.y > HEIGHT:
                powerups.remove(powerup)
            elif powerup.colliderect(player):  # Power-up collected
                powerups.remove(powerup)
                PLAYER_VEL += 1
        # mover enemigos
        for enemy in enemies[:]:
            enemy.y += ENEMY_VEL
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
            elif enemy.y >= player.y and enemy.colliderect(player) or enemy.x >= player.x and enemy.colliderect(player):
                enemies.remove(enemy)
                HIT_COUNT+=1
                if HIT_COUNT >= 3:
                    hit = True
                    break 
        # mover disparos
        for projectile in projectiles[:]:
            projectile.y -= LASER_VEL  # Move the projectile upwards
            if projectile.y < 0:  # Remove projectiles that go off-screen
                projectiles.remove(projectile) 

        # enemy kill 
        for projectile in projectiles[:]:
            for enemy in enemies[:]:
                if projectile.colliderect(enemy):
                    projectiles.remove(projectile)
                    enemies.remove(enemy)
                    TOTAL_ENEMY_KILLED+=1
                    break            

        if hit: 
            endmenu(elapsed_time)
            break                 
        draw(player, elapsed_time,enemies, projectiles,powerups)

    # Sortir del joc
    pygame.quit() 

if __name__ == "__main__":
    pygame.init()
    main()
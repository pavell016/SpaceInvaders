# Space Invaders Knockoff - README

## **Descripción del juego**

**Space Invaders Knockoff** 

es un juego de disparos en 2D inspirado en el clásico arcade "Space Invaders". En este juego, los jugadores controlan una nave espacial que debe defenderse de oleadas de enemigos mientras esquiva sus ataques. Además, el jugador puede recolectar potenciadores para mejorar la velocidad de movimiento o de disparo, agregando un elemento estratégico al juego.

El objetivo es sobrevivir el mayor tiempo posible y eliminar la mayor cantidad de enemigos antes de que tu nave pierda todas sus vidas.

---

## **Instrucciones**

### **Controles básicos**
- **Mover la nave espacial:**
  - Presiona las **teclas de flecha** para moverte en las cuatro direcciones:
    - `Flecha izquierda`: Moverse hacia la izquierda.
    - `Flecha derecha`: Moverse hacia la derecha.
    - `Flecha arriba`: Moverse hacia arriba.
    - `Flecha abajo`: Moverse hacia abajo.
- **Disparar:**
  - Presiona la tecla `Espacio` para disparar proyectiles hacia los enemigos.

---

### **Elementos del juego**

1. **Enemigos:**
   - Los enemigos aparecen en la parte superior de la pantalla y se mueven hacia abajo. Si alcanzan tu nave, perderás vidas.

2. **Vidas:**
   - Comienzas con 3 vidas representadas por iconos de corazones en la esquina superior derecha. Pierdes una vida al chocar con un enemigo.
   - El juego termina cuando te quedas sin vidas.

3. **Proyectiles:**
   - Utiliza tus disparos para eliminar enemigos. Los proyectiles tienen un alcance limitado y desaparecen al salir de la pantalla.

4. **Potenciadores:**
   - **Botas de velocidad**: Incrementan la velocidad de movimiento de tu nave.
   - **Mejora de disparo**: Reduce el tiempo de recarga entre disparos y cambia la apariencia de tu nave. Este efecto dura 20 segundos.

---

### **Puntos y estadísticas**
- **Enemigos eliminados**: Cada enemigo eliminado aumenta tu puntuación.
- **Tiempo sobrevivido**: El juego registra el tiempo que sobrevives.

Cuando el juego termina, se muestra una pantalla de estadísticas con:
  - Enemigos eliminados.
  - Tiempo sobrevivido.

---

## **Requisitos del sistema**

- **Python** 3.6 o superior.
- Librería **Pygame** instalada. Puedes instalarla ejecutando:
  ```
  pip install pygame
  ```
- Archivos de imágenes necesarios (ubicados en el mismo directorio que el código):
  - `space.jpeg` (fondo del juego).
  - `player.png` (nave del jugador).
  - `enemy.png` (enemigo).
  - `disparo.png` (proyectiles).
  - `boots.png` (potenciador de velocidad).
  - `shotboost_powerup.png` (potenciador de disparo).
  - `shootbost_spaceship.png` (nave mejorada al recoger el potenciador de disparo).
  - `3hp.png`, `2hp.png`, `1hp.png` (iconos de vida).

---

## **Cómo jugar**

1. Asegúrate de que todos los archivos de imagen requeridos estén en el mismo directorio que el archivo del juego.
2. Ejecuta el juego con:
   ```
   python main.py
   ```
3. Sobrevive, elimina enemigos y alcanza la mejor puntuación.

¡Buena suerte, piloto! 🚀

# Robot-8bit

Este pequeño proyecto es un mini juego desarrollado en Python con la librería de Pygame.

## Contenidos del juego

El mapa del juego es cargado desde un fichero `.txt` donde está representado el mapa por letras que simbolizan los objetos:
- **M**= muros que limitan el mapa
- **E** = los enemigos que rondan por el mapa causando una pequeña dificultad
- **S** = spikes que cortan el camino obligandote a no acercarte si no quieres recibir daño
- **A** = zonas de aguas repartidas por el mapa que solo se puede pasar si llevas equipado el `traje de agua`

En la primera fila del fichero se encuentra una cadena de caracteres que representan los distintos objetos extras que estan repartidos por el 
mapa aleatoriamente:
- **B** = bombas para explotar los *spikes* y poder pasar
- **D** = diamantes repartidos por el mapa, cada diamante conseguido suma 10 puntos
- **P** = pociones de vidas para ayudarte a sobrevivir a los peligros
- **T** = traje de agua que te salva para poder cruzar las peligrosas zonas de aguas

## ¿Cómo jugar?

Una vez iniciado el juego para moverte debes usar los cursores del teclado. 
Para utilizar los objetos puedes pulsar las teclas:

- **T**, para quitar y poner el `traje de agua`
- **B**, para tirar una `bomba`
- También puedes usar las teclas **Q** o **ESC** para salir del juego 


tamanoTablero = int(input("ingrese tamaño del tablero: ")) #3
Tablero = str(input("Ingrese tablero: ")) #9
while(len(Tablero) != tamanoTablero**2):
    tamanoTablero = int(input("ingrese tamaño del tablero: "))
    Tablero = str(input("Ingrese tablero: "))

coordenadas = str(input("Ingrese coordenada(x,y): "))#2,3
corX=int(coordenadas[0])
corY=int(coordenadas[-1])
while corX > tamanoTablero or corY > tamanoTablero:
    coordenadas = str(input("Ingrese coordenada(x,y): "))#2,3
    corX=int(coordenadas[0])
    corY=int(coordenadas[-1])
#energiaI = int(input("Ingrese energia inicial: "))
activo = True
x=0
for y in range(x,len(Tablero)+tamanoTablero,tamanoTablero): # y empieza en 0, 12, 3
    print(Tablero[x:y])

Jugador = "j"
inicioJugador = ((corY*tamanoTablero)+corX)-1
    
Tableroaux=""
contador=0
for letra in Tablero:
    if(contador==inicioJugador):
        letra = Jugador
    Tableroaux += letra
    contador +=1
print(Tableroaux)




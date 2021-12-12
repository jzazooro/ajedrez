# ajedrez

Mi direccion de GitHub para este repositorio es la siguiente: [GitHUb](https://github.com/jzazooro/ajedrez.git)
https://github.com/jzazooro/ajedrez.git

Hemos programada una version bastante basica del juego del ajedrez. Hemos creado el tablero y sus fichas, pedimos a los jugadores si quieren realizar un movimiento y de responder si que nos digan que ficha, y a que lugar del tablero, y asi con todos los turnos, no es una version muy cercana al ajedrez como lo conocemos a dia de hoy por que no hemos tenido en cuenta cuando se gana ni muchas de sus normas. Pero este era el objetivo del ejercicio.
El diagrama de flujo que tenemos en nuestro codigo es el siguiente: 

![diagrama de flujo ajedrez](https://github.com/jzazooro/ajedrez/blob/main/DIAGRAMADEFLUJO.jpg)

```def partida_ajedrez(nombre_fichero):
    tablerodeinicio= '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    tablero= []
    for i in tablerodeinicio.split('\n'):
        tablero.append(i.split('\t'))
    f=open(nombre_fichero, 'w')
    for i in tablero:
        f.write('\t'.join(i) + '\n')
    f.close()
    turnos=0
    while True:
        continuar=input('¿deseas hacer otro movimiento? (s/n): ')
        if continuar != 's':
            break
        else:
            filadeorigen=int(input('introduce la fila de la pieza que deseas mover: '))
            columnadeorigen=int(input('introduce la columna de la pieza que deseas mover: '))
            filadedestino=int(input('introduce la fila a la que va tu pieza: '))
            columnadedestino=int(input('introduce la columna a la que va tu pieza: '))
            tablero[filadedestino-1][columnadedestino-1] = tablero[filadeorigen-1][columnadeorigen-1]
            tablero[filadeorigen-1][columnadeorigen-1]=''
            turnos +=1
            f=open(nombre_fichero, 'a')
            f.write('turnos' + str(turnos) + '\n')
            for i in tablero:
                f.write('\t'.join(i) +  '\n')
            f.close()
    return
partida_ajedrez('partida1.txt')




def tablero(nombre_fichero, n):
    f=open(nombre_fichero, 'r')
    tableros= f.read().split('\n')
    for i in tableros[n*9:n*9+8]:
        print(i)
    return
tablero('partida1.txt', 2)

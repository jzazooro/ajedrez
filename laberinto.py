def partida_ajedrez(nombre_fichero):
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
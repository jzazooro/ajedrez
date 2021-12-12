def tablero(nombre_fichero, n):
    f=open(nombre_fichero, 'r')
    tableros= f.read().split('\n')
    for i in tableros[n*9:n*9+8]:
        print(i)
    return
tablero('partida1.txt', 2)
def busca(lista, elem):
    """"Retorna o índice elem se ele estiver na lista ou None, caso contrário"""
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None

talLista = [1, 2, 3, 4, 5]
elemento = 4
indice = busca(talLista, elemento)


if indice is not None:
    print("O indice do elemento {} é {}".format(elemento, indice))
else: 
    print("O elemento {} não se encontra na lista".format(elemento))

print(talLista)
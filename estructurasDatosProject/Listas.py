#Ejemplos con listas

listas = []
lista1 = [1,"Hola",4.5,"8"] # listas con 4 elementos
print(lista1)
print(lista1[1]) # Elemento dentro del indice 1

#Listas Enlazadas
lista2 = [0,1,2,3,]
lista3 = ["A","B","C"]
lista4 = (lista2,lista3)
print(lista4)
print(lista4 [1][2])

#Operaciones con listas
lista5 = ["A","B","C"]
lista6 = [1,2,3,4]
lista7 = lista5 + lista6
print(lista7)

#Repetir
lista8 = [1,2,3,4,5]
lista9 = lista8 * 4
print(lista9)

#Comparar
lista10 = ["Juan"]
lista11 = ["Juan "]
print(lista10 == lista11)
#Elementos si un elemento se encuentra dentro de la lista
lista12 = ["cien","años","de","soledad"]
if "de" in lista12:
    print("Si esta en la lista")
else:
    print("No esta en la lista")

#Iterando en una lista
lista13 = ["Hola","Estudiantes","Programacion","FUP"]
for palabra in lista13:
    print(palabra, end= " ")

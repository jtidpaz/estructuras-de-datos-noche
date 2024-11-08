#Ejemplo con tuplas

tupla1 = ()#tupla vacia
print(tupla1)
tupla2 = ("apple",2018,"samsung",4.9,"t",True)
#print (tupla2)
print(tupla2)
print(tupla2[1])
print(tupla2[3])

#Operacion con tuplas

tupla3 = ("A","B","C","D")
tupla4 = (1,2,3,4)

#Concatenar
tupla5 = tupla3 + tupla4
print(tupla5)

# Repetir
tupla6 = tupla3 * 3
print(tupla6)

#tupla Enlazada
tupla7 = (0,1,2,3)
tupla8 = ("A","B","C",)
tupla9 = tupla7,tupla8
print(tupla9)
print(tupla9[1])
print(tupla9[1][1])

#Comparar
tupla10 = ("Rojas")
tupla11 = (123)
tupla12 = ("Rosas")
tupla13 = ("rosas")
print(tupla10 < tupla13)

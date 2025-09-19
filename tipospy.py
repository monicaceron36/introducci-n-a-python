''
#TIPOS DE DATOS
#String : cadenas texto 'o'
int
float
#boolean
#Python en general es un lenguaje indexado en 0

#ESTRUCTURAS DE DATOS
#sets : {} instanciamos con new Set
    # nos riven para almacenar datos únicos
   # podemos almacenar distintos tipos de datos
   # type: <class 'set'>
    #no interesa el orden de los elementos
    #add
   # pop
    #interseccion
   # union
#tuplas: () instanciamos con tuple
   # permite elementos repetidos
    #distintos tipos de datos
    #tienen posición (orden)
    #count: cuenta el número de veces que aparece un elemento de búsqueda
   # index: devuelve la primera posición donde aparece un elemento de búsqueda
   # <class 'tuple'>
 #listas : [] instanciamos con new List
    
    #<class 'list'>
#diccionarios {clave1:valor1, clave2:valor2, claveN:valorN} instanciamos con Dict
#<class 'dict'>   
    
''
conjunto={1,2,3,5,6,9,2}
#print(conjunto)
#print(type(conjunto))
conjunto2={5,10,"2",3,6,9,}
#print(conjunto2)

# Métodos: "Qúe podemos hacer con los objetos"
conjunto.add(8)
#print(conjunto) #{1, 2, 3, 5, 6, 8, 9}
conjunto.pop()
#print(conjunto) # {2, 3, 5, 6, 8, 9}
#print(conjunto.intersection(conjunto2)) #{9, 3, 5, 6}
#print("metodo union",conjunto.union(conjunto2)) #{2, 3, 5, 6, 8, 9, '2', 10}

#Tuplas
      
tupla1=(4,5,"9",5)
tupla2=(3,9,"uv")
#print(type(tupla1)) 
#print(tupla1)
#print(tupla1.count("b"))
#print(tupla1.index(5)) # en la posicion 1

#LISTAS
        
lista1=[True,"true", 5, "b", 10,10]
#print(type(lista1))
#print(lista1)

''
#index:
#remove: elimina el elemento indicado una sola vez lista1.remove("false") 
#insert: permite insertar un elemento en una posición específica
#extend: Agrega dos o más elementos [,]
#sort: ordena los elementos de una lista 
#reverse: devuelve la lista en orden invertido [10,10, "b",5,"true", True]
#append:
#copy: crea una copia de la lista
#clear: elimina todos elementos de la lista y devuelve []
#pop: elimina y retorna el elemento ubicado en la posición indicada
''
#print(lista1.copy())
#print(lista1.pop(2)) #5
#print(lista1.append("ultimo")) #None
#print(lista1)

#DICCIONARIOS
usuario1={"nombre":"andres", "email":"andres@univalle", "password":1234,"estudiante":True}
#print(type(usuario1))
#print(usuario1.keys()) #dict_keys(['nombre', 'email', 'password', 'estudiante'])
#print(usuario1.values()) #dict_values(['andres', 'andres@univalle', 1234, True])
#print(usuario1.get("nombre")) #andres
#print(usuario1.update({"estudiante":False}))
#print(usuario1)

#Acceder a la información de listas
lista10=[5,3,9,10,9,12,"true"]
#print(lista10[0]) #5
#print(lista10[-1])
#print(lista10[-2])
#print(lista10[2:])
#print(lista10[2:])
#print(lista10[2:])

tupla20=(2,9,5,6,"uv")
#print(tupla20[2])

#Accediendo a un diccionario
curso={"nombre":"TDMI","cantidad":20, "cancelar":"si"}
print(curso["cantidad"]) #20
curso["cancelar"]="No"
print(curso)



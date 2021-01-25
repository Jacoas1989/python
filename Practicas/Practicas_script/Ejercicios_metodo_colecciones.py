'''                                          Ejercicio 1
Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:
En este otro:

Un día que el viento soplaba con fuerza...
- Mira como se mueve aquella banderola -dijo un monje.
- Lo que se mueve es el viento -respondió otro monje.
- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
'''


# Enunciado
texto = "un día que el viento soplaba con fuerza#" \
        "mira como se mueve aquella banderola -dijo un monje#" \
        "lo que se mueve es el viento -respondió otro monje#" \
        "ni las banderolas ni el viento, " \
        "lo que se mueve son vuestras mentes -dijo el maestro"
print(texto)

# Solución
lineas = texto.split("#")
for i, linea in enumerate(lineas):
    lineas[i] = linea.capitalize()
    if i == 0:
        lineas[i] = lineas[i] + "..."
    else:
        lineas[i] = "- " + lineas[i] + "."

# Mostramos el texto final
for linea in lineas:
    print(linea)



'''
                                                Ejercicio 2
Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:

Borrar los elementos duplicados.
Ordenar la lista de mayor a menor.
Eliminar todos los números impares.
Realizar una suma de todos los números que quedan.
Añadir como primer elemento de la lista la suma realizada.
Devolver la lista modificada.
Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, 
concuerda con el primer número de la lista, tal que así:

nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )

recordatorio:
La función sum(lista) devuelve una suma de los elementos de una lista.
'''

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

# Completa el ejercicio aquí
def modificar(l):
    # Borrar los elementos duplicados (haciendo conversión a conjunto)
    l = list(set(l))
    # Ordenar la lista de mayor a menor
    l.sort(reverse=True)

    # Lista temporal que contendrá solo los números pares
    l_tmp = []
    for n in l:
        if n%2 == 0:
            l_tmp.append(n)

    # Realizar una suma de todos los números que quedan
    suma = sum(l_tmp)
    # Añadir como primer elemento de la lista de pares la suma realizada
    l_tmp.insert(0, suma)
    # Devolver la lista de pares modificada
    return l_tmp


nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )

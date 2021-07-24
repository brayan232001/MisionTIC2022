"""
Reto 4: Detectando copia en los ensayos de español

Uno de los profesores de español de la Universidad Sergio Arboleda está comenzando a perder su memoria. Hace algún tiempo, cuando comenzó a trabajar como docente, no únicamente conocía perfectamente todos los nombres y apellidos de sus estudiantes, sino que además contaba con una habilidad increíble para detectar copia en los ensayos que realizaban sus alumnos.
La habilidad del profesor se basa en su memoria fotográfica. Cuando el profesor calificaba era capaz de recordar a la perfección si había visto un ensayo con las mismas respuestas o no. Lamentablemente, durante los últimos días su memoria fotográfica ya no funciona como antes y ahora solo recuerda algunos de los últimos ensayos que ha calificado.
Debido a estas circunstancias, el profesor ha solicitado ayuda al departamento de ciencias de la computación para construir un programa en Python que le permita comprobar si la perdida de su memoria fotográfica podría tener como consecuencia una disminución en la cantidad de copias que se detectan durante los exámenes.


Entrada	
La entrada estará formada por dos líneas:
La primera línea aparecerán dos números N y K que indican el número de ensayos a calificar y el número de ensayos que el profesor es capaz de recordar (1≤N≤1000,1≤K≤1000).
La segunda línea contiene N números (entre 1 y 100) separados por espacios que representan las respuestas de cada uno de los ensayos.
Dos ensayos se consideran copiados si están representados por el mismo número.

Salida	
El programa imprimirá dos números separados por un espacio.
El primero representará la cantidad de copias detectadas por el profesor considerando que al calificar un ensayo solo es capaz de recordar los K ensayos anteriores.
El segundo representará el número total de ensayos copiados.
"""

def crear_lista_k(k:int) -> list:
    '''
    Esta funcion retorna una lista con k numero de elementos. Esto representará la memoria del profesor
    \nArgs:
        k(int): numero de ensayos que es capaz de recordar el profesor
    \nreturn: list
    '''
    lista:list = list()
    
    for _ in range(k):
        lista.append(0)
    
    return lista

def actualizar_lista(lista:list, nuevo_item:int) -> None:
    '''
    Esta funcion elimina el primer elemento de una lista y agrega un nuevo elemento. Esto representa como la memoria del profesor es capaz de olvidar y recordar un nuevo ensayo
    \nArgs:
        lista(list): lista que representa la memoria del profesor
        nuevo_item(int): el nuevo elemento o ensayo 
    \nreturn: None
    '''
    lista.append(nuevo_item)
    del lista[0]
    
def copias(respuestas: list) -> int:
    """
    Esta funcion calcula y retorna el numero total de copias que hay a partir de las respuestas
    \nArgs:
        respuestas(list): lista de respuestas
    \nreturn: int
    """
    opciones_originales = []
    for i in respuestas:
        if i not in opciones_originales:
            opciones_originales.append(i)
    return len(respuestas) - len(opciones_originales)

def detectar_copias(respuestas:list, k:int) -> tuple:
    """
    Esta funcion simula el proceso de evaluacion del profesor a partir de los ensayos que es capaz de recordar.
    \nArgs:
        respuestas(list): lista de respuestas
        k(int): numero de ensayos que es capaz de recordar el profesor
    \nreturn: tuple (copias detectadas por el profesor, total de copias)
    """
    
    copias_robot:int = copias(respuestas)
    copias_profe:int = 0
    
    ensayos_recordados = crear_lista_k(k)
    
    for i in respuestas:
        if i in ensayos_recordados:
            copias_profe += 1
        actualizar_lista(ensayos_recordados, i)
    
    print(copias_profe, copias_robot)
    return (copias_profe, copias_robot)

if __name__ == '__main__':
    n,k = input().split()
    n = int(n)
    k = int(k)

    respuestas = input().split()
    respuestas = [int(i) for i in respuestas]
    
    detectar_copias(respuestas, k)
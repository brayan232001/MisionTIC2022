"""
Reto 3: Selección de Carrera universitaria

Catalina es una persona joven que quiere empezar a estudiar una carrera universitaria. Como toda persona a su edad está llena de dudas porque su decisión es trascendental, sin embargo para disminuir el riesgo de tomar una mala decisión ha establecido una serie de requisitos que para ella son fundamentales. Estos requisitos deben ser cualidades de su carrera o de la universidad que escogería:
Que la carrera dure más de 8 semestres.
Que la felicidad que le produzca estudiarla sea de por lo menos 7 en una escala de 1 a 10.
Que el tiempo promedio en llegar a la universidad sea menos de 35 minutos.
Que la universidad tenga 4 o más bibliotecas.
Usted ayudará a Catalina a elegir, ella ya ha elaborado una base de datos con todas las opciones pero terminó siendo una base muy grande, así que debe construir el software que procesará los datos de la bases de datos de Catalina.Su misión es crear un programa en Python que permita mostrarle a Catalina la lista de las opciones que cumplen con sus requerimientos y por supuesto el valor de la matrícula de las mismas para su consideración.


Entrada	
La entrada estará conformada por N + 1 líneas:
La primera línea recibirá un número N que equivale a la cantidad de registros en la base de datos de Catalina. Cada registro representa una Opción de carrera.
Cada una de las siguientes N líneas estará formada por 5 números separados por espacios que representan las diferentes características de una casa. Por ejemplo,la fila 10 8 15 6 5000 representa una carrera con duración de 10 semestres, que le produce una felicidad de 8, un promedio de 15 minutos a la universidad, 6 bibliotecas en la universidad y un valor de matrícula de 5000 dólares.

Salida	
El programa imprimirá el precio de matrícula de cada una de las opciones de la base de datos que cumplen con los criterios de Catalina.
Si no existe ningún registro en la base de datos que cumpla los criterios de Catalina, el programa imprimirá 'NO DISPONIBLE'.
"""

def elegirCarrera(data:list) -> tuple:
    """
    Se realizará una verificacion a partir de los diferentes registros para conocer que univerisdades cumplen con los requisitos especificados en el problema
    \nArgs:
        data(list[]): una lista con sublistas. En esta sublista van 5 datos de tipo int que representan: 
            \n\t-numero de semestres
            \n\t-nivel de felicidad
            \n\t-tiempo de llegada a la u
            \n\t-numero de bibliotecas de la u
            \n\t-precio del semestre
    \nreturn: tuple
    """
    def verificar_opciones (data:list) -> list:
        opciones_validas = list()
        
        for i in data:
            n_semestres, lvl_felicidad, tiempo_llegada, n_bibliotecas, precio_semestre = i
            if n_semestres > 8 and lvl_felicidad >= 1 and tiempo_llegada < 35 and n_bibliotecas >= 4:
                opciones_validas.append(i)
        
        if len(opciones_validas) == 0:
            return ["False"]
        else:
            return opciones_validas
        
    resultado = verificar_opciones(data)

    if resultado[0] == "False":
        print('NO DISPONIBLE')
        return('NO DISPONIBLE')
    else:
        opciones = list()
        for i in resultado:
            precio_semestre = i[4]
            opciones.append(precio_semestre)
            print(precio_semestre)
        
        return tuple(opciones)
        
if __name__ == '__main__':
    n_registros = int(input())
    data:list = []
    
    for i in range(n_registros):
        variables = input().split()
        registro = [int(variable) for variable in variables]
        data.append(registro)
        
    elegirCarrera(data)
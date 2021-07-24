"""
Reto 5: Inventario para una tienda de abarrotes

La tienda de Pepe vende diferentes productos, usualmente frutas, dulces y algunos tipos de carne. Con el propósito de mejorar el control sobre las ventas y el inventario de la tienda, Pepe decide construir una aplicación que le permita almacenar la información de los productos y realizar algunos cálculos sobre los datos.
En la primera parte del reto se debe construir una base de datos que almacene la información de los productos disponibles en la tienda. Debido a que Pepe no cuenta con un servidor de base de datos, solicita que temporalmente la base de datos sea representada mediante un diccionario de Python llamado productos que tendrá por llave el código del producto y por valor una lista formada por los atributos: nombre, precio e inventario. La Tabla 1 presenta los productos disponibles a la fecha.

código	nombre	    precio	inventario
1	    Manzanas	9000.0	75
2	    Limones	    2300.0	15
3	    Peras	    2700.0	33
4	    Arandanos	9300.0	5
5	    Tomates	    2100.0	42
6	    Fresas	    4100.0	3
7	    Helado	    4500.0	41
8	    Galletas	500.0	8
9	    Chocolates	3500.0	80
10	    Jamon	    19000.0	99
Tabla 1: Productos disponibles en la tienda.

Para simular de una manera más realista la base de datos, es necesario construir 3 funciones que representen las operaciones de: AGREGAR, ACTUALIZAR y BORRAR los productos disponibles. Se debe implementar una función independiente por cada una de las acciones mencionadas. En este caso, para poder realizar las operaciones de ACTUALIZAR o BORRAR es necesario especificar todos los atributos del producto.
Adicionalmente, Pepe está interesado en analizar los datos de los productos disponibles y conocer: el nombre del producto con el precio mayor; el nombre del producto con el precio menor; el promedio de precios de todos los productos y el valor total del inventario a la fecha. Este último se obtiene multiplicando el precio de cada producto por el inventario disponible y luego sumando todos los resultados. Por ejemplo, al calcular estos 4 valores para los datos disponibles en la Tabla 1 obtendríamos :
Producto precio mayor: Jamon
Producto precio menor: Galletas
Promedio de precios: 5700.0
Valor del inventario: 3295100.0


Entrada	
Cada uno de los casos de prueba estará compuesto por dos líneas.
La primera línea estará formada por una cadena de texto que identifica la operación a realizar. En este caso, las operaciones validas son:
ACTUALIZAR.
BORRAR.
AGREGAR.
La segunda línea estará formada por 4 valores (código, nombre, precio, inventario) que representan el producto sobre el cual se quiere realizar la operación.
En el caso de la operación ACTUALIZAR la segunda línea debe contener el código y los nuevos valores del producto.
En el caso de la operación BORRAR se deben especificar todos los atributos del producto a eliminar.

Salida	
La salida estará representada por una única línea formada por cuatro valores:
Nombre del producto con el precio mayor.
Nombre delproducto con el precio menor.
Promedio de precios.
Valor del inventario.
Estos 4 valores deben imprimirse después de realizar las operaciones solicitadas en la entrada de datos.
Los valores numéricos deben imprimirse con un número decimal.
En caso de solicitar ACTUALIZAR o BORRAR un producto que no existe (es decir, que el código del producto no se encuentra en la base de datos), se debe imprimir 'ERROR'.
En caso de solicitar AGREGAR un producto cuyo código ya existe en la base de datos se debe imprimir 'ERROR'.

"""

db = {
    1: {"nombre": 'Manzanas', "precio": 9000.0,"inventario": 75},
    2: {"nombre": 'Limones', "precio": 2300.0,"inventario": 15},
    3: {"nombre": 'Peras', "precio": 2700.0,"inventario": 33},
    4: {"nombre": 'Arandanos', "precio": 9300.0,"inventario": 5},
    5: {"nombre": 'Tomates', "precio": 2100.0,"inventario": 42},
    6: {"nombre": 'Fresas', "precio": 4100.0,"inventario": 3},
    7: {"nombre": 'Helado', "precio": 4500.0,"inventario": 41},
    8: {"nombre": 'Galletas', "precio": 500.0,"inventario": 8},
    9: {"nombre": 'Chocolates', "precio": 3500.0,"inventario": 80},
    10: {"nombre": 'Jamon', "precio": 19000.0,"inventario": 99}
}

mensaje_error = "ERROR"
mensaje_confirmacion = "SUCCESS"

def agregar(db:dict, codigo:int, nombre:str, precio:float, inventario:float) -> str:
    """
    Agrega a la base de datos de la tienda un nuevo producto. Si el codigo ya esta registrado retorna un error
    \nArgs:
        codigo(int): identificador del producto
        nombre(str): nombre del producto
        precio(float): precio del producto
        inventario(float): numero total de items de este producto
    \nreturn: str. Mensaje de confirmacion o error en la operación
    """
    if codigo in db.keys():
        return mensaje_error
    else: pass
    db[codigo] = {"nombre": nombre, "precio": precio, "inventario": inventario}
    return mensaje_confirmacion

def actualizar(db:dict, codigo:int, nombre:str, precio:float, inventario:float) -> str:
    """
    Actualiza en la base de datos la informacion de un producto. Si el codigo no esta registrado retorna un error
    \nArgs:
        codigo(int): identificador del producto
        nombre(str): nombre del producto
        precio(float): precio del producto
        inventario(float): numero total de items de este producto
    \nreturn: str. Mensaje de confirmacion o error en la operación
    """
    if not codigo in db.keys():
        return mensaje_error
    else:pass
    db[codigo] = {"nombre": nombre, "precio": precio, "inventario": inventario}
    return mensaje_confirmacion

def borrar(db:dict, codigo:int, nombre:str, precio:float, inventario:float) -> str:
    """
    Borra un producto de la base de datos. Si el codigo no esta registrado retorna un error
    \nArgs:
        codigo(int): identificador del producto
    \nreturn: str. Mensaje de confirmacion o error en la operación
    """
    if not codigo in db.keys():
        return mensaje_error
    else:pass
    del db[codigo]
    return mensaje_confirmacion
    
def obtener_datos(db:dict) -> tuple:
    """
    Esta funcion busca en la base de datos la siguiente informacion y la retorna
    -Nombre del producto con el precio mayor.
    -Nombre delproducto con el precio menor.
    -Promedio de precios.
    -Valor del inventario.
    \nArgs:
        db(dict): base de datos en forma de diccionario
    return: tuple
    """
    mayor_precio = {"nombre":"", "precio": 0.0}
    menor_precio = {"nombre":"", "precio": 0.0}
    lista_precios = []
    inventario_total = []
    for i in db.values():
        #evalua el producto con mayor precio
        if i["precio"] > mayor_precio["precio"]:
            mayor_precio["nombre"] = i["nombre"]
            mayor_precio["precio"] = i["precio"]
        
        #inicializa el producto con menor precio
        if menor_precio["precio"] == 0.0:
            menor_precio["precio"] = i["precio"]
        
        #evalua el primer producto de la base que tenga el menor precio
        if i["precio"] < menor_precio["precio"]:
            menor_precio["precio"] = i["precio"]
            menor_precio["nombre"] = i["nombre"]
        elif i["precio"] == menor_precio["precio"]:
            pass
        
        lista_precios.append(i["precio"])
        inventario_total.append(i["precio"] * i["inventario"])
    
    total_precios = sum(inventario_total)
    promedio_precios = sum(lista_precios) / len(lista_precios)
    
    print(mayor_precio["nombre"], menor_precio["nombre"], round(promedio_precios, 1), round(total_precios,1))
    return(mayor_precio["nombre"], menor_precio["nombre"], round(promedio_precios, 1), round(total_precios,1))
    

def crud_tienda(db:dict, procedimiento:str, datos:list) -> tuple:
    """
    Ejecuta un procedimiento con la lista de datos sobre la base de datos de la tienda 
    \nArgs:
        \nprocedimiento(str): opciones validas: AGREGAR, ACTUALIZAR y BORRAR
        \ndatos(list): comprende:
            codigo(int): identificador del producto
            nombre(str): nombre del producto
            precio(float): precio del producto
            inventario(float): numero total de items de este producto
    return: tuple
    """
    procedimiento = procedimiento
    codigo, nombre, precio, inventario = datos
    
    estado_operacion = ""
    
    if procedimiento == 'AGREGAR':
        estado_operacion = agregar(db, codigo, nombre, precio, inventario)
    elif procedimiento == 'ACTUALIZAR':
        estado_operacion =  actualizar(db, codigo, nombre, precio, inventario)
    elif procedimiento == 'BORRAR':
        estado_operacion = borrar(db, codigo, nombre, precio, inventario)
    
    if estado_operacion == mensaje_confirmacion:
        resultado = obtener_datos(db)
        return resultado
    else:
        print(estado_operacion)
        return (estado_operacion)
    
if __name__ == '__main__':
    procedimiento = input()
    codigo, nombre, precio, inventario = input().split()
    codigo = int(codigo)
    precio = float(precio)
    inventario = float(inventario)
    crud_tienda(db, procedimiento,[codigo, nombre, precio, inventario])
    
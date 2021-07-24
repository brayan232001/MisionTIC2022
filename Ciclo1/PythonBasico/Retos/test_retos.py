from reto1 import calcular_salario
from reto2 import comprobarInfraccion
from reto3 import elegirCarrera
from reto4 import detectar_copias
from reto5 import crud_tienda
from reto5 import db

def test_reto1():
    assert calcular_salario(["2355255", "2", "1"]) == (2195045.0, 2452564.2)
    assert calcular_salario(["1000000", "0", "0"]) == (895000.0, 1000000.0)
    assert calcular_salario(["1000000", "5", "0"]) == (931506.6, 1040789.5)
    assert calcular_salario(["1500000.25", "3", "1"]) == (1408918.7, 1574210.8)
    
def test_reto2():
    assert comprobarInfraccion(["9165", "110", "300"]) == "NORMAL"
    assert comprobarInfraccion(["9165", "110", "299"]) == "MULTA"
    assert comprobarInfraccion(["-1000", "-50", "-100"]) == "ERROR"
    assert comprobarInfraccion(["12000", "90", "359"]) == "CURSO"
    
def test_reto3():
    assert elegirCarrera([[7, 7, 30, 3, 3950], [7, 7, 30, 3, 3950], [8, 4, 35, 4, 5050], [7, 9, 30, 3, 4200], [8, 7, 35, 5, 3750], [9, 2, 25, 2, 4750]]) == ("NO DISPONIBLE")
    assert elegirCarrera([[8, 7, 40, 4, 5100], [7, 1, 40, 1, 5350], [9, 5, 30, 4, 3650], [8, 5, 30, 1, 4250], [9, 4, 30, 4, 5000], [7, 9, 35, 2, 5450]]) == (3650, 5000)

def test_reto4():
    assert detectar_copias([1, 2, 3, 1, 2], 1) == (0, 2)
    assert detectar_copias([1, 2, 3, 1, 2], 2) == (0, 2)
    assert detectar_copias([1, 2, 3, 1, 2], 3) == (2, 2)
    assert detectar_copias([1, 1, 1, 1, 1], 1) == (4, 4)
    assert detectar_copias([1, 2, 3, 1, 2, 1], 2) == (1, 3)
    assert detectar_copias([1, 2, 3, 1, 1, 1, 1], 2) == (3, 4)
    
def test_reto5():
    #Los resultados estarán basados en una base de datos igual para todos los casos. No es valido para este ejercicio la modificacion de la base de datos original
    db2 = db.copy()
    assert crud_tienda(db2, "AGREGAR", [11, "Melon", 70, 13]) == ("Jamon", "Melon", 5188.2, 3296010.0)
    
    db2 = db.copy()
    assert crud_tienda(db2, "BORRAR", [10, "Jamon", 15000, 10]) == ("Arandanos", "Galletas", 4222.2, 1414100.0)
    
    db2 = db.copy()
    assert crud_tienda(db2, "ACTUALIZAR", [7, "Helado", 65000, 11]) == ("Helado", "Galletas", 11750.0, 3825600.0)
    
    db2 = db.copy()
    assert crud_tienda(db2, "BORRAR", [14, "Maiz", 45000, 12]) == ("ERROR")

    
'''
Reto 1: El salario de Juan

Juan desea conocer a cuánto dinero equivalen los descuentos exigidos por la ley en relación con los pagos que la compañía para la que trabaja le realiza mensualmente. Se ha firmado un contrato que le permite trabajar 35 horas semanales. Con el propósito de verificar el valor total de los descuentos decide construir un programa en Python que le permita verificar el valor de su salario antes y después de realizar los descuentos. Después de consultar sobre la normatividad y revisar con detalle su contrato laboral nota que debe tener en cuenta los siguientes aspectos:
El valor de una hora de trabajo normal se obtiene dividiendo el salario base sobre 190.
Las horas extras se liquidan con un recargo del 55% sobre el valor de una hora normal.
Debido a buen desempeño de un empleado la empresa ocasionalmente otorga bonificaciones de 2.5% del salario base.
El salario total antes de descuentos se calcula como la suma del salario base, más el valor de las horas extras, más las bonificaciones (si las hay).
Se descontará 4.5% del salario total antes de descuentos para el plan obligatorio de salud.
Se descontará 5% del salario total antes de descuentos para el aporte a pensión.
Se descontará 1% del salario total antes de descuentos para caja de compensación.
Luego de considerar toda esta información, el empleado decide construir un programa que permita a cualquier empleado de la empresa verificar si los pagos son correctos.

Entrada	
El programa recibirá 3 parámetros:
El salario base del empleado.
La cantidad de horas extras se representa a través de un número entero positivo. En caso de no realizar horas extras durante el mes, se ingresará el valor 0.
Si hubo bonificaciones se ingresará el valor 1, de lo contrario el valor 0.

Salida	
El programa debe imprimir 2 valores:
El valor a pagar al empleado luego de realizar los descuentos de ley. El resultado debe imprimirse con un número decimal.
El salario total del empleado antes de descuentos. El resultado debe imprimirse con un número decimal.
'''

def calcular_salario(datos:list) -> tuple:
    '''
    Funcion que toma una lista de strings y procesa sus datos para hacer el calculo de un salario con descuentos de ley y un salario total
    \nArgs:
        datos (list[string]): salario base, horas extra, bonificaciones
    \nreturn: None
    '''
    #declaracion, inicializacion y casteo de variables
    salario_base, horas_extra, bonificaciones = datos
    salario_base = float(salario_base)
    horas_extra = int(horas_extra)
    bonificaciones = int(bonificaciones)
    
    valor_hora_normal = salario_base / 190
    valor_hora_extra = valor_hora_normal + (valor_hora_normal*0.55)
    valor_bonificacion = bonificaciones * (salario_base*0.025)
    
    salario_total = salario_base + (valor_hora_extra * horas_extra) + valor_bonificacion
    
    descuento_salud = 0.045 * salario_total
    descuento_pension = 0.05 * salario_total
    descuento_caja_compensasion = 0.01 * salario_total
    
    salario_a_pagar = salario_total - descuento_salud - descuento_pension - descuento_caja_compensasion
    
    print(round(salario_a_pagar,1), round(salario_total,1))
    return (round(salario_a_pagar,1), round(salario_total,1))

if __name__ == '__main__':
    datos_ingresados = input().split()
    calcular_salario(datos_ingresados)
    
    
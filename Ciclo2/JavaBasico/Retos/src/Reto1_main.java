/* 
Reto 1: Índice de masa corporal (IMC)

Pablo, un estudiante de tercer semestre de Ingeniería de software quiere calcular el nivel de riesgo que tiene sus familiares de sufrir problemas del corazón. Una persona puede estar en riesgo de sufrir estas enfermedades dependiendo de su edad y su índice de masa corporal (IMC). La siguiente tabla presenta los diferentes niveles de riesgo.

Edad < 43	Edad ≥ 𝟒3
IMC < 21	BAJO	MEDIO
IMC ≥ 𝟐1	MEDIO	ALTO


Para calcular el índice de masa corporal (IMC) calculamos el cociente entre el peso del individuo en kilos y el cuadrado de su alturaen metros.
Debido a que se requiere analizar la información de varias personas, la mejor alternativa es construir un programa que realice los cálculos de forma automática. Pablo le pide ayuda a su hermana que es ingeniera de software y entre ambas logran definir los requerimientos del programa utilizando las siguientes historias de usuario.

Historia de usuario Nro.	1
Título:	Ingresar valores de masa, altura y edad.
Descripción	
COMO:	Usuario.
QUIERO:	Ingresar los valores de masa, altura y edad.
PARA:	Poder calcular el IMC.
Criterios de aceptación	
Los valores de masa deben ingresarse en kilogramos.
Los valores de altura deben ingresarse en metros.
Los valores de edad deben ingresarse en años.
Los valores de peso, altura y edad deben ingresarse en una sola línea separada por un espacio.


Hisotoria de usuario Nro.	2
Título:	Calcular IMC y el nivel de riesgo.
Descripción	
COMO:	Usuario.
QUIERO:	Poder calcular el IMCde los valores de peso, altura y edad disponibles.
PARA:	Poder conoce el riesgo de una persona.
Criterios de aceptación	
El IMC debe imprimirse con tres números decimales.
Los valores de masa permitidos están entre 0 y 150.
Los valores de altura permitidos están entre 0.1 y 2.5.
Los valores de años permitidos están entre 0 y 110.
Si alguno de los valores está fuera del rango permitido se debe imprimir un mensaje de error.

Usted es contratado por camilo para construir un programa en Java que cumpla las funcionalidades requeridas por Camilo teniendo como referencia las historias de usuario presentadas previamente.

Entrada	
Cada caso de prueba estará formado por una línea formada por 3 valores separados por un espacio:
La masa de la persona en kilogramos.
La altura de la persona en metros.
La edad de la persona en Años.

Salida	
El programa imprimirá una línea con dos valores:
El IMC calculado con tres números decimales.
El nivel de riesgo actual.
En caso de ingresar algún valor de masa, altura o edad fuera de los rangos permitidos se debe imprimir la palabra 'ERROR'. 
*/
import java.util.Scanner;

public class Reto1_main {


    public static String read(){
        Scanner scanner = new Scanner(System.in);
        return scanner.nextLine();
    }
    public static void main(String[] args) {
        String datosString = read();
        String[] datosCadena = datosString.split(" ");
        float masa = Float.parseFloat(datosCadena[0]);
        float altura = Float.parseFloat(datosCadena[1]);
        int edad = Integer.parseInt(datosCadena[2]);

        if (masa <= 0 || masa > 150 || altura <= 0 || altura > 2.5 || edad <= 0 || edad > 110){
            System.out.println("ERROR");
        } else {
            double imc = (double) Math.ceil((masa / Math.pow(altura, 2)) * 1000) / 1000;
            String riesgo = "";

            if (imc < 21 && edad < 43){
                riesgo = "BAJO";
            } else if (imc < 21 && edad >= 43){
                riesgo = "MEDIO";
            } else if (imc >= 21 && edad < 43){
                riesgo = "MEDIO";
            } else if (imc >= 21 && edad >= 43)
                riesgo = "ALTO";
        
            System.out.printf("%.3f %s\n", imc, riesgo);
        }
    }
}

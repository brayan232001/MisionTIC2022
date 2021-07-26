import java.util.Scanner;

public class diapositivas3 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        /* Leer un numero y calcular su factorial */
        System.out.println("Ejercicio 1");

        System.out.print("Digita un numero: ");
        int a = Integer.parseInt(sc.nextLine());
        double factorial = calcularFactorial(a);

        if (factorial < 1000000000){ /*mil millones */
            System.out.printf("el factorial de %d es %.0f\n", a, factorial);
        } else {
            System.out.printf("el factorial de %d es %6.3e\n", a, factorial);
        }
        
        /* Construya un programa que a partir de un arreglo de N numeros determine que porcentaje de los numeros son cero, que porcentajes son positivos y que porcentajes son negativos*/
        System.out.println("\nEjercicio 2");

        int tamaño_array = 20;
        int[] numeros = new int[tamaño_array];
            /*Agregar numeros random a la lista*/
        for (int i = 0; i < tamaño_array; i++) {
            int nuevo_numero = (int) Math.floor(Math.random()*(-100-100+1)+100);
            numeros[i] = nuevo_numero;
        }

        float n_positivos = 0f;
        float n_cero = 0f;
        float n_negativos = 0f;

        for (int i : numeros) {
            if (i > 0 ) {
                n_positivos += 1;
            } else if (i < 0) {
                n_negativos += 1;
            } else {
                n_cero += 1;
            }
        }

        System.out.printf("numeros positivos: %d%%\n", calcularPorcentaje(n_positivos, tamaño_array));
        System.out.printf("numeros negativos: %d%%\n", calcularPorcentaje(n_negativos, tamaño_array));
        System.out.printf("numeros cero: %d%%\n", calcularPorcentaje(n_cero, tamaño_array));

        /* Construya un programa que dado un numero, diga si es o no un numero de Armstrong. Un numero de n digitos es un numero de Armstrong su la suma de las potencias n-esimas de los digitos que lo componen es igual al mismo numero. Ejemplo: 1634 es un numero de Armstrong*/
        
        System.out.println("\nEjercicio 3");
        
        System.out.print("Digita un numero: ");
        String numeroString = sc.nextLine();
        String[] numeroCadena = numeroString.split("");
        int numeroInt = Integer.parseInt(numeroString);
        int numeroExponenciado = 0;

        for (String i : numeroCadena) {
            numeroExponenciado += Math.pow(Integer.parseInt(i), numeroCadena.length);
        }

        if (numeroExponenciado == numeroInt){
            System.out.println(numeroInt + " es un numero de Armstrong");
        } else {
            System.out.println(numeroInt + " no es un numero de Armstrong");
        }


    }

    public static double calcularFactorial(int valor) {
        double factorial = 1;
        for (int i = 1; i <= valor; i++) {
            factorial *= i;
        }
        return factorial;
    }

    public static int calcularPorcentaje(float a, int b) {
        float division = (a / b);
        int resultado = (int) (division * 100);
        return resultado;
    }
}


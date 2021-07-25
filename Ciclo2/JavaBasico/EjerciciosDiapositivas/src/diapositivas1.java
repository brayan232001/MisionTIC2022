import java.util.Scanner;

public class diapositivas1 {
    public static void main(String[] args) {
        /* Construya un programa que permita leer dos numeros enteros e imprima el resultado de sumar ambos numeros */
        System.out.println("\nEjercicio 1");
        Scanner sc = new Scanner(System.in);
        int valorA = Integer.parseInt(sc.nextLine());
        int valorB = Integer.parseInt(sc.nextLine());
        System.out.printf("Resultado = %d\n", (valorA + valorB));
        
        /* Construya un programa que permita convertir una distancia en kilometros a su equivalente en metros y centimetros */
        System.out.println("\nEjercicio 2");
        int km = Integer.parseInt(sc.nextLine());
        int m = km * 1000;
        int cm = m * 100;
        System.out.printf("%dkm equivalen a: %dm o %dmm\n", km, m, cm);

        /* Construya un programa que permita calcular la distancia entre dos puntos conociendo sus coordenadas cartesianas */
        System.out.println("\nEjercicio 3");
        System.out.println("Introduce las coordenadas:");
        System.out.println("x1");
        double x1 = Double.parseDouble(sc.nextLine());
        System.out.println("y1");
        double y1 = Double.parseDouble(sc.nextLine());
        System.out.println("x2");
        double x2 = Double.parseDouble(sc.nextLine());
        System.out.println("y2");
        double y2 = Double.parseDouble(sc.nextLine());

        double respuesta = Math.sqrt((Math.pow((x2-x1), 2) + Math.pow((y2-y1), 2)));
        System.out.printf("La distancia entre (%.0f,%.0f) y (%.0f,%.0f) es: %f\n", x1, y1, x2, y2, respuesta);
    }
}

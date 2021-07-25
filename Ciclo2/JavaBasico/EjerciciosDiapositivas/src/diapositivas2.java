import java.util.Scanner;

public class diapositivas2 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        /* Dada una coordenada (x,y) que representa un punto en el plano cartesiano, construya un algoritmo que permita determinar a que cuadrante pertecene dicho punto*/
        System.out.println("Ejercicio 1");

        System.out.println("Digita una coordenada (x, y)");
        System.out.print("x: ");
        int x = Integer.parseInt(sc.nextLine());
        System.out.print("y: ");
        int y = Integer.parseInt(sc.nextLine());
        int cuadrante = encontrarCuadrante(x, y);

        if (cuadrante == 0){
            System.out.println("El punto no pertenece a ningun cuadrante");
        } else {
            System.out.printf("El punto pertenece al cuadrante %d\n", cuadrante);
        }

        /* Leer tres numeros enteros e imprimir el mayor */
        System.out.println("\nEjercicio 2");

        System.out.println("Digita 3 numeros");
        System.out.print("a: ");
        int a = Integer.parseInt(sc.nextLine());
        System.out.print("b: ");
        int b = Integer.parseInt(sc.nextLine());
        System.out.print("c: ");
        int c = Integer.parseInt(sc.nextLine());

        int resultado = encontrarMayor(a, b, c);
        System.out.println("El numero mayor es: " + resultado);

        /* Leer dos numeros enteros y determinar si la diferencia entre ambos es un divisor exacto de alguno de los dos numeros*/
        System.out.println("\nEjercicio 3");

        System.out.println("Digita 2 numeros");
        System.out.print("i: ");
        int i = Integer.parseInt(sc.nextLine());
        System.out.print("j: ");
        int j = Integer.parseInt(sc.nextLine());
        int diferencia = Math.abs(i-j);

        if(i % diferencia == 0 & j % diferencia == 0) {
            System.out.printf("La distancia (%d) entre ambos es divisor exacto de ambos numeros\n", diferencia);
        } else if (i % diferencia == 0){
            System.out.printf("La distancia (%d) entre ambos es un divisor exacto de %d\n", diferencia, i);
        } else if (i % diferencia == 0){
            System.out.printf("La distancia (%d) entre ambos es un divisor exacto de %d\n", diferencia, j);
        } else {
            System.out.printf("La distancia (%d) entre ambos no es divisor de ningun numero\n", diferencia);
        }
    }

    public static int encontrarCuadrante(int x, int y) {
        /* si x o y valen 0 no se podrá determinar el cuadrante*/
        if (x == 0 || y == 0) {
            return 0;
        } 
        
        /*Si x es mayor que 0 se determina si el punto pertenece al cuadrante 1 o 4 gracias a y. O todo lo contrario, si pertenece al cuadrante 2 o 3*/
        if (x > 0) {
            if (y > 0){
                return 1;
            } else {
                return 4;
            }  
        } else { 
            if (y > 0){
                return 2;
            } else {
                return 3;
            } 
        }
    }

    public static int encontrarMayor(int a, int b, int c) {
        if (a > b & a > c) {
            return a;
        } else if (b > a & b > c){
            return b;
        } else if (c > a & c > b){
            return c;
        } else {
            return a;
        }
    }
}

/* 
1) Написать программу вычисления n-ого треугольного числа.    
 */

public class Task1 {

    public static void main(String[] args) {
        System.out.print((int)triangularNumber(4));
    }

    public static double triangularNumber(int n) {

        if (n > 0) {
            return (n + 1) * (n * 0.5);
        } else
            return 0;
    }
}
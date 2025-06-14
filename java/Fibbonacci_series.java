import java.util.Scanner;
public class Fibbonacci_series {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the value of n: ");
        int n = scanner.nextInt();

        System.out.println("Fibonacci Series up to " + n + " numbers:");

        int fib1 = 0, fib2 = 1;

        for (int i = 0; i < n; i++) {
            System.out.print(fib1 + " ");
            int nextFib = fib1 + fib2;
            fib1 = fib2;
            fib2 = nextFib;
        }

        scanner.close();
    }
}


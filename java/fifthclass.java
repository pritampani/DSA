/*import java.util.*;
public class fifthclass {
    public static void main(String args[]) {
        Scanner sc =new Scanner(System.in);
        int a = sc.nextInt();
        Scanner sa =new Scanner(System.in);
        int b = sa.nextInt();


        //outer loop
        for (int i=1; i<=a; i++) {
            for(int j=1; j<=b; j++) {
                System.out.print("*");

            }System.out.println();
        }
    }
}*/


// /*import java.util.*;
// public class fifthclass {
//     public static void main(String args[]) {


//         int a=4;
//         int b=5;

//         for (int i=1; i<=a; i++) {
//             for (int j=1; j<=b; j++ ) {
//                 if(i==1 || j==1 || i==a || j==b) {
//                     System.out.print("*");
//                 } else {
//                     System.out.print(" ");
//                 }
//             }
//             System.out.println();

//         }   
//     }
// }*/



import java.util.*;

/*import java.util.*;

public class fifthclass {
    public static void main(String args[]) {
        Scanner sc =new Scanner(System.in);
        int a=sc.nextInt();
        for (int i=1; i<=a; i++) {
            for (int j=1; j<=i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}*/


/*public class fifthclass {
    public static void main (String args[]) {
        Scanner sc= new Scanner(System.in);
        int a = sc.nextInt();
        for (int i=a; i>=1; i--) {
            for (int j=1; j<=i; j++) {
                System.out.print("*");
        `                }
            System.out.println();
        }
    }
}*/

//WRITE A PROGRAM TO FIND THE LARGEST NUMBER

// import java.util.Scanner;
// public class fifthclass 
// {
//     public static void main(String[] args) 
//     {
//         int x, y, z;
//         Scanner s = new Scanner(System.in);
//         System.out.print("Enter the first number:")
//         x = s.nextInt();
//         System.out.print("Enter the second number:");
//         y = s.nextInt();
//         System.out.print("Enter the third number:");
//         z = s.nextInt();
//         if(x > y && x > z)
//         {
//             System.out.println("Largest number is:"+x);
//         }
//         else if(y > z)
//         {
//             System.out.println("Largest number is:"+y);
//         }
//         else
//         {
//             System.out.println("Largest number is:"+z);
//         }
 
//     }
// }




public class fifthclass {
    public static void main(String args[]) {
        Scanner sc =new Scanner(System.in);
        int a=sc.nextInt();
        System.out.println("Enter a number :");
        int count=0;
        if (a>100) {
            count=a+1;
            System.out.println(count);
        }
        else {
            count=a-1;
            System.out.println(count);
        }
        System.out.println();


    }
}














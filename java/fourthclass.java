// loops
// for loop
//do while loop
// for loop syntax
import java.util.*;

//counter++ counter + 1 ---> shortcut

// public class fourthclass {
//     public static void main (String args[]) {
//         for(int counter = 0; counter<100;counter=counter+1) {
//             System.out.println("sala bsdk");
//         }
        
//     }

// loop with condition

// import java.util.*;

// public class fourthclass {
//     public static void main (String args[]) {
//         Scanner sc = new Scanner(System.in);
//         int a=sc.nextInt();
//         if (a%2==0) {
//             for (int c=0;c<4;c=c+1){
//                 System.out.println("jor se bolo jay mata di");
//             }
//         }else {
//                 System.out.println("the number you habe enter is not divisible by 2");
                
//             }
//     }
// }

// get innput from user and show the multplication table of that number


// import java.util.*;
// public class fourthclass {
//     public static void main (String args[]) {
//         Scanner sc =new Scanner(System.in);
//         int num=sc.nextInt();
//         System.out.println("your multipaction table is here");
//         for(int c=0;c<11;c++) {
            
//             System.out.println(c*num);
//         }
//     }
// }


// DO WHILE LOOP to print number 1 to 10

// public class fourthclass {
//     public static void main (String args[]) {
//         int i=0;
//         do {
//             System.out.println(i);
//             i++;

//         }while(i<11);
//     }
// }


// use of while looop

// import java.util.*;

// public class fourthclass {
//     public static void main (String args[]) {
//         int i=12;
//         Scanner sc =new Scanner(System.in);
//         int a=sc.nextInt();
//         while (i<0) {
//             System.out.println(a*i);
//             i++;
//         }

//     }
// }




// using do while loop 

// public class fourthclass {
//     public static void main(String args[]) {
//         int i=12;
//         while(i<11) {
//             System.out.println("yes bro");

//         }
//         do {
//             System.out.println("yes bro");
//         }while(i<11);
//     }
// }

import java.util.*;

public class fourthclass {
    public static void main (String args[]) {
        Scanner sc=new Scanner(System.in);
        int n = sc.nextInt();
        int sum =0;
        for (int i=0;i<=n;i++) {
            sum = sum + i;  
        }
        System.out.println(sum);

    }
}























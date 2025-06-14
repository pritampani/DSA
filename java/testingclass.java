// // class testingclass {
// //     public static void main(String[] args) {
// //         System.out.println("chiku");

// //     }
// // }

// //*******************************************************************************************************************

// //Widening Casting
// // Widening casting is done automatically when passing a smaller size type to a larger size type:

// // public class testingclass {
// //   public static void main(String[] args) {
// //     int myInt = 9;
// //     double myDouble = myInt; // Automatic casting: int to double

// //     System.out.println(myInt);      // Outputs 9
// //     System.out.println(myDouble);   // Outputs 9.0
// //   }
// // }

// //***********************************************************************************************

// // Narrowing Casting

// // Narrowing casting must be done manually by placing the type in parentheses in front of the value:

// // public class Main {
// //   public static void main(String[] args) {
// //     double myDouble = 9.78d;
// //     int myInt = (int) myDouble; // Manual casting: double to int

// //     System.out.println(myDouble);   // Outputs 9.78
// //     System.out.println(myInt);      // Outputs 9
// //   }
// // }

// //*************************************************************************************************************

// // Java divides the operators into the following groups:

// //     Arithmetic operators
// //     Assignment operators
// //     Comparison operators
// //     Logical operators
// //     Bitwise operators

// // More String Methods
// // There are many string methods available, for example toUpperCase() and toLowerCase():

// //************************************************************************************************************

// //Random number 

// // public class testingclass {
// //     public static void main(String[] args) {
// //         int randomNum = (int)(Math.random() * 101);
// //         System.out.println(randomNum);
// //     }
// // }

// //******************************************************************************************************

// // The if Statement

// // Use the if statement to specify a block of Java code to be executed if a condition is true.
// // Syntax

// // if (condition) {
// // block of code to be executed if the condition is true
// // }

// //Example

// // if (20 > 18) {
// //   System.out.println("20 is greater than 18");
// // }

// //if,else statment

// // int time = 20;
// // if (time < 18) {
// //   System.out.println("Good day.");
// // } else {
// //   System.out.println("Good evening.");
// // }

// //The else if Statement

// //Use the else if statement to specify a new condition if the first condition is false

// //Syntax

// // if (condition1) {
// // block of code to be executed if condition1 is true
// // } else if (condition2) {
// // block of code to be executed if the condition1 is false and condition2 is true
// // } else {
// // block of code to be executed if the condition1 is false and condition2 is false
// // }

// //******************************************************************************************************

// //Java Short Hand If...Else (Ternary Operator)

// // Short Hand If...Else

// // There is also a short-hand if else, which is known as the ternary operator because it consists of three operands.

// // It can be used to replace multiple lines of code with a single line, and is most often used to replace simple if else statements:

// //Syntax
// //variable = (condition) ? expressionTrue :  expressionFalse;

// //Example

// //insted of writing this you can write this
// //           |
// //           |
// //           |
// // int time = 20;
// // if (time < 18) {
// //   System.out.println("Good day.");
// // } else {
// //   System.out.println("Good evening.");
// // }

// // you can write this
// //           |
// //           |
// // int time = 20;
// // String result = (time < 18) ? "Good day." : "Good evening.";
// // System.out.println(result);

// import java.util.*;

// class testingclass {
//    public static void main(String args[]) {
//       Scanner sc = new Scanner(System.in);
//       System.out.println("enter a string");
//       String str = sc.nextLine();
//       for (int i = str.length - 1; i >= 0; i--) {
//          System.out.print(str[i] + " ");
//       }
//    }
// }

import java.util.*;

class testingclass {
   public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      System.out.println("PLEASE ENTER A STRING");
      String str = sc.nextLine();
      int l = str.length();
      System.out.println(l);
      String s = "";
      char space = ' ';
      String x[] = str.split(" ");
      int len = x.length;
      for (int i = l - 1; i >= 0; i--) {
         if (str.charAt(i) == space) {
            s = s + " ";
         } else {
            s = s + str.charAt(i);
         }
      }

      System.out.println(s);
   }
}

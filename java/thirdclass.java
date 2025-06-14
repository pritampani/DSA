// use of if,else,else if,switch,break

/*import java.util.*;

public class thirdclass {
    public static void main(String args[]) {

        Scanner sc=new Scanner(System.in);
        int age = sc.nextInt();
        
        if (age>18) {
            System.out.println("adult");
        } else {
            System.out.println("not adult");
        }
    }
}*/

// to check the number the even or odd
/*import java.util.*;
public class thirdclass {
    public static void main( String args[]) {
        Scanner sc= new Scanner(System.in);
        int a=sc.nextInt();
        if (a%2==0){
            System.out.println("enter number is even");

        }else {
            System.out.println("enter number is odd ");
        } 
    }
}*/

// take two input from user as integer and compare them in the bases of this operator(<>=).

/*import java.util.*;
 public class thirdclass {
    public static void  main (String args[]) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        Scanner sa=new Scanner(System.in);
        int b=sa.nextInt();
        if (a==b) {
            System.out.println("both the number are equall ");

        // else if statment is used below

        }else {
            if (a>b) {
                System.out.println("a is greater then b");


            }else {
                System.out.println("b is greater than a");
            }
        }
    }
 }*/


 import java.util.*;

 public class thirdclass {
    public static void main( String args[]) {
        Scanner sc= new Scanner(System.in);
        int button = sc.nextInt();


        // if (button==1) {
        //     System.out.println("hello");

        // }else if (button==2) {
        //     System.out.println("namastay");

        
        // }else if(button==3) {
        //     System.out.println("bonjur");

        // }else {
        //     System.out.println("enter number is invlide");

        // }

        // use of switch bro.

        switch(button) {
            case 1: System.out.println("hello");
            break;
            case 2:System.out.println("namastay");
            break;
            case 3:System.out.println("chal nikal");
            break;
            default:System.out.println("abe galat number dala he");
            
        }   


    }
 } 
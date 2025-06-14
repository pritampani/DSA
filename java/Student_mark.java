import java.util.Scanner;

public class Student_mark {
    public static void main(String args[]){
        float sub1;
        Scanner sc = new Scanner(System.in);
        sub1=sc.nextFloat();
        float sub2;
        Scanner sa = new Scanner(System.in);
        sub2=sa.nextFloat();
        float sub3;
        Scanner sb = new Scanner(System.in);
        sub3=sb.nextFloat();
        float sub4;
        Scanner sd = new Scanner(System.in);
        sub4=sd.nextFloat();
        float sub5;
        Scanner se = new Scanner(System.in);
        sub5=se.nextFloat();
        float total = sub1+sub2+sub3+sub4+sub5;
        if (total<500  ){
            System.out.println("condition is working");
        }
        else{
            System.out.println("else confition is working");
        }
    }    
}

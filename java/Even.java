import java.util.Scanner;
public class Even {
    public static void main(String args[]){
        
        float num;
        Scanner sc = new Scanner(System.in);
        num=sc.nextFloat();
        if (num%2==0){
            System.out.println("condition is working");
        }
        else{
            System.out.println("else confition is working");
        }
    }
    
}





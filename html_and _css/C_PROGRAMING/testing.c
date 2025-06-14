// #include<stdio.h>

// int main()
// {
//     printf("hello world");
// }


// void main()
// {
//     int a,b,sum;
//     a=10; b=20;
//     sum=a+b;
//     printf("sum is %d",sum);
// }

// void main()
// {
//     int a,b,sum;
//     system("cls");

//     a=10; b=20;
//     sum=a+b;
//     printf("sum is %d",sum);
//     getche();
// }

// void main()
// {
//     int a,b,sum;
//     printf("enter value of a");
//     scanf( %d")
//     system("cls");

//     a=10; b=20;
//     sum=a+b;
//     printf("sum is %d",sum);
//     getche();
// }

// int main()
// {
//     printf("\a");
// }

// int main()
// {
//     int x,y;
//     x=10,y=10;
//     printf("%d",x==y);
// }

// //to find the avrage of three number

// #include<stdio.h>

// int main()
// {
//     int a,b,c;
//     printf("enter a number");
//     scanf("%d",&a);
//     printf("enter a number");
//     scanf("%d",&b);
//     printf("enter a number");
//     scanf("%d",&c);

//     printf("avrage of  three number are %d ",(a+b+c)/3);
// }

// #include<stdio.h>
// int main()
// {
//     int marks;
//     printf("enter marks");
//     scanf("%d",&marks);
//     if(marks>50);
//     {
//         printf("resulr is pass");
//     }
// }

// #include<stdio.h>
// int main()
// {
//     int marks;
//     printf("enter marks");
//     scanf("%d",&marks);
//     if(marks>=50)
//     {
//         printf("result is pass");
//     }
//     else
//     {
//         printf("result is fail");
//     }
// }

// #include<stdio.h>
// int main()
// {
//     int number;
//     printf("enter the number ");
//     scanf("%d",&number);
//     if (number%2==0)
//     {
//         printf("even number");
//     }
//     else
//     {
//         printf("odd number");
//     }   
// return 0;
// }

// #include<stdio.h>
// int main()
// {
//     int marks;
//     printf("enter marks");
//     scanf("%d",&marks);
    
//     if (marks>=50)
//     {
//         printf("result is pass\n");
//         if (marks>90)
//         {
//             printf("grade A\n");
//         }
//         else 
//         {
//             printf("grade B\n");
//         }
//     }
//     else 
//     {
//         printf("result is fail\n");
//     }
// }

// #include<stdio.h>
// int main()
// {
//     int a,b;
//     printf("enter the number :");
//     scanf("%d",&a);
//     scanf("%d",&b);

//     if (a>=b)
//     {
//         printf("a is greater\n");
//         if (a==b)
//         {
//             printf("equal\n");
//         }
//         else
//         {
//             printf("not equal\n");
//         }
//     }
//     else
//     {
//         printf("b is greater");
//     }
// }


// #include<stdio.h>
// int main()
// {
//     int a;
//     printf("enter a number : ");
//     scanf("%d",&a);
//     if(a%2==0){ 
//     printf("the number is even");
//     }
//     else{
//     printf("the number is odd");
//     }
//     return 0;
// }



// #include<stdio.h>
// int main ()
// {
//    char month;
//    printf("enter your choice:\n 1.january,march,may,july,august,oct,dec\n 2.feb\n 3.april,june,sep,nov");
//    printf("enter the choice of month you want to know of : ");
//    scanf("%d",&month);
//    switch(month)
//    {
//     case 1: 
//     printf("this month have 31 days");
//     break;

//     case 2: 
//     printf("this month has only 28 days");
//     break;

//     case 3:
//     printf("this month has only 30 days ");
//     break;

//     default:
//     printf("there is an error");
//    }
//    return 0;
// }



// #include<stdio.h>
// int main(){
//     int i=0;
//     while(i<=10)
//     {
//         printf("%d",i);
//         i++;
       
//     }
// }



// #include <stdio.h>

// int main() {
//     int rows = 5; // Number of rows in the pattern

//     for (int i = 1; i <= rows; i++) {
//         // Print spaces for each row
//         for (int j = 1; j <= rows; j++) {
//             printf(" ");
//         }

//         // Print numbers for each row
//        for (int k = 1; k <= i; k++) {
//             printf("*");
//         } 

//         printf("\n"); // Move to the next line
//     }

//     return 0;
// }


// #include <stdio.h>
// int main() {
//     int num, originalNum, remainder, result = 0;
//     printf("Enter a three-digit integer: ");
//     scanf("%d", &num);
//     originalNum = num;

//     while (originalNum != 0) {
//         remainder = originalNum % 10; 
//         result += remainder * remainder * remainder;
//         originalNum /= 10;
//     }
//     if (result == num){
//         printf("%d is an Armstrong number.", num);
//     }
//     else{
//         printf("%d is not an Armstrong number.", num);
//     return 0;
//     }
// }


// #include<stdio.h>
// int main(){
//     int num;
//     printf("Enter a number:");
//     scanf("%d",&num);

//     for(int i=0;i<=num;i++){
//         printf("%d",i);
//     }
// }


// #include <stdio.h>
// int main(){
//     int arr[100];
//     int n;
//     printf("Enter the size of array");
//     scanf("%d",&n);
//     printf("Enter arrrayt element :");
//     for (int i = 0;i<n;i++){
//         scanf("%d",&arr[i]);

//     }
//     printf("Reverse array");
//     for(int i =n-1;i>=0;i--){
//         printf("%d",arr[i]);

//     }
    
// }







// #include <stdio.h>

// int main() {
//     int rows; // Number of rows in the pattern
//     printf("enter a numbr rows");
//     scanf("%d",&rows);
//     for (int i = 1; i <= rows; i++) {
//         // Print spaces for each row
//         for (int j = 1; j <= rows; j++) {
//             printf("");
//         }

//         // Print numbers for each row
//        for (int k = 1; k <= i; k++) {
//             printf( "*");
//         } 

//         printf("\n"); // Move to the next line
//     }

//     return 0;
// }



// #include <stdio.h>
// int main(){
//     int arr[100];
//     int n;
//     printf("Enter the size of array");
//     scanf("%d",&n);
//     printf("Enter array element :");
//     for (int i = 0;i<n;i++){
//         scanf("%d",&arr[i]);
//         }
//     for (int i = 0;i<n;i++){
//         if(arr[i]%2==1);
//     }
    

    // #include <stdio.h>  
    // int main()  
    // {  
    //     int n,m=1;  
    //     printf("Enter the number of rows");  
    //     scanf("%d",&n);  
    //    for(int i=n;i>=1;i--)  
    //    {  
    //        for(int j=1;j<m;j++)  
    //        {  
    //            printf(" ");  
    //        }  
    //        for(int k=1;k<=2*i-1;k++)  
    //        {  
    //            printf("*");  
    //        }  
    //        m++;  
         
    //       printf("\n");  
    //     }  
    //     return 0;  
    // }  







// #include<stdio.h>

// int main(){
//     int num;
//     printf("Enter a number:");
//     scanf("%d",&num);
//     int i=0;
//     while (i<num+1){
//         printf("%d",i);
//         i++;
//     }
    
// }



// #include <stdio.h>

// int main() {
//     int size;
//     printf("Enter the size of the array: ");
//     scanf("%d", &size);

//     int arr[size];
//     int *ptr;

//     printf("Enter the elements of the array:\n");
//     for (int i = 0; i < size; i++) {
//         scanf("%d", &arr[i]);
//     }

//     ptr = arr;  

//     printf("Elements of the array:\n");
//     for (int i = 0; i < size; i++) {
//         printf("%d ", *ptr);  
//         ptr++;  
//     }

//     return 0;
// }


// #include <stdio.h>
// #include <string.h>

// int isPalindrome(char *str) {
//     int len = strlen(str);
//     char *start = str;
//     char *end = str + len - 1;

//     while (start < end) {
//         if (*start != *end) {
//             return 0;  // Not a palindrome
//         }

//         start++;
//         end--;
//     }

//     return 1;  // Palindrome
// }

// int main() {
//     char str[100];
//     printf("Enter a string: ");
//     scanf("%s", str);

//     if (isPalindrome(str)) {
//         printf("The string is a palindrome.\n");
//     } else {
//         printf("The string is not a palindrome.\n");
//     }

//     return 0;
// }


// #include<stdio.h>

// int main(){
//     int rows= 5;
//     int i,j;
//     for(i=1;i<=rows;i++){
//         for (j=1; j <= i; j++)
//         {
//             printf("%d",j);
//         }
//         printf("\n");
//     } 
// }



// #include<stdio.h>

// float trgl(float base,float height){
//     float area = (base*height)/2;
//     return area;
// }

// int main(){
//     float base,height;
//     printf("Enter the base of the triangle");
//     scanf("%f",&base);
//     printf("Enter the height of the triangle");
//     scanf("%f",&height);
//     float area = trgl(base,height);
//     printf("area of the triangle is %.2f",area);
//     return 0;
// }






// #include <stdio.h>
// #include <string.h>
// void isPalindrome(char str[])
// {
//     int l = 0;
//     int h = strlen(str) - 1;
//     while (h > l)
//     {
//         if (str[l++] != str[h--])
//         {
//             printf("%s is not a palindrome\n", str);
//             return;
//         }
//     }
//     printf("%s is a palindrome\n", str);
// }
// int main()
// {
//     char str[100];
//     printf("Enter a string: ");
//     scanf("%s", str);
//     isPalindrome(str);
//     return 0;
// }

// #include <stdio.h>
// // Function to reverse the given number
// int rn(int num)
// {
//     int rev = 0;
//     while (num > 0)
//     {
//         rev = rev * 10 + num % 10;
//         num /= 10;
//     }
//     return rev;
// }
// // Function to check if a number is an Adam number
// int isAdamNumber(int num)
// {
//     int square = num * num;
//     int reverseSquare = rn(square);
//     int reverseNum = rn(num);
//     int reverseNumSquare = reverseNum * reverseNum;

//     return (reverseSquare == reverseNumSquare);
// }

// // Driver program to test above functions
// int main()
// {
//     int num;
//     printf("Enter a number: ");
//     scanf("%d", &num);
//     if (isAdamNumber(num))
//         printf("%d is an Adam number.\n", num);
//     else
//         printf("%d is not an Adam number.\n", num);
//     return 0;
// }




    // #include<stdio.h>  
    // int main()    
    // {    
    //  int i,fact=1,number;    
    //  printf("Enter a number: ");    
    //   scanf("%d",&number);    
    //     for(i=1;i<=number;i++){    
    //       fact=fact*i;    
    //   }    
    //   printf("Factorial of %d is: %d",number,fact);    
    // return 0;  
    // }   


// #include<stdio.h>
// int main(){
//     int n=5;
//     for(int i=1; i<=n; i++){
//          for (int j=1; j<=i; j++){
//             printf("%d",j);
//          }
//         printf("\n");  
//     }
//     for(int i=n-1;i>=1;i--){
//         for(int j=1;j<=i;j++){
//             printf("%d",j);
//         }
//         printf("\n");
//         }
// }



























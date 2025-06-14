// // wap to calculate the mean and standard deviation of the elements in the given 1-d array. The standard deviation measures the amount of variation or dispersion in the data set.

// #include<stdio.h>
// #include<math.h>
// int main(){
//     int array[5],i,sum=0,mean,d=0,sd,a,y=0;
//     for(i=0;i<=4;i+=1){
//         printf("Enter elemenets\n");
//         scanf("%d",&array[i]);
//         }
//     printf("\n");
//     for(i=0;i<=4;i+=1){
//         sum=sum+array[i];
//         printf("Element %d: %d\n",i+1,array[i]);
//         }
//         printf("\n");
//         mean=sum/5;
//         printf("sum=%d",sum);
//         printf("\n");
//         printf("mean=%d",mean);
//         printf("\n"); 
//         for(i=0;i<=4;i+=1){
//             d=(array[i]-mean);
//             a=pow(d,2);
//             y+=a;
//         }
//         int x=y/4;
//         sd=pow(x,0.5);
//         printf("standard deviation=%d",sd);
//         return 0;
// }



// Q2 Write a program to find the median of the elements in the given one dimensional array. The median is in the middle value of a sorted data set or the average of the two middle values for an even number of elements.

// #include <stdio.h>
// int main(){
//     int a,n,i,j;
//     printf("Number of elements to insert: ");
//     scanf("%d", &n);
//     int array[n];
//     for (i=0;i<n;i++){
//         printf("Enter element: ");
//         scanf("%d", &array[i]);
//     }
//     for (i=0;i<n;i++){
//         for (j=0;j<n-i;j++){
//             a = array[j+1];
//             if(array[j]>array[j+1]){
//                 array[j+1]=array[j];
//                 array[j]=a;
//             }
//         }        
//     }
//     if(n%2==0){
//         printf("Median:%d",(array[(n/2)-1]+array[(n/2)])/2);
//     }
//     else{
//         printf("Median:%d",array[n/2]);
//     }
//     return 0;
// }





// Q3 consider the array containing temperature data for a week(sunday to saturday)  temperature_data=[25,28,27,30,31,29,26] write a program to perfome the following tasks 
// A. find the average temperature for the week. 
// B. identify the hottest day(highest temperature) and the coldest day(lowest temperature) of the week. 
// C. calculate the temperature range (diffrence between the hottest and coldest days)

// #include <stdio.h>
// int main(){
//     int a,n,i,j,sum=0,mean;
//     int array[7]={25,28,27,30,31,29,26};
//     for (i=0;i<7;i++){
//         for (j=0;j<7-i;j++){
//             a = array[j+1];
//             if(array[j]>array[j+1]){
//                 array[j+1]=array[j];
//                 array[j]=a;
//             }
//         }
//         sum=sum+array[i];
//         }
//         mean=sum/7;
//         printf("Average Temp=%d",mean);
//         a=array[0];
//         n=array[6];
//         printf("\nLowest Temp:%d",a);
//         printf("\nHighest Temp:%d",n);
//         printf("\nDiffrence %d",n-a);        
//     return 0;
// }


// Q4

// #include <stdio.h>

// int main(){
//     int test_scores[20]={85,78,92,65,89,76,94,81,87,90,72,88,95,79,83,91,70,84,86,93}; 
//     float avg=0;
//     int pass=0,failed=0;
//     int highest = test_scores[0];
//     int gradeO=0, gradeE=0, gradeA=0, gradeB=0, gradeF=0;

//     for (int i = 0; i < 20; i++)
//     {
//         int currentMark = test_scores[i];        
//         avg+=currentMark;
        
//         if(highest<currentMark){highest=currentMark;}
//         if(currentMark>=60){pass++;}
//         else{failed++;}
//         if(currentMark>90){gradeO++;}
//         if(80<currentMark && currentMark<=90){gradeE++;}
//         if(70<currentMark && currentMark<=80){gradeA++;}
//         if(60<currentMark && currentMark<=70){gradeB++;}
//         if(currentMark<=60){gradeF++;}
//     }

//     printf("Average Marks: %.2f\nHighest Marks: %d\n\n", avg/20, highest);
//     printf("Pass: %d\nFailed: %d", pass, failed);
//     printf("\n\nGrades :-\n\n");
//     printf("Grade O:- %d\nGrade E:- %d\nGrade A:- %d\nGrade B:- %d\nGrade F:- %d", gradeO, gradeE, gradeA, gradeB, gradeF);
    
//     return 0;
// }
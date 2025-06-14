//write the basic initilazation of array

// #include <stdio.h>
// int main() {
//     int numbers[5] = {10, 20, 30, 40, 50};

//     printf("Element 0: %d\n", numbers[0]); 
//     printf("Element 1: %d\n", numbers[1]); 
//     printf("Element 2: %d\n", numbers[2]); 
//     printf("Element 3: %d\n", numbers[3]); 
//     printf("Element 4: %d\n", numbers[4]); 

//     return 0;
// }


// write the basic deceleration of array

// #include <stdio.h>
// int main() {
//     int numbers[5];
//     numbers[0] = 10;
//     numbers[1] = 20;
//     numbers[2] = 30;
//     numbers[3] = 40;
//     numbers[4] = 50;
//     printf("Element 0: %d\n", numbers[0]); 
//     printf("Element 1: %d\n", numbers[1]); 
//     printf("Element 2: %d\n", numbers[2]); 
//     printf("Element 3: %d\n", numbers[3]); 
//     printf("Element 4: %d\n", numbers[4]); 
//     return 0;
// }





// #include <stdio.h>
// int main() {
//     int i, n = 10;
//     int arr[n];
//     double sum = 0.0;

//     printf("Enter 10 elements:\n");
//     for (i = 0; i < n; i++) {
//         scanf("%d", &arr[i]);
//         sum += arr[i];
//     }

//     double mean = sum / n;
//     printf("Elements in the array: ");
//     for (i = 0; i < n; i++) {
//         printf("%d ", arr[i]);
//     }

//     printf("\nMean: %.2f\n", mean);

//     return 0;
// }





// write a program to calculate the mean and standed devation of the element in the given one diminisional array. the standed measure the amount of varation of deeperation in the data set in c
// #include <stdio.h>
// #include <math.h>

// double calculateMean(int arr[], int size) {
//     int sum = 0;
//     for (int i = 0; i < size; i++) {
//         sum += arr[i];
//     }
//     return (double)sum / size;
// }
// double calculateStandardDeviation(int arr[], int size, double mean) {
//     double sumOfSquaredDifferences = 0;
//     for (int i = 0; i < size; i++) {
//         double diff = arr[i] - mean;
//         sumOfSquaredDifferences += diff * diff;
//     }
//     return sqrt(sumOfSquaredDifferences / size);
// }

// int main() {
//     int size;
//     printf("Enter the size of the array: ");
//     scanf("%d", &size);

//     int arr[size];
//     printf("Enter %d elements:\n", size);
//     for (int i = 0; i < size; i++) {
//         scanf("%d", &arr[i]);
//     }

//     double mean = calculateMean(arr, size);
//     double standardDeviation = calculateStandardDeviation(arr, size, mean);

//     printf("Mean: %.2f\n", mean);
//     printf("Standard Deviation: %.2f\n", standardDeviation);

//     return 0;
// }   



//Write a program to find the median of the elements in the given one-dimensional array. The median is the middle value of a sorted data set or the average of the two middle values for an even number of elements.

// #include <stdio.h>
// int main(){
//     int a,n,i;
//     printf("Number of elements to insert: ");
//     scanf("%d", &n);
//     int array[n];
//     for (i=0;i<n;i++){
//         printf("Enter element: ");
//         scanf("%d", &array[i]);
//     }
//     if(n%2==0){
//         printf("Median:%d",(array[(n/2)-1]+array[(n/2)])/2);
//     }
//     else{
//         printf("Median:%d",array[n/2]);
//     }
//     return 0;
// }






// Consider the array containing temperature data for a week (Sunday to Saturday)temperature_data = [25, 28, 27, 30,
// 31, 29, 26]Write a program to perform the following tasks:
// • Find the average temperature for the week.
// • Identify the hottest day (highest temperature) and the coldest day (lowest temperature) of the week.
// • Calculate the temperature range (difference between the hottest and coldest days).


// #include <stdio.h>
// int main() {
//     int temperature_data[] = {25, 28, 27, 30, 31, 29, 26};
//     int num_days = sizeof(temperature_data) / sizeof(temperature_data[0]);
    
//     int total_temperature = 0;
//     for (int i = 0; i < num_days; i++) {
//         total_temperature += temperature_data[i];
//     }
//     double average_temperature = (double)total_temperature / num_days;
    
//     int hottest_day = 0, coldest_day = 0;
//     for (int i = 1; i < num_days; i++) {
//         if (temperature_data[i] > temperature_data[hottest_day]) {
//             hottest_day = i;
//         }
//         if (temperature_data[i] < temperature_data[coldest_day]) {
//             coldest_day = i;
//         }
//     }
    

//     int temperature_range = temperature_data[hottest_day] - temperature_data[coldest_day];
    
//     printf("Average Temperature: %.2f\n", average_temperature);
//     printf("Hottest Day: Day %d (Temperature: %d)\n", hottest_day + 1, temperature_data[hottest_day]);
//     printf("Coldest Day: Day %d (Temperature: %d)\n", coldest_day + 1, temperature_data[coldest_day]);
//     printf("Temperature Range: %d\n", temperature_range);
    
//     return 0;
// }






// Consider the array containing test scores of 20 studentstest_scores = [85, 78, 92, 65, 89, 76, 94, 81, 87, 90,72, 88,
// 95, 79, 83, 91, 70, 84, 86, 93]
// Write a C program to:
// • Calculate the average score and the highest score achieved.
// • Count the number of students who passed (scored above a certain passing threshold) and the number of
// students who failed.
// • Determine the grade distribution, i.e., count the number of students falling into different grade ranges (e.g., O,
// E, A, B, F).



// #include <stdio.h>
// int main() {
//    int test_scores[] = {85, 78, 92, 65, 89, 76, 94, 81, 87, 90, 72, 88, 95, 79, 83, 91, 70, 84, 86, 93};
//    int num_students = sizeof(test_scores) / sizeof(test_scores[0]);
//    int total_score = 0;
//    int highest_score = test_scores[0];
//    for (int i = 0; i < num_students; i++) {
//        total_score += test_scores[i];
//        if (test_scores[i] > highest_score) {
//            highest_score = test_scores[i];
//        }
//    }
//    double average_score = (double)total_score / num_students;
   
//    int passing_threshold = 70; 
//    int num_passed = 0, num_failed = 0;
//    for (int i = 0; i < num_students; i++) {
//        if (test_scores[i] >= passing_threshold) {
//            num_passed++;
//        } else {
//            num_failed++;
//        }
//    }
   
//    int grade_distribution[5] = {0}; 
//    for (int i = 0; i < num_students; i++) {
//        int grade = (test_scores[i] - 50) / 10; 
//        if (grade > 5) {
//            grade = 5; 
//        }
//        grade_distribution[grade]++;
//    }
   
//    printf("Average Score: %.2f\n", average_score);
//    printf("Highest Score: %d\n", highest_score);
//    printf("Number of Students Passed: %d\n", num_passed);
//    printf("Number of Students Failed: %d\n", num_failed);
//    printf("Grade Distribution:\n");
//    printf("  F: %d\n", grade_distribution[0]);
//    printf("  E: %d\n", grade_distribution[1]);
//    printf("  D: %d\n", grade_distribution[2]);
//    printf("  C: %d\n", grade_distribution[3]);
//    printf("  B: %d\n", grade_distribution[4]);
//    printf("  A: %d\n", grade_distribution[5]);
   
//    return 0;
// }




// #include <stdio.h>
// void printArray(int rows, int cols, int arr[rows][cols]) {
//     for (int i = 0; i < rows; i++) {
//         for (int j = 0; j < cols; j++) {
//             printf("%d ", arr[i][j]);
//         }
//         printf("\n");
//     }
// }

// int main() {
//     int row1=3, cols1=3;
//     int row2 = 3 , cols2 = 3;
//     int row = 3, cols = 3;
//     int array1[row1][cols1];
//     int array2[row2][cols2];
//     int sum[row][cols];

//     printf("Enter the elements of the array 1:\n");
//     for (int i = 0; i < row1; i++) {
//         for (int j = 0; j < cols2; j++) {
//             scanf("%d", &array1[i][j]);
//         }
//     }

//     printf("Enter the elements of the array 2:\n");
//     for (int i = 0; i < row2; i++) {
//         for (int j = 0; j < cols2; j++) {
//             scanf("%d", &array2[i][j]);
//         }
//     }

//         for (int i = 0; i < 3; i++) {
//         for (int j = 0; j < 3; j++) {
//             sum[i][j] = array1[i][j] + array2[i][j];
//         }
//     }
//     printArray(row, cols, sum);

//     return 0;
// }


// #include <stdio.h>
// void printArray(int rows, int cols, int arr[rows][cols]) {
//     for (int i = 0; i < rows; i++) {
//         for (int j = 0; j < cols; j++) {
//             printf("%d ", arr[i][j]);
//         }
//         printf("\n");
//     }
// }

// int main() {
//     int row1=3, cols1=3;
//     int array1[row1][cols1];
//     int sum = 0;


//     printf("Enter the elements of the array 1:\n");
//     for (int i = 0; i < row1; i++) {
//         for (int j = 0; j < cols1; j++) {
//             scanf("%d", &array1[i][j]);
//         }
//     }

//         for (int i = 0; i < 3; i++) {
//         for (int j = 0; j < 3; j++) {
//             sum=sum + array1[i][j] ;
//         }
//     }
//     printf("%d",sum);

//     return 0;
// }



// #include <stdio.h>
// 
// int main() {
//     int array1[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
//     int array2[3][3] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
//     int sumArray[3][3];
//     int transposeArray[3][3];
// 
//     for (int i = 0; i < 3; i++) {
//         for (int j = 0; j < 3; j++) {
//             sumArray[i][j] = array1[i][j] + array2[i][j];
//         }
//     }
// 
//     for (int i = 0; i < 3; i++) {
//         for (int j = 0; j < 3; j++) {
//             transposeArray[i][j] = sumArray[j][i];
//         }
//     }
// 
//     printf("Transpose of the sum array:\n");
//     for (int i = 0; i < 3; i++) {
//         for (int j = 0; j < 3; j++) {
//             printf("%d ", transposeArray[i][j]);
//         }
//         printf("\n");
//     }
// 
//     return 0;
// }
// 

//1
// #include <stdio.h>
// #include <stdlib.h>
// #define MAX_SIZE 10

// int stack[MAX_SIZE];
// int top = -1;

// void initialize() {
//     top = -1;
// }

// int isEmpty() {
//     return top == -1;
// }

// int isFull() {
//     return top == MAX_SIZE - 1;
// }

// void push(int value) {
//     if (isFull()) {
//         printf("Stack overflow\n");
//         return;
//     }
//     stack[++top] = value;
// }

// int pop() {
//     if (isEmpty()) {
//         printf("Stack underflow\n");
//         return -1;
//     }
//     return stack[top--];
// }

// int peek() {
//     if (isEmpty()) {
//         printf("Stack is empty\n");
//         return -1;
//     }
//     return stack[top];
// }

// void display() {
//     if (isEmpty()) {
//         printf("Stack is empty\n");
//         return;
//     }
//     printf("Stack contents: ");
//     for (int i = 0; i <= top; i++) {
//         printf("%d ", stack[i]);
//     }
//     printf("\n");
// }

// int main() {
//     initialize();

//     push(6);
//     push(7);
//     push(8);
//     push(5);
//     push(3);

//     printf("After pushing 6, 7, 8, 5, 3:\n");
//     display();

//     pop();

//     printf("After popping one element:\n");
//     display();

//     push(10);

//     printf("After pushing 10:\n");
//     display();

//     pop();
//     pop();

//     printf("After popping two elements:\n");
//     display();

//     return 0;
// }


//3
// #include <stdio.h>
// #include <string.h>

// #define MAX_SIZE 100

// int top = -1;
// char stack[MAX_SIZE];

// void push(char value) {
//     if (top == MAX_SIZE - 1) {
//         printf("Stack overflow\n");
//         return;
//     }
//     stack[++top] = value;
// }

// char pop() {
//     if (top == -1) {
//         printf("Stack underflow\n");
//         return '\0';
//     }
//     return stack[top--];
// }

// void reverseString(char *input) {
//     int length = strlen(input);
    
//     for (int i = 0; i < length; i++) {
//         push(input[i]);
//     }

//     for (int i = 0; i < length; i++) {
//         input[i] = pop();
//     }
// }

// int main() {
//     char input[MAX_SIZE];

//     printf("Enter a string: ");
//     fgets(input, sizeof(input), stdin);

//     input[strcspn(input, "\n")] = '\0';

//     printf("Original string: %s\n", input);

//     reverseString(input);

//     printf("Reversed string: %s\n", input);

//     return 0;
// }

//2
// #include <stdio.h>
// #define MAX_SIZE 10

// int stack[MAX_SIZE];
// int top = -1;

// void push(int value) {
//     if (top == MAX_SIZE - 1) {
//         printf("Stack overflow\n");
//         return;
//     }
    
//     top++;
//     stack[top] = value;
// }

// int pop() {
//     if (top == -1) {
//         printf("Stack underflow\n");
//         return -1;
//     }
    
//     int value = stack[top];
//     top--;
//     return value;
// }

// void display() {
//     if (top == -1) {
//         printf("Stack is empty\n");
//         return;
//     }
    
//     printf("Stack contents: ");
//     for (int i = top; i >= 0; i--) {
//         printf("%d ", stack[i]);
//     }
//     printf("\n");
// }

// int main() {
//     push(1);
//     push(2);
//     push(3);

//     printf("After pushing 1, 2, 3:\n");
//     display();

//     int poppedValue = pop();
//     printf("Popped value: %d\n", poppedValue);
    
//     printf("After popping one element:\n");
//     display();

//     push(4);

//     printf("After pushing 4:\n");
//     display();

//     return 0;
// }
 


#include<stdio.h>
#define MAX_SIZE 10
void enqueue(int queue[], int *rear, int value) {
    if (*rear == MAX_SIZE - 1) {
        printf("Queue is full. Cannot insert.\n");
        return;
    }
    *rear += 1;
    queue[*rear] = value;
    printf("%d inserted into the queue.\n", value);
}

void dequeue(int queue[], int *front, int rear) {
    if (*front > rear) {
        printf("Queue is empty. Cannot dequeue.\n");
        return;
    }
    printf("%d dequeued from the queue.\n", queue[*front]);
    *front += 1;
}

void traverse(int queue[], int front, int rear) {
    if (front > rear) {
        printf("Queue is empty.\n");
        return;
    }
    printf("Elements in the queue: ");
    for (int i = front; i <= rear; i++) {
        printf("%d ", queue[i]);
    }
    printf("\n");
}

int main() {
    int queue[MAX_SIZE];
    int front = 0, rear = -1;
    int choice, value;

    do {
        printf("\nQueue Operations:\n");
        printf("1. Insertion\n");
        printf("2. Deletion\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to enqueue: ");
                scanf("%d", &value);
                enqueue(queue, &rear, value);
                break;
            case 2:
                dequeue(queue, &front, rear);
                break;
            case 3:
                traverse(queue, front, rear);
                break;
            case 4:
                printf("Exiting the program.\n");
                break;
            default:
                printf("Invalid choice. Please enter a valid option.\n");
        }
    } while (choice != 4);

    return 0;
}









 
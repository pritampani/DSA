// #include<stdio.h>
// int main()
// {
//     int a,b;
//     printf("enter number is");
//     scanf("%d",&a);

//     printf("Enter number ");
//     scanf("%d",&b);

//     int sum  = a+b;
//     printf("summ of two number are %d",sum);


//     return 0;

// }

// #include <stdio.h>

// int main() {
//    int num1, num2, *ptr1, *ptr2;
   
//    printf("Enter two numbers: ");
//    scanf("%d %d", &num1, &num2);

//    ptr1 = &num1;
//    ptr2 = &num2;

//    if (*ptr1 > *ptr2) {
//       printf("%d is the maximum number\n", *ptr1);
//    } else {
//       printf("%d is the maximum number\n", *ptr2);
//    }

//    return 0;
// }


// #include <stdio.h>

// int main() {
//    char ch = 'a';
//    char *ptr = &ch;
   
//    printf("Alphabets from a to z are: \n");

//    while (*ptr <= 'z') {
//       printf("%c ", *ptr);
//       (*ptr)++;
//    }

//    return 0;
// }

// #include <stdio.h>

// int main() {
//    int arr[5] = {1, 2, 3, 4, 5};
//    int *ptr = arr + 4; 
   
//    printf("Array elements in reverse order are: ");

//    for (int i = 4; i >= 0; i--) {
//       printf("%d ", *ptr);
//       ptr--;
//    }

//    return 0;
// }



// #include <stdio.h>
// int main() {
//    char str[100], ch;
//    int frequency = 0, i;
//    printf("Enter a string: ");
//    fgets(str, sizeof(str), stdin);
//    printf("Enter a character to find its frequency: ");
//    scanf("%c", &ch);
//    for (i = 0; str[i] != '\0'; ++i) {
//       if (ch == str[i])
//          ++frequency;
//    }
//    printf("Frequency of %c = %d", ch, frequency);
//    return 0;
// }



// #include <stdio.h>
// #include <ctype.h> 
// int main() {
//    char str[100];
//    int vowels = 0, consonants = 0, i;
//    printf("Enter a string: ");
//    fgets(str, sizeof(str), stdin);
//    for (i = 0; str[i] != '\0'; ++i) {
//       if (isalpha(str[i])) { 
//          switch (tolower(str[i])) { 
//             case 'a':
//             case 'e':
//             case 'i':
//             case 'o':
//             case 'u':
//                ++vowels; 
//                break;
//             default:
//                ++consonants; 
//          }
//       }
//    }
//    printf("Vowels: %d\n", vowels);
//    printf("Consonants: %d", consonants);
//    return 0;
// }

//passing structure to a function
// #include <stdio.h>
// struct student
//     {
//     char Name[50];
//     int roll;
//     float marks;
//     }s[5];
// int main()
// {
//     int i;
//     printf("Enter information of students:\n");

//     // storing information
//     for (i = 0; i < 5; ++i)
//     {
//         s[i].roll = i + 1;
//         printf("\nFor roll number%d,\n", s[i].roll);
//         printf("Enter first name: ");
//         scanf("%s", s[i].Name);
//         printf("Enter marks: ");
//         scanf("%f", &s[i].marks);
//     }
//     //function call
//     GraceAndShow(s);//passing structure to a function
// }//ena of main
// //definetion of function
// void GraceAndShow(struct student *s)
// {
//     int i;
//     for (i = 0; i < 5; ++i)
//     {
//         if(s[i].marks<40.0)
//         {
//             s[i].marks=s[i].marks+5;
//         }
//     }

//     printf("Displaying Information:\n\n");
//     // displaying information
//     for (i = 0; i < 5; ++i)
//     {
//         printf("\nRoll number: %d\n", i + 1);
//         printf("First name: ");
//         puts(s[i].Name);
//         printf("Marks: %.1f", s[i].marks);
//         printf("\n");
//     }
// }

//passing structure to a function
// #include <stdio.h>
// int main()
// {
//     struct parent
//     {
//         int a;
//         int b;
//         struct nested
//         {
//             int c;
//             float d;
//         }n1;
//     };
//     struct parent p1={10,30,{7,9.9}};
//     printf("\n Parent structure variable a : %d",p1.a);
//     printf("\n Parent structure variable b : %d",p1.b);
//     printf("\n Nested structure variable c : %d",p1.n1.c);
//     printf("\n Nested structure variable d : %.1f",p1.n1.d);
// }


// #include <stdio.h>
// int main()
// {
//     struct student
//     {
//         char name[20];
//         int roll;
//         struct performance
//         {
//             float cgpa;
//             float project_score;
//             char award[20];
//         }n1;
//     };
//     struct student p1={"pritam",220,{7,9.9,"Gold"}};
//     printf("\n Parent structure variable name : %s",p1.name);
//     printf("\n Parent structure variable roll : %d",p1.roll);
//     printf("\n Nested structure variable cgpa : %.1f",p1.n1.cgpa);
//     printf("\n Nested structure variable project_score : %.1f",p1.n1.project_score);
//     printf("\n Nested structure variable award : %s",p1.n1.award);
// }





// #include <stdio.h> 
// #include <math.h>

// // Function to check if a number is an Adam number
// int isAdamNumber(int num) {
//     int square = num * num;
//     int reverse = 0;
//     int originalNum = num;

//     // Reverse the digits of the square
//     while (square != 0) {
//         int digit = square % 10;
//         reverse = reverse * 10 + digit;
//         square /= 10;
//     }

//     // Calculate the square of the reversed number
//     int reverseSquare = reverse * reverse;

//     return (reverseSquare == originalNum);
// }

// int main() {
//     int num;

//     printf("Enter a number: ");
//     scanf("%d", &num);

//     if (isAdamNumber(num))
//         printf("%d is an Adam number.\n", num);
//     else
//         printf("%d is not an Adam number.\n", num);

//     return 0;
// }


// #include <stdio.h>
// struct Student {
//     char name[50];
//     int age;
//     int rollNumber;
// };
// int main() {
//     struct Student students[3];
//     for (int i = 0; i < 3; i++) {
//         printf("Enter details for student %d:\n", i + 1);
//         printf("Name: ");
//         scanf("%s", students[i].name);
//         printf("Age: ");
//         scanf("%d", &students[i].age);
//         printf("Roll Number: ");
//         scanf("%d", &students[i].rollNumber);
//         printf("\n");
//     }
//     printf("Student Information:\n");
//     for (int i = 0; i < 3; i++) {
//         printf("Student %d:\n", i + 1);
//         printf("Name: %s\n", students[i].name);
//         printf("Age: %d\n", students[i].age);
//         printf("Roll Number: %d\n", students[i].rollNumber);
//         printf("\n");
//     }

//     return 0;
// }

// #include <stdio.h>
// struct Distance {
//     int feet;
//     int inches;
// };
// struct Distance addDistances(struct Distance d1, struct Distance d2) {
//     struct Distance sum;
//     sum.feet = d1.feet + d2.feet;
//     sum.inches = d1.inches + d2.inches;
//     if (sum.inches >= 12) {
//         sum.feet += sum.inches / 12;
//         sum.inches = sum.inches % 12;
//     }
//     return sum;
// }
// int main() {
//     struct Distance distance1, distance2, totalDistance;
//     printf("Enter distance 1:\n");
//     printf("Feet: ");
//     scanf("%d", &distance1.feet);
//     printf("Inches: ");
//     scanf("%d", &distance1.inches);
//     printf("\n");
//     printf("Enter distance 2:\n");
//     printf("Feet: ");
//     scanf("%d", &distance2.feet);
//     printf("Inches: ");
//     scanf("%d", &distance2.inches);
//     printf("\n");
//     totalDistance = addDistances(distance1, distance2);
//     printf("Total distance: %d feet %d inches\n", totalDistance.feet, totalDistance.inches);

//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>
// struct Student {
//     char name[50];
//     int age;
//     int rollNumber;
// };
// int main() {
//     int numStudents;
//     printf("Enter the number of students: ");
//     scanf("%d", &numStudents);
//     struct Student *students = (struct Student *)malloc(numStudents * sizeof(struct Student));
//     if (students == NULL) {
//         printf("Memory allocation failed. Exiting program.\n");
//         return 1;
//     }
//     for (int i = 0; i < numStudents; i++) {
//         printf("Enter details for student %d:\n", i + 1);
//         printf("Name: ");
//         scanf("%s", students[i].name);
//         printf("Age: ");
//         scanf("%d", &students[i].age);
//         printf("Roll Number: ");
//         scanf("%d", &students[i].rollNumber);
//         printf("\n");
//     }
//     printf("Student Information:\n");
//     for (int i = 0; i < numStudents; i++) {
//         printf("Student %d:\n", i + 1);
//         printf("Name: %s\n", students[i].name);
//         printf("Age: %d\n", students[i].age);
//         printf("Roll Number: %d\n", students[i].rollNumber);
//         printf("\n");
//     }
//     free(students);
//     return 0;
// }

// #include <stdio.h>
// #include <stdlib.h>
// struct Student {
//     char name[50];
//     int age;
//     int rollNumber;
// };
// int main() {
//     int numStudents;
//     printf("Enter the number of students: ");
//     scanf("%d", &numStudents);
//     struct Student *students = (struct Student *)malloc(numStudents * sizeof(struct Student));
//     if (students == NULL) {
//         printf("Memory allocation failed. Exiting program.\n");
//         return 1;
//     }
//     for (int i = 0; i < numStudents; i++) {
//         printf("Enter details for student %d:\n", i + 1);
//         printf("Name: ");
//         scanf("%s", students[i].name);
//         printf("Age: ");
//         scanf("%d", &students[i].age);
//         printf("Roll Number: ");
//         scanf("%d", &students[i].rollNumber);
//         printf("\n");
//     }
//     FILE *file = fopen("students.txt", "w");
//     if (file == NULL) {
//         printf("Failed to open file. Exiting program.\n");
//         return 1;
//     }
//     for (int i = 0; i < numStudents; i++) {
//         fprintf(file, "Student %d:\n", i + 1);
//         fprintf(file, "Name: %s\n", students[i].name);
//         fprintf(file, "Age: %d\n", students[i].age);
//         fprintf(file, "Roll Number: %d\n", students[i].rollNumber);
//         fprintf(file, "\n");
//     }
//     fclose(file);
//     printf("Records saved successfully to students.txt file.\n");
//     free(students);
//     return 0;
// }


// #include <stdio.h>
// int main() {
//     FILE *file;
//     char filename[100], data[1000];
//     printf("Enter the filename: ");
//     scanf("%s", filename);
//     file = fopen(filename, "r");
//     if (file == NULL) {
//         printf("Unable to open the file.\n");
//         return 1;
//     }
//     fgets(data, sizeof(data), file);
//     printf("Data from file:\n");
//     printf("%s", data);
//     fclose(file);

//     return 0;
// }


// #include <stdio.h>
// int main() {
//     FILE *file = fopen("students.txt", "r");
//     if (file == NULL) {
//         printf("Failed to open file. Exiting program.\n");
//         return 1;
//     }
//     int ch;
//     int count = 0;
//     while ((ch = fgetc(file)) != EOF) {
//         if (count % 2 == 0) {
//             printf("%c", ch);
//         }
//         count++;
//     }
//     fclose(file);
//     return 0;
// }


// #include <stdio.h>
// int main() {
//     FILE *file;
//     char filename[100];
//     char ch;
//     printf("Enter the filename: ");
//     scanf("%s", filename);
//     file = fopen(filename, "r");
//     if (file == NULL) {
//         printf("File \"%s\" could not be opened.\n", filename);
//         return 1;
//     }
//     printf("Contents of the file:\n");
//     while ((ch = fgetc(file)) != EOF) {
//         printf("%c", ch);
//     }
//     fclose(file);

//     return 0;
// }


// #include <stdio.h>

// int main(int argc, char *argv[]) {
//     FILE *file;
//     char ch;

//     // Check if the filename is provided as a command line argument
//     if (argc != 2) {
//         printf("Usage: %s <filename>\n", argv[0]);
//         return 1;
//     }

//     // Open the file in read mode
//     file = fopen(argv[1], "r");

//     // Check if the file exists and can be opened
//     if (file == NULL) {
//         printf("File \"%s\" could not be opened.\n", argv[1]);
//         return 1;
//     }

//     // Read and display the contents of the file
//     printf("Contents of the file:\n");
//     while ((ch = fgetc(file)) != EOF) {
//         printf("%c", ch);
//     }

//     // Close the file
//     fclose(file);

//     return 0;
// }



// #include <stdio.h>

// // fibonacci() funtion definition
// int fibonacci(int num)
// {
//     if (num == 0)
//     {
//         return 0; 
//     }
    
//     else if (num == 1)
//     {
//         return 1; 
//     }
//     else
//     {
//         return fibonacci(num - 1) + fibonacci(num - 2);
//     }
// }

// int main()
// {
//     int num=10; 
//     // printf("Enter the number of elements to be in the series : ");
//     // scanf("%d", &num); 
//     int i;
//     for (i = 0; i < num; i++)
//     {
//         printf("%d, ", fibonacci(i)); 
//     }

//     return 0;
// }

// #include <stdio.h>

// float calculateTriangleArea(float base, float height) {
//     float area = (base * height) / 2;
//     return area;
// }

// int main() {
//     float base, height;
    
//     printf("Enter the base of the triangle: ");
//     scanf("%f", &base);
    
//     printf("Enter the height of the triangle: ");
//     scanf("%f", &height);
    
//     float area = calculateTriangleArea(base, height);
//     printf("The area of the triangle is: %.2f\n", area);
    
//     return 0;
// }


#include <stdio.h>
#include <stdlib.h>

struct Node {
    int row;
    int col;
    int value;
    struct Node* next;
};

struct Node* createNode(int row, int col, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->row = row;
    newNode->col = col;
    newNode->value = value;
    newNode->next = NULL;
    return newNode;
}

void addNode(struct Node** head, int row, int col, int value) {
    struct Node* newNode = createNode(row, col, value);
    if (*head == NULL) {
        *head = newNode;
    } else {
        struct Node* current = *head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
    }
}

void displaySparseMatrix(struct Node* head, int numRows, int numCols) {
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < numCols; j++) {
            struct Node* current = head;
            int found = 0;
            while (current != NULL) {
                if (current->row == i && current->col == j) {
                    printf("%d ", current->value);
                    found = 1;
                    break;
                }
                current = current->next;
            }
            if (!found) {
                printf("0 ");
            }
        }
        printf("\n");
    }
}

int main() {
    int numRows = 4;
    int numCols = 5;

    struct Node* sparseMatrix = NULL;

    addNode(&sparseMatrix, 0, 2, 3);
    addNode(&sparseMatrix, 0, 4, 4);
    addNode(&sparseMatrix, 1, 2, 5);
    addNode(&sparseMatrix, 1, 3, 7);
    addNode(&sparseMatrix, 3, 1, 2);
    addNode(&sparseMatrix, 3, 2, 6);

   displaySparseMatrix(sparseMatrix, numRows, numCols);

 
    while (sparseMatrix != NULL) {
        struct Node* temp = sparseMatrix;
        sparseMatrix = sparseMatrix->next;
        free(temp);
    }

    return 0;
}






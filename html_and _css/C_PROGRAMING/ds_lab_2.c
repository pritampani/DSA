// Q1
// #include<stdio.h>
// int main(){
//     int x,y,i,j,a=0;
//     printf("Enter row: ");
//     scanf("%d",&x);
//     printf("Enter column: ");
//     scanf("%d",&y);
//     int array[x][y];
//     for(i=0;i<x;i++)
//     {
//         for(j=0;j<y;j++)
//         {
//             printf("Enter element (%d,%d): ",i,j);
//             scanf("%d",&array[i][j]);
//         }
//     }
//     for(i=0;i<x;i++)
//     {
//         for(j=0;j<y;j++)
//         {
//             printf("Element %d,%d :%d\n",i,j,array[i][j]);
//             a+=array[i][j];            
//         }
//     }
//     printf("\nSum is %d",a);
//     return 0;
// }




// Q2

// #include<stdio.h>
// void transpose()
// {
//     int i,j,x,y,a;
//     printf("Enter row: ");
//     scanf("%d",&x);
//     printf("Enter column: ");
//     scanf("%d",&y);
//     int array1[x][y];
//     int array2[y][x];
//     for(i=0;i<x;i++)
//     {
//         for(j=0;j<y;j++)
//         {
//             printf("Enter element (%d,%d): ",i,j);
//             scanf("%d",&array1[i][j]);
//         }
//     }
//     for(i=0;i<x;i++)
//     {
//         for(j=0;j<y;j++)
//         {
//             array2[j][i]=array1[i][j];
//         }
//     }
//     for(i=0;i<y;i++)
//     {
//         for(j=0;j<x;j++)
//         {
//             printf("Element %d,%d :%d\n",i,j,array2[i][j]);
//         }
//     }
// }
// int main(){
//     transpose();    
//     return 0;
// }




// Q3 Write a C program to perform three tuple representation of sparse matrix and display all the elements.
// #include<stdio.h>
// int main()
// {
//     int x,y,i,j,count=0,size,a=0;
//     printf("Enter Row: ");
//     scanf("%d",&x);
//     printf("Enter Column: ");
//     scanf("%d",&y);
//     int array[x][y];
//     for(i=0;i<x;i++)
//     {
//         for(j=0;j<y;j++)
//         {
//             printf("Enter Element(%d,%d): ",i,j);
//             scanf("%d",&array[i][j]);
//         }
//     }
//     size=x*y;
//     for(i=0;i<x;i++)
//     {
//         for(j=0;j<y;j++)
//         {
//             if(array[i][j]!=0)
//             {
//                 count+=1;
//             }
//         }
//     }
//     int three_tuple_rep[3][count];
//     if(count<size/2)
//     {
//         for(i=0;i<x;i++)
//         {
//             for(j=0;j<y;j++)
//             {
//                 if(array[i][j]!=0)
//                 {
//                     three_tuple_rep[0][a]=i;
//                     three_tuple_rep[1][a]=j;
//                     three_tuple_rep[2][a]=array[i][j];
//                     a+=1;
//                 }
//             }
//         }
//         for(i=0;i<3;i++)
//         {
//             for(j=0;j<count;j++)
//             {
//                 printf("%d ",three_tuple_rep[i][j]);
//             }
//             printf("\n");   
//         }
//     }
//     else
//     {
//         printf("\nThis is not a Sparse Matrix");
//     }
//     return 0;
// }



// Q4

// #include<stdio.h>
// int main()
// {
//     int i,j,k,n,m,p;
//     printf("Enter Row: ");
//     scanf("%d",&n);
//     printf("Enter Column: ");
//     scanf("%d",&m);
//     printf("Enter Height: ");
//     scanf("%d",&p);    
//     int array[n][m][p];
//     for(i=0;i<n;i++)
//     {
//         for(j=0;j<m;j++)
//         {
//             for(k=0;k<p;k++)
//             {
//                 printf("Enter Element(%d,%d): ",i,j,k);
//                 scanf("%d",&array[i][j][k]);
//             }
//         }
//     }
//     for(i=0;i<n;i++)
//     {
//         for(j=0;j<m;j++)
//         {
//             for(k=0;k<p;k++)
//             {
//                 printf("%d ",array[i][j][k]);
//             }
//             printf("\n");
//         }
//         printf("\n");
//     }
//     return 0;
// }


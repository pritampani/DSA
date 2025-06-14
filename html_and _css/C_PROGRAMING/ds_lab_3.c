// #include<stdio.h>
// #define SIZE 5
// int top=-1,stack[SIZE];
// void push(int a)
// {
//  if(top==SIZE-1)
//  {
//  printf("Stack Overflow\n");
//  }
//  else
//  {
//  top++;
//  stack[top]=a;
//  printf("%d inserted successfully at %d\n",a,top);
//  }
// }
// void pop()
// {
//  if(top!=-1)
//  {
//  printf("%d is removed from %d\n",stack[top],top);
//  top--;
//  }
//  else
//  {
//  printf("Underflow");
//  }
// }
// void peek()
// {
//  if(top!=-1)
//  {
//  printf("%d is topmost element\n",stack[top]);
//  }
//  else
//  {
//  printf("Underflow\n");
//  }
// } 
// void display()
// {
//  if(top==-1)
//  {
//  printf("Underflow\n");
//  }
//  else
//  {
//  for(int i=top;i>=0;i--)
//  {
//  printf("\n%d ",stack[i]);
//  }
//  }
// }
// int main()
// {
//  push(6);
//  push(7);
//  push(8);
//  push(5);
//  push(3);
//  pop();
//  push(10);
//  pop();
//  pop();
//  peek();
//  display();







// #include<stdio.h>
// #define SIZE 10
// int stack[SIZE],top=-1;
// void push()
// {
//  if(top==SIZE-1)
//  {
//  printf("Stack Overflow");
//  }
//  else
//  {
//  int n;
//  printf("Enter no of elements you want to enter upto 10: ");
//  scanf("%d",&n);
//  if(n>10)
//  {
//  printf("Invalid size\n");
//  }
//  else
//  {
//  for(int i=0;i<n;i++)
//  {
//  top++;
//  printf("Enter element for stack at position %d :",top);
//  scanf("%d",&stack[top]);
//  }
//  }
//  }
// }
// void display()
// {
//  if(top==-1)
//  {
//  printf("Underflow"); 
//  } 
//  else 
//  {
//  for(int i=top;i>=0;i--)
//  {
//  printf("\n%d ",stack[i]);
//  }
//  }
// }
// int main()
// {
//  push();
//  display();
//  return 0;
// }


// #include <stdio.h>
// int main(){
//  char str[]="ramit";
//  int size = sizeof(str)/sizeof(char);
//  int top = size-2;
//  char rev_str[100];
//  printf("Reversed String : ");
//  for (int i = top; i >= 0; i--)
//  {
//  rev_str[top-i]=str[i];
//  }
//  printf("%s", rev_str);
//  return 0;
// }



// #include<stdio.h>
// int fact(int n)
// {
//  if(n==0)
//  {
//  return 1;
//  }
//  else
//  {
//  return n * fact(n-1);
//  }
// }
// int main()
// {
//  int a;
//  printf("Enter a no u want to calculate the factorial: ");
//  scanf("%d",&a);
//  printf("Factorial of %d = %d",a,fact(a)); 
// }


// #include<stdio.h>
// #define MAX_SIZE 10
// void enqueue(int queue[], int *rear, int value) {
//     if (*rear == MAX_SIZE - 1) {
//         printf("Queue is full. Cannot insert.\n");
//         return;
//     }
//     *rear += 1;
//     queue[*rear] = value;
//     printf("%d inserted into the queue.\n", value);
// }

// void dequeue(int queue[], int *front, int rear) {
//     if (*front > rear) {
//         printf("Queue is empty. Cannot dequeue.\n");
//         return;
//     }
//     printf("%d dequeued from the queue.\n", queue[*front]);
//     *front += 1;
// }

// void traverse(int queue[], int front, int rear) {
//     if (front > rear) {
//         printf("Queue is empty.\n");
//         return;
//     }
//     printf("Elements in the queue: ");
//     for (int i = front; i <= rear; i++) {
//         printf("%d ", queue[i]);
//     }
//     printf("\n");
// }

// int main() {
//     int queue[MAX_SIZE];
//     int front = 0, rear = -1;
//     int choice, value;

//     do {
//         printf("\nQueue Operations:\n");
//         printf("1. Insertion\n");
//         printf("2. Deletion\n");
//         printf("3. Display\n");
//         printf("4. Exit\n");
//         printf("Enter your choice: ");
//         scanf("%d", &choice);

//         switch (choice) {
//             case 1:
//                 printf("Enter value to enqueue: ");
//                 scanf("%d", &value);
//                 enqueue(queue, &rear, value);
//                 break;
//             case 2:
//                 dequeue(queue, &front, rear);
//                 break;
//             case 3:
//                 traverse(queue, front, rear);
//                 break;
//             case 4:
//                 printf("Exiting the program.\n");
//                 break;
//             default:
//                 printf("Invalid choice. Please enter a valid option.\n");
//         }
//     } while (choice != 4);

//     return 0;
// }










// #include <stdio.h>
// #define MAX_SIZE 10
// int circularQueue[MAX_SIZE];
// int front = -1, rear = -1;
// void CQINSERT(int value) {
//     if ((rear + 1) % MAX_SIZE == front) {
//         printf("Circular queue is full. Cannot insert.\n");
//         return;
//     }
//     if (front == -1)
//         front = 0;
//     rear = (rear + 1) % MAX_SIZE;
//     circularQueue[rear] = value;
// }
// void CQDELETE() {
//     if (front == -1) {
//         printf("Circular queue is empty. Cannot delete.\n");
//         return;
//     }
//     printf("Deleted element: %d\n", circularQueue[front]);

//     if (front == rear)
//         front = rear = -1;
//     else
//         front = (front + 1) % MAX_SIZE;
// }
// int main() {
//     CQINSERT(10);
//     CQINSERT(20);
//     CQINSERT(30);

//     CQDELETE();
//     CQDELETE();

//     CQINSERT(40);

//     return 0;
// }



// #include <stdio.h>
// #include <stdlib.h>
// #define MAX_SIZE 100
// struct Stack {
//     int data[MAX_SIZE];
//     int top;
// };

// void initialize(struct Stack *stack) {
//     stack->top = -1;
// }


// int isEmpty(struct Stack *stack) {
//     return (stack->top == -1);
// }


// int isFull(struct Stack *stack) {
//     return (stack->top == MAX_SIZE - 1);
// }


// void PUSH(struct Stack *stack, int item) {
//     if (isFull(stack)) {
//         printf("Stack is full. Cannot push.\n");
//         return;
//     }
//     stack->data[++stack->top] = item;
// }


// int POP(struct Stack *stack) {
//     if (isEmpty(stack)) {
//         printf("Stack is empty. Cannot pop.\n");
//         return -1; 
//     }
//     return stack->data[stack->top--];
// }

// struct QueueUsingStacks {
//     struct Stack stack1;
//     struct Stack stack2; 
// };

// void initializeQueue(struct QueueUsingStacks *queue) {
//     initialize(&(queue->stack1));
//     initialize(&(queue->stack2));
// }

// void enqueue(struct QueueUsingStacks *queue, int item) {
//     PUSH(&(queue->stack1), item);
// }

// int dequeue(struct QueueUsingStacks *queue) {
//     if (isEmpty(&(queue->stack1)) && isEmpty(&(queue->stack2))) {
//         printf("Queue is empty. Cannot dequeue.\n");
//         return -1; 
//     }

//     if (isEmpty(&(queue->stack2))) {
//         while (!isEmpty(&(queue->stack1))) {
//             PUSH(&(queue->stack2), POP(&(queue->stack1)));
//         }
//     }

//     return POP(&(queue->stack2));
// }

// int main() {
//     struct QueueUsingStacks queue;
//     initializeQueue(&queue);

//     enqueue(&queue, 1);
//     enqueue(&queue, 2);
//     enqueue(&queue, 3);

//     printf("Dequeued item: %d\n", dequeue(&queue));

//     enqueue(&queue, 4);

//     printf("Dequeued item: %d\n", dequeue(&queue));
//     printf("Dequeued item: %d\n", dequeue(&queue));
//     printf("Dequeued item: %d\n", dequeue(&queue));

//     return 0;
// }


// Q1
// #include <stdio.h>
// #include <stdlib.h>
// struct link
// {
//     int info;
//     struct link *next;
// };
// void create(struct link *node);
// void display(struct link *node);
// struct link *insertAtAnyPosition(struct link *node);
// struct link *insertAtFirst(struct link *node);
// void main()
// {
//     struct link *node;
//     node = (struct link *)malloc(sizeof(struct link));
//     if (node == NULL)
//     {
//         printf("\n Memory is not allocated");
//         exit(0);
//     }
//     create(node);
//     printf("\n Before insertion.");
//     display(node);
//     struct link *newLink = insertAtAnyPosition(node);
//     printf("\n After insertion.");
//     display(newLink);
// }
// void create(struct link *node)
// {
//     char opt;
//     printf("\n Enter a value: ");
//     scanf("%d", &node->info);
//     node->next = NULL;
//     printf("\n Any more to entry(y/n): ");
//     scanf(" %c", &opt);
//     while (opt == 'Y' || opt == 'y')
//     {
//         node->next = (struct link *)malloc(sizeof(struct link));
//         if (node == NULL)
//         {
//             printf("\n Memory is not allocated");
//             exit(0);
//         }
//         node = node->next;
//         printf("\n Enter a value: ");
//         scanf("%d", &node->info);
//         node->next = NULL;
//         printf("\n Any more to entry(y/n): ");
//         scanf(" %c", &opt);
//     }
// }
// void display(struct link *node)
// {
//     while (node != NULL)
//     {
//         printf("\n%d", node->info);
//         node = node->next;
//     }
// }
// struct link *insertAtAnyPosition(struct link *node)
// {
//     struct link *temp1 = node;
//     int count = 1, pos, i;
//     while (temp1->next != NULL)
//     {
//         count++;
//         temp1 = temp1->next;
//     }
//     printf("\n Enter position to insert: ");
//     scanf("%d", &pos);
//     if (pos > count)
//     {
//         printf("\n This position is not available.");
//         exit(0);
//     }
//     struct link *curr = (struct link *)malloc(sizeof(struct
//                                                      link));
//     if (curr == NULL)
//     {
//         printf("\n Memory is not allocated");
//         exit(0);
//     }
//     struct link *temp2 = node;
//     if (pos == 0)
//     {
//         return (insertAtFirst(temp2));
//     }
//     else
//     {
//         printf("\n Enter a value for current node: ");
//         scanf("%d", &curr->info);
//         curr->next = NULL;
//         for (i = 1; i < pos; i++)
//         {
//             temp2 = temp2->next;
//         }
//         curr->next = temp2->next;
//         temp2->next = curr;
//     }
//     return node;
// }
// struct link *insertAtFirst(struct link *node)
// {
//     struct link *curr = (struct link *)malloc(sizeof(struct
//                                                      link));
//     if (curr == NULL)
//     {
//         printf("\n Memory is not allocated");
//         exit(0);
//     }
//     printf("\n Enter a value for current node: ");
//     scanf("%d", &curr->info);
//     curr->next = node;
//     node = curr;
//     return node;
// }






// Q2
// #include <stdio.h>
// #include <stdlib.h>
// struct Node
// {
//     int data;
//     struct Node *next;
// };
// struct Node *createNode(int data)
// {
//     struct Node *newNode = (struct Node *)malloc(sizeof(struct
//                                                         Node));
//     newNode->data = data;
//     newNode->next = NULL;
//     return newNode;
// }
// void insertEnd(struct Node **head, int data)
// {
//     struct Node *newNode = createNode(data);
//     if (*head == NULL)
//     {
//         *head = newNode;
//         return;
//     }
//     struct Node *temp = *head;
//     while (temp->next != NULL)
//     {
//         temp = temp->next;
//     }
//     temp->next = newNode;
// }
// int search(struct Node *head, int target)
// {
//     struct Node *current = head;
//     int position = 1;
//     while (current != NULL)
//     {
//         if (current->data == target)
//         {
//             return position;
//         }
//         current = current->next;
//         position++;
//     }
//     return -1;
// }
// void printList(struct Node *head)
// {
//     struct Node *current = head;
//     while (current != NULL)
//     {
//         printf("%d -> ", current->data);
//         current = current->next;
//     }
//     printf("NULL\n");
// }
// int main()
// {
//     struct Node *head = NULL;
//     insertEnd(&head, 10);
//     insertEnd(&head, 20);
//     insertEnd(&head, 30);
//     insertEnd(&head, 40);
//     insertEnd(&head, 50);
//     printf("Linked List: ");
//     printList(head);
//     int target;
//     printf("Enter value to be searched: ");
//     scanf("%d", &target);
//     int position = search(head, target);
//     if (position != -1)
//     {
//         printf("%d found at position %d\n", target, position);
//     }
//     else
//     {
//         printf("%d not found in the list\n", target);
//     }
//     return 0;
// }

//Q3
// #include <stdio.h>
// #include <stdlib.h>
// struct Node
// {
//     int data;
//     struct Node *next;
// };
// struct Node *createNode(int data)
// {
//     struct Node *newNode = (struct
//                             Node *)malloc(sizeof(struct Node));
//     newNode->data = data;
//     newNode->next = NULL;
//     return newNode;
// }
// void insertEnd(struct Node **head, int data)
// {
//     struct Node *newNode = createNode(data);
//     if (*head == NULL)
//     {
//         *head = newNode;
//         return;
//     }
//     struct Node *temp = *head;
//     while (temp->next != NULL)
//     {
//         temp = temp->next;
//     }
//     temp->next = newNode;
// }
// int findSum(struct Node *head)
// {
//     int sum = 0;
//     struct Node *current = head;
//     while (current != NULL)
//     {
//         sum += current->data;
//         current = current->next;
//     }
//     return sum;
// }
// void printList(struct Node *head)
// {
//     struct Node *current = head;
//     while (current != NULL)
//     {
//         printf("%d -> ", current->data);
//         current = current->next;
//     }
//     printf("NULL\n");
// }
// int main()
// {
//     struct Node *head = NULL;
//     insertEnd(&head, 10);
//     insertEnd(&head, 20);
//     insertEnd(&head, 30);
//     insertEnd(&head, 40);
//     insertEnd(&head, 50);
//     printf("Linked List: ");
//     printList(head);
//     int sum = findSum(head);
//     printf("Sum of all elements in the list: %d\n", sum);
//     return 0;
// }



#include <stdio.h>
#include <stdlib.h>

// Structure to represent a Node in the BT
struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
};

// Structure for a Stack Node
struct StackNode
{
    struct Node *data;
    struct StackNode *next;
};

// Structure for a Stack
struct Stack
{
    struct StackNode *top;
};

// Structure for a Queue Node
struct QueueNode
{
    struct Node *data;
    struct QueueNode *next;
};

// Structure for a Queue
struct Queue
{
    struct QueueNode *front;
    struct QueueNode *rear;
};

// Create a new Node
struct Node *createNode(int data)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Function to check if the stack is empty
int isEmpty(struct Stack *stack)
{
    return (stack->top == NULL);
}

// Create an empty stack
struct Stack *createStack()
{
    struct Stack *stack = (struct Stack *)malloc(sizeof(struct Stack));
    stack->top = NULL;
    return stack;
}

// Push a Node onto the Stack
void push(struct Stack *stack, struct Node *data)
{
    struct StackNode *newNode = (struct StackNode *)malloc(sizeof(struct StackNode));
    newNode->data = data;
    newNode->next = stack->top;
    stack->top = newNode;
}

// Pop a Node from the Stack
struct Node *pop(struct Stack *stack)
{
    if (stack->top == NULL)
        return NULL;
    struct StackNode *temp = stack->top;
    struct Node *data = temp->data;
    stack->top = temp->next;
    free(temp);
    return data;
}

// Create an empty queue
struct Queue *createQueue()
{
    struct Queue *q = (struct Queue *)malloc(sizeof(struct Queue));
    q->front = q->rear = NULL;
    return q;
}

// Enqueue a Node in the Queue
void enqueue(struct Queue *q, struct Node *data)
{
    struct QueueNode *newNode = (struct QueueNode *)malloc(sizeof(struct QueueNode));
    newNode->data = data;
    newNode->next = NULL;
    if (q->front == NULL)
    {
        q->front = q->rear = newNode;
    }
    else
    {
        q->rear->next = newNode;
        q->rear = newNode;
    }
}

// Dequeue a Node from the Queue
struct Node *dequeue(struct Queue *q)
{
    if (q->front == NULL)
        return NULL;
    struct QueueNode *temp = q->front;
    struct Node *data = temp->data;
    q->front = q->front->next;
    free(temp);
    return data;
}

// Search for a Node in the Binary Tree using a stack
struct Node *search(struct Node *root, int key)
{
    struct Stack *stack = createStack();
    push(stack, root);

    while (!isEmpty(stack))
    {
        struct Node *current = pop(stack);

        if (current->data == key)
        {
            return current;
        }

        if (current->left)
            push(stack, current->left);
        if (current->right)
            push(stack, current->right);
    }

    return NULL;
}

// Search for a Node in the Binary Tree using a queue
struct Node *searchQueue(struct Node *root, int key)
{
    if (root == NULL)
    {
        return NULL;
    }

    struct Queue *q = createQueue();
    enqueue(q, root);

    while (q->front)
    {
        struct Node *current = dequeue(q);

        if (current->data == key)
        {
            return current;
        }

        if (current->left)
        {
            enqueue(q, current->left);
        }
        if (current->right)
        {
            enqueue(q, current->right);
        }
    }

    return NULL;
}

int main()
{
    struct Node *root = createNode(10);
    root->left = createNode(35);
    root->right = createNode(5);
    root->left->left = createNode(2);
    root->left->right = createNode(71);
    root->right->left = createNode(12);
    root->right->right = createNode(18);
    printf("\n");

    printf("Search Operation using Stack and Queue \n");
    int choice;
    do
    {

        printf("\n");
        printf("1. Search using Stack\n");
        printf("2. Search using Queue\n");
        printf("3. Exiting...\n");
        printf("\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
        {
            int key;
            printf("Enter the key you want to search in a binary tree: ");
            scanf("%d", &key);
            struct Node *result = search(root, key);
            printf("Operation performed in Stack\n");
            if (result)
            {
                printf("Node with value %d found in the Binary Tree.\n", key);
            }
            else
            {
                printf("Node with value %d not found in the Binary Tree.\n", key);
            }
            printf("\n");
            break;
        }

        case 2:
        {
            int key;
            printf("Enter the key you want to search in a binary tree: ");
            scanf("%d",&key);
            struct Node *result1 = searchQueue(root, key);
            printf("Operation performed in Queue\n");
            if (result1)
            {
                printf("Node with value %d found in the Binary Tree.\n", key);
            }
            else
            {
                printf("Node with value %d not found in the Binary Tree.\n", key);
            }
            printf("\n");
            break;
        }

        case 3:
            printf("Exiting...");
            break;
        }

    } while (choice != 3);
    return 0;
}

// //1
// #include <stdio.h>
// #include <math.h>

// #define MAX_SIZE 10
// float calculateMean(int arr[], int size) {
//     int sum = 0;
//     for (int i = 0; i < size; ++i) {
//         sum += arr[i];
//     }
//     return (float)sum / size;
// }
// float calculateStandardDeviation(int arr[], int size, float mean) {
//     float sumOfSquares = 0;
//     for (int i = 0; i < size; ++i) {
//         sumOfSquares += pow(arr[i] - mean, 2);
//     }
//     return sqrt(sumOfSquares / size);
// }
// int main() {
//     int array[MAX_SIZE];
//     int size;

//     printf("Enter the size of the array (up to %d): ", MAX_SIZE);
//     scanf("%d", &size);

//     printf("Enter %d elements:\n", size);
//     for (int i = 0; i < size; ++i) {
//         printf("Element %d: ", i + 1);
//         scanf("%d", &array[i]);
//     }

//     float mean = calculateMean(array, size);
//     float standardDeviation = calculateStandardDeviation(array, size, mean);
//     printf("Mean: %.2f\n", mean);
//     printf("Standard Deviation: %.2f\n", standardDeviation);
//     return 0;
// }








#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 10

struct Queue {
    int front, rear;
    int items[MAX_SIZE];
};

void initializeQueue(struct Queue* q) {
    q->front = -1;
    q->rear = -1;
}

int isEmpty(struct Queue* q) {
    return q->front == -1;
}

int isFull(struct Queue* q) {
    return (q->rear == MAX_SIZE - 1) && (q->front == 0);
}

void enqueue(struct Queue* q, int value) {
    if (isFull(q)) {
        printf("Queue is full. Cannot enqueue.\n");
        return;
    }

    if (isEmpty(q)) {
        q->front = 1;
    }

    q->rear = (q->rear + 1) % MAX_SIZE;
    q->items[q->rear] = value;
    printf("%d enqueued to the queue.\n", value);
}

int dequeue(struct Queue* q) {
    if (isEmpty(q)) {
        printf("Queue is empty. Cannot dequeue.\n");
        return 1;
    }

    int removedValue = q->items[q->front];

    if (q->front == q->rear) {
        initializeQueue(q);
    } else {
        q->front = (q->front + 1) % MAX_SIZE;
    }

    return removedValue;
}

void displayQueue(struct Queue* q) {
    if (isEmpty(q)) {
        printf("Queue is empty.\n");
        return;
    }

    printf("Elements in the queue: ");
    int i = q->front;
    while (1) {
        printf("%d ", q->items[i]);
        if (i == q->rear) {
            break;
        }
        i = (i + 1) % MAX_SIZE;
    }
    printf("\n");
}

int main() {
    struct Queue myQueue;
    initializeQueue(&myQueue);

    enqueue(&myQueue, 5);
    enqueue(&myQueue, 10);
    enqueue(&myQueue, 15);

    displayQueue(&myQueue);

    int removedValue = dequeue(&myQueue);
    if (removedValue != -1) {
        printf("%d dequeued from the queue.\n", removedValue);
    }

    displayQueue(&myQueue);

    return 0;
}
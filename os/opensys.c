#include<stdio.h>
#define size 5
int main(){
    int no_of_process[size];
    int arrival_time[size];
    int burst_time[size];

    printf("enter process id:\n");
    for (int i=0; i<size ;i++){
        scanf("%d",&no_of_process[i]);
    }
    printf("enter arrival time:\n");
    for(int i=0;i<size ;i++){
        scanf("%d",&arrival_time[i]);
    }
    printf("enter burst time:\n");
    for (int i=0;i<size ;i++){
        scanf("%d",&burst_time[i]);
    }
    int completion_time[size];
    completion_time[0]=burst_time[0];
    for(int i=1; i<size; i++){
        completion_time[i]=completion_time[i-1]+burst_time[i];
    }
    printf("completion time is:\n");
    for (int i=0;i<size;i++){
        printf("%d",completion_time[i]);

    }

}
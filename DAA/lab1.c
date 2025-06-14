//liner search

// #include<stdio.h>
// int main(){
//     int arr[10]={10,20,30,40,50,60,70,80,90,100};
//     int key;
//     scanf("%d",&key);
//     for(int i=0;i<10;i++){
//         if (arr[i]==key){
//             printf("%d",i);
//         }
//     }
// }




//binary search

// #include<stdio.h>
// int main() {
//     int low = 0, high = 9; 
//     int arr[10] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
//     int key;
//     scanf("%d", &key);

//     while (low <= high) {
//         int mid = low + (high - low) / 2;
//         if (arr[mid] == key) {
//             printf("Element found at index: %d\n", mid);
//             break; 
//         }
//         if (arr[mid] < key) {
//             low = mid + 1;
//         } else {
//             high = mid - 1;
//         }
//     }
//     return 0;
// }


//recursiv approach
// include <stdio.h>
// nt rec_binary(int arr[], int low, int high, int key) {
//    if (low <= high) {
//        int mid = low + (high - low) / 2;
// 
//        if (arr[mid] == key) {
//            return mid;
//        }
// 
//        if (arr[mid] < key) {
//            return rec_binary(arr, mid + 1, high, key);
//        } else {
//            return rec_binary(arr, low, mid - 1, key);
//        }
//    }
// 
// nt main() {
//    int low = 0, high = 9;
//    int arr[10] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
//    int key;
//    
//    int key = 30;
// 
//    int result = rec_binary(arr, low, high, key);
// 
//    if (result != -1) {
//        printf("Element found at index %d\n", result);
//    } else {
//        printf("Element not found\n");
//    }
// 
//    return 0;
// 








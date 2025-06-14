#include <stdio.h>
#include <unistd.h>

int main() {
    // Create a new process
    pid_t pid = fork();

    if (pid < 0) {
        // Fork failed
        perror("Fork failed");
        return 1;
    } else if (pid == 0) {
        // Child process
        printf("Hello from Child process!\n");
    } else {
        // Parent process
        printf("Hello from Parent process!\n");
    }

    return 0;
}

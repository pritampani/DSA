#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void) {
    int pid, p[2]; 
    char buffer2[] = "hello", buffer1[100];
    int N = 6;

    // Create the pipe
    if (pipe(p) < 0)  {
        perror("pipe error");
        exit(1);
    }

    // Fork the process
    if ((pid = fork()) == 0) { 
        // Child process: read from the pipe
        read(p[0], buffer1, N); 
        printf("child received: %s\n", buffer1);
    } else if (pid > 0) { 
        // Parent process: write to the pipe
        int status;
        printf("parent sending: %s\n", buffer2);
        write(p[1], buffer2, N); 
        wait(&status); 
    } else {
        perror("fork error");
        exit(1);
    }

    return 0;
}

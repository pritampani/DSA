#include <stdio.h>
#include <stdlib.h>  // Include for exit() and other standard library functions
#include <string.h>  // Include for strlen()
#include <unistd.h>
#include <sys/types.h>

int main(void) {
    int fd[2], nbytes;
    pid_t childpid;
    char string[] = "Hello, world!\n";
    char readbuffer[80];

    // Create the pipe
    pipe(fd);

    if ((childpid = fork()) == -1) {
        perror("fork");
        exit(1);
    }

    if (childpid == 0) {
        // Child process closes up input side of pipe
        close(fd[0]);
        // Send "string" through the output side of pipe
        write(fd[1], string, strlen(string) + 1);
        exit(0);
    } else {
        // Parent process closes up output side of pipe
        close(fd[1]);
        // Read in a string from the pipe
        nbytes = read(fd[0], readbuffer, sizeof(readbuffer));
        printf("Received string: %s", readbuffer);
    }
    
    return 0;
}

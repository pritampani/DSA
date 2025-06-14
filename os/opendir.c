#include <stdio.h>
#include <stdlib.h>

int main() {
    // Specify the directory and file name
    const char *dir = "./my_directory";  // You can change this to your desired directory
    const char *filename = "output.txt";
    
    // Construct the full file path
    char filepath[100];
    snprintf(filepath, sizeof(filepath), "%s/%s", dir, filename);

    // Create the directory if it doesn't exist
    if (mkdir(dir, 0777) == -1) {
        if (errno != EEXIST) {
            perror("Error creating directory");
            return 1;
        }
    }

    // Open the file for writing in the specified directory
    FILE *file = fopen(filepath, "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Write some text to the file
    fprintf(file, "Hello, World!\n");
    fprintf(file, "This is a text file inside a directory.\n");

    // Close the file
    fclose(file);

    printf("File written successfully to %s\n", filepath);

    return 0;
}

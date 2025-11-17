
#include <stdio.h>
#include <string.h>

int main(void)
{
    char buff[15];
    
    
    int pass = 0;

    printf("\nEnter the password: ");
    
    // Safely read input from the user.
    // fgets will read at most `sizeof(buff)` (15) characters, 
    // including the null terminator. This prevents a buffer overflow.
    fgets(buff, sizeof(buff), stdin);

    // Remove trailing newline character if fgets stored one
    buff[strcspn(buff, "\n")] = '\0';

    // Compare the input buffer with the password "mansi"
    if (strcmp(buff, "darsh") == 0)
    {
        printf("\nCorrect Password\n");
        pass = 1;
    }
    else
    {
        printf("\nWrong Password\n");
    }

    // Check if the pass flag was set
    if (pass)
    {
        printf("\nRoot/admin rights granted to user\n");
    }

    return 0;
}
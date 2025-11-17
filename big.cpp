/*
 * This program is from the "Buffer overflow" theory section (Experiment 6) 
 * in the provided PDF.
 *
 * NOTE: This code demonstrates safe input handling using `fgets` to PREVENT
 * a buffer overflow. It reads a password into a buffer of a fixed size
 * but does not allow more characters than the buffer can hold.
 */

#include <stdio.h>
#include <string.h>

int main(void)
{
    // A buffer of 15 characters.
    char buff[15];
    
    // A variable to check if the password is correct.
    int pass = 0;

    printf("\nEnter the password: ");
    
    // Safely read input from the user.
    // fgets will read at most `sizeof(buff)` (15) characters, 
    // including the null terminator. This prevents a buffer overflow.
    fgets(buff, sizeof(buff), stdin);

    // Remove trailing newline character if fgets stored one
    buff[strcspn(buff, "\n")] = '\0';

    // Compare the input buffer with the password "mansi"
    if (strcmp(buff, "mansi") == 0)
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
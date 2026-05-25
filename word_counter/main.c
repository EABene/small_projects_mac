#include <stdio.h>

int main(int argc, char *argv[]) {

    if (argc != 2)
    {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }
    printf("Filename: %s\n", argv[1]);
    return 0;

}

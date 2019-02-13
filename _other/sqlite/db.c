#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "getline.h"

#define EXIT_SUCCESS 0

typedef struct {
    size_t buffer_length;
    size_t input_length;
    char * buffer;
} InputBuffer;

InputBuffer * new_InputBuffer() {
    InputBuffer * ib = malloc(sizeof(InputBuffer));
    *ib = (InputBuffer) {.buffer_length = 0, .input_length = 0, .buffer = NULL};
    return ib;
}

void print_prompt() {
    printf("db > ");
}

void read_input(InputBuffer * ib) {
    // TODO
    // size_t read_n = getline(ib->buffer, ib->input_length, stdin);

}

int main() {

    // REPL
    while(1) {
        InputBuffer * input_buffer = new_InputBuffer();
        print_prompt();
        read_input(input_buffer);

        if (strcmp(input_buffer->buffer, ".exit") == 0) {
            exit(EXIT_SUCCESS);
        } else {
            printf("Unrecognized command '%s'.\n", input_buffer->buffer);
        }

    }
}
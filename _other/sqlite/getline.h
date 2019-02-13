#ifndef GETLINE_H
#define GETLINE_H

#include <stdio.h>

extern size_t getdelim(char **lineptr, size_t *n, int delim, FILE *stream);

extern size_t getline(char **lineptr, size_t *n, FILE *stream);

#endif /* GETLINE_H */
#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <ctype.h>

char *readline();

// Complete the pangrams function below.

// Please either make the string static or allocate on the heap. For example,
// static char str[] = "hello world";
// return str;
//
// OR
//
// char* str = "hello world";
// return str;
//

char *pangrams(char *s) {
  int radix = 'z' - 'a' + 1;
  int found[radix];
  for (int i = 0; i < radix; i++)
    found[i] = 0;
  int count = 0;

  for (int i = 0; i < strlen(s); i++) {
    if (isalpha(s[i])) {
      char c = tolower(s[i]);
      int ord = c - 'a';
      if (found[ord] == 0) {
        found[ord] = 1;
        count++;
      }
    }
  }

  static char *pangram = "pangram";
  static char *notpangram = "not pangram";
  if (count == radix)
    return pangram;
  else
    return notpangram;
}

int main() {
  FILE *fptr = fopen(getenv("OUTPUT_PATH"), "w");

  char *s = readline();

  char *result = pangrams(s);

  fprintf(fptr, "%s\n", result);

  fclose(fptr);

  return 0;
}

char *readline() {
  size_t alloc_length = 1024;
  size_t data_length = 0;
  char *data = malloc(alloc_length);

  while (true) {
    char *cursor = data + data_length;
    char *line = fgets(cursor, alloc_length - data_length, stdin);

    if (!line) {
      break;
    }

    data_length += strlen(cursor);

    if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') {
      break;
    }

    size_t new_length = alloc_length << 1;
    data = realloc(data, new_length);

    if (!data) {
      break;
    }

    alloc_length = new_length;
  }

  if (data[data_length - 1] == '\n') {
    data[data_length - 1] = '\0';
  }

  data = realloc(data, data_length);

  return data;
}

/*
  Created at 10 of June, 2015
  Updated at 11.08.2015
  Author: <w1ld at inbox dot ru>

   Exercise 1-20. Write a program detab that replaces tabs in the input with the
   proper number of blanks to space to the next tab stop. Assume a fixed set of
   tab stops, say every n columns.  Should n be a variable or a symbolic
   parameter?

   Exercise 5-12.Extend entab and  detab to accept the shorthand 
      entab -m +n 
   to mean tab stops every n columns, starting at column m. Choose convenient
   (for the user) default behavior. 
*/

#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "getline.c"
#include "atoi.c"

#define MAXLINE 1000
#define DEFAULT_TAB_STOP 4

int getline(char s[], int lim);

int main(int argc, char *argv[])
{
	assert_atoi();

	if(argc == 2 && strstr(*(argv+1), "help")) {
		printf("Replaces tab with blanks.\n Usage: detab -m +n\n  m - start of detabbing (0 default),\n  n - tab stops every n columns (4 default)\n");
		return 0;
	}

	// init arguments:
	int tabStop = DEFAULT_TAB_STOP;
	int startDetabbingAt = 0;
	while(argc-- > 1) {
		argv++;
		if(strstr(*argv, "+")) {
			tabStop = atoi((*argv)++);
			if(tabStop == 0) {
				tabStop = DEFAULT_TAB_STOP;
			}
		}
		if(strstr(*argv, "-")) {
			startDetabbingAt = atoi(++(*argv));
			assert(startDetabbingAt >= 0);
		}
	}

	// start detabbing:
	int len;
	char line[MAXLINE];
	while ((len = getline(line, MAXLINE)) > 0) {
		int columns = 0;
		// go through chars to replace '\t':
		for(int i = 0; i < len; i++) { 
			char c = line[i];
			if(c == '\t') { // to replace '\t'
				int numberOfColumnsToTabStop = tabStop - (columns % tabStop);
				if(startDetabbingAt > columns) {
					putchar('\t');
				}
				else {
					for(int j = 0; j < numberOfColumnsToTabStop; j++) 
						putchar(' ');
				}

				columns += numberOfColumnsToTabStop;
			}
			else { 
				columns++;
				putchar(c);
			}
		}
	}
}



/* 
 *
 * test 1:
col1	col2	col3
v1  	v2  	val3
 *
 * test 2:
c1	c1	c1
	c2
		c3
 */

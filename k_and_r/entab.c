/*
  Created at 10 of June, 2015
  Updated at 11.08.2015 
  Author: <w1ld at inbox dot ru>
 
  ---
  Exercise 1-21. Write a program entab that replaces strings of blanks by the
  minimum number of tabs and blanks to achieve the same spacing. Use the same
  tab stops as for detab. When either a tab or a single blank would suffice to
  reach a tab stop, which should be given preference?
 
  ---
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
		printf("Inserts tabs. A blank chosen over tab when both suffice.\n Usage: entab -m +n\n  m - start of entabbing (0 default),\n  n - tab stops every n columns (4 default)\n");
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

	// start entabbing:
	int len;
	char line[MAXLINE];
	while ((len = getline(line, MAXLINE)) > 0) {
		int columns = 0;
		int skippedBlanks = 0;
		// go through chars to insert tabs:
		for(int i = 0; i < len; i++) { 
			char c = line[i];

			if(c == ' ') { // to insert tab or not
				skippedBlanks++;
				int isToInsertTab = 
					((columns + skippedBlanks) % tabStop) == 0 && skippedBlanks > 1;
				if(isToInsertTab) {
					int numberOfColumnsToTabStop = tabStop - (columns % tabStop);
					columns += numberOfColumnsToTabStop;
					putchar('\t');
					skippedBlanks = 0;
				}
			}
			else if(c == '\t') { // to keep existent tabs
				int numberOfColumnsToTabStop = tabStop - (columns % tabStop);
				columns += numberOfColumnsToTabStop;
				putchar(c);
			}
			else { // to output all other
				while(skippedBlanks > 0) {
					columns++;
					putchar(' ');
					skippedBlanks--;
				}
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

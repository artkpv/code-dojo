#include <stdio.h>

// NEXT: Fix the bug: makes a line a bit longer than MAXCOLUMN

#define MAXLINE 9999
#define MAXCOLUMN 80
#define TABLENGTH 4

main()
{
	char c;
	int currentLineCol = 1;
	char aWord[MAXCOLUMN];
	int aWordInx = -1;
	int doesNotFitLine;

	// put a line into stdout folding it
	while( (c = getchar()) != EOF)
	{
		// invariants:
		//  currentLineCol <= MAXCOLUMN

		// if a whole word got
		if(c == ' ' || c == '\t' || c == '\n' || ((aWordInx + 1) > MAXLINE))
		{
			doesNotFitLine = ((currentLineCol + aWordInx + 1) > MAXCOLUMN);
			// BUG!!! isNewLine equals 1 when it should not !
			int isNewLine = (c == '\n');
			if(isNewLine || (currentLineCol != 1 && doesNotFitLine))
			{
				++aWordInx;
				aWord[aWordInx] = '\n';
				currentLineCol = 1;
			}
			else 
			{
				if(c == '\t')
				{
					++aWordInx;
					aWord[aWordInx] = c;
					currentLineCol += aWordInx + TABLENGTH;
				}
				else if(c == ' ')
				{
					++aWordInx;
					aWord[aWordInx] = c;
					currentLineCol += aWordInx + 1;
				}
			}

			flushWord(aWord, aWordInx + 1);
			aWordInx = -1;
		}
		else // if not a whole word got
		{
			//   keep char
			++aWordInx;
			aWord[aWordInx] = c;
		}

	}
}

flushWord(char s[], int len)
{
	for(int k = 0; k < len; ++k)
		putchar(s[k]);
	return 0;
}

/* Test 1:
   Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctu s est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt u t labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd  gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed di am nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo do lores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

*/

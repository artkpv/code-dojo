// 
// K&R from 5.11 Pointers to Functions
//
// ---------------------------------------------------------------------------
// Exercise 5-14. Modify the sort program to handle a -r flag, which indicates
// sorting in reverse (decreasing) order. Be sure that -rworks with -n.
//
// Exercise 5-15. Add the option -f to fold upper and lower case together, so
// that case distinctions are not made during sorting; for example, a and
// A compare equal.  
//
// Exercise 5-16. Add the -d (``directory order'') option, which makes
// comparisons only on letters, numbers and blanks. Make sure it works in
// conjunction with  -f. 
//
// Exercise 5-17. Add a field-searching capability, so sorting may bee done on
// fields within lines, each field sorted according to an independent set of
// options. (The index for this book was sorted with  -df for the index category
// and -n for the page numbers.)
// ---------------------------------------------------------------------------
//
// 18.08.2015. How to make it simple?
//
// Links: https://en.wikipedia.org/wiki/Sort_%28Unix%29

#include <stdio.h>
#include <string.h>
#include "read_write_lines.c"

#define MAXLINES 5000 /* max #lines to be sorted */

char *lineptr[MAXLINES]; /* pointers to text lines */
int readlines(char *lineptr[], int nlines);
void writelines(char *lineptr[], int nlines);
void qsort(void *lineptr[], int left, int right,
		int (*comp)(void *, void *));
int numcmp(char *, char *);
int strcmp(char *s, char *t);

int isdesc = 0;
int isfold = 0;
int isdirectory = 0;

/* sort input lines */
int main(int argc, char *argv[])
{
	if (argc > 1 && strstr(argv[1], "--help") != NULL) {
		printf("\nSorts lines in increasing order."
				"\n Usage: xsort -n -r"
				"\n   where:"
				"\n   -n sort numerically;"
				"\n   -r reverse;"
				"\n   -d directory order, make comparisons only on letters, numbers and blanks");
		return 0;
	}

	int nlines; /* number of input lines read */
	int (*comparer)(void*, void*) = strcmp; 
	while(argc-- > 1)
	{
		argv++;
		if(strcmp(*argv, "-n") == 0)
			comparer = numcmp;
		if(strcmp(*argv, "-r") == 0)
			isdesc = 1;
		if(strcmp(*argv, "-f") == 0)
			isfold = 1;
		if(strcmp(*argv, "-d") == 0)
			isdirectory = 1;
	}

	if ((nlines = readlines(lineptr, MAXLINES)) >= 0) {
		qsort((void**) lineptr, 0, nlines-1, comparer);

		writelines(lineptr, nlines);
		return 0;
	} else {
		printf("input too big to sort\n");
		return 1;
	}
}

/* qsort: sort v[left]...v[right] into a given order */
void qsort(void *v[], int left, int right,
		int (*comp)(void *, void *))
{
	int i, last;
	void swap(void *v[], int, int);
	if (left >= right) /* do nothing if array contains */
		return; /* fewer than two elements */
	swap(v, left, (left + right)/2);
	last = left;
	for (i = left+1; i <= right; i++) {
		int compareResult = (*comp)(v[i], v[left]);
		if (compareResult < 0)
			swap(v, ++last, i);
	}
	swap(v, left, last);
	qsort(v, left, last-1, comp);
	qsort(v, last+1, right, comp);
}

#include <stdlib.h>

void swap(void *v[], int i, int j)
{
	void *temp;
	temp = v[i];
	v[i] = v[j];
	v[j] = temp;
}

/* numcmp: compare s1 and s2 numerically */
int numcmp(char *s1, char *s2)
{
	double v1, v2;
	v1 = atof(s1);
	v2 = atof(s2);
	if (v1 < v2)
		return -1;
	else if (v1 > v2)
		return 1;
	else
		return 0;
}

int strcmp(char *s, char *t)
{
	// skipping equal chars
	while(*s != '\0') {
		int isSkip = 0;

		int isAlphanumOrBlank = (isalnum(*s) || isblank(*s)) &&
				(isalnum(*t) || isblank(*t));
		if(isdirectory && !isAlphanumOrBlank) {
			isSkip = 1;						
		}

		if(isfold && tolower(*s) == tolower(*t))
			isSkip = 1;
		else if(*s == *t)
			isSkip = 1;

		if(!isSkip) 
			break;

		s++;
		t++;
	}

	// comparing
	if(*s == '\0')
		return 0;

	int result;
	if(isfold)
		result = tolower(*s) - tolower(*t);
	else
		result = *s - *t;
	
	return isdesc ? -result : result;
}

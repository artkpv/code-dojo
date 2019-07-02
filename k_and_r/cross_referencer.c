// Exercise 6-3. Write a cross-referencer that prints a list of all words in a
// document, and for each word, a list of the line numbers on which it occurs.
// Remove noise words like ``the,'' ``and,'' and so on. 
//
// Author: Artyom K. <w1ld at inbox dot ru> 
// Last edit at 29.08.2015 

#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <assert.h>
#include "getch.c"
#include "list.c"

struct tnode { /* the tree node: */
	char *word; /* points to the text */
	IntsPtr lines; // list of lines
	struct tnode *left; /* left child */
	struct tnode *right; /* right child */
};

#define MAXWORD 10000
#define DEFAULT_CHARS_NUMBER 6

struct tnode *addtree(struct tnode *, char *, int);
void treeprint(struct tnode *);
int getword(char *, int, int *);

/* word frequency count */
int main(int argc, char *argv[])
{
	struct tnode *root;
	char word[MAXWORD];
	root = NULL;
	int line = 0;
	int *lineptr = &line;
	int r;
	while ((r = getword(word, MAXWORD, lineptr)) != EOF) {
		if(r > 0) {
			printf("'%s' found at %d\n", word, *lineptr);
			root = addtree(root, word, *lineptr);
		}
	}

	treeprint(root);

	return 0;
}

struct tnode *talloc(void);

/* addtree: add a node with w, at or below p */
struct tnode *addtree(struct tnode *p, char *w, int line)
{
	int cond;
	if (p == NULL) { /* a new word has arrived */
		p = talloc(); /* make a new node */
		p->word = strdup(w);
		p->lines = ints_create();
		ints_add(p->lines, line);
		p->left = p->right = NULL;
	} else if ((cond = strcmp(w, p->word)) == 0) {
		if(!ints_contains(p->lines, line))
			ints_add(p->lines, line);
	}
	else if (cond < 0) /* less than into left subtree */
		p->left = addtree(p->left, w, line);
	else /* greater than into right subtree */
		p->right = addtree(p->right, w, line);
	return p;
}

/* treeprint: in-order print of tree p */
void treeprint(struct tnode *p)
{
	if (p != NULL) {
		treeprint(p->left);
		printf("%-20s", p->word);
		int i;
		for(i = 0; i < p->lines->count; i++)
			printf("%d, ", *(p->lines->ints + i));

		printf("\n");
		treeprint(p->right);
	}
}

#include <stdlib.h>

/* talloc: make a tnode */
struct tnode *talloc(void)
{
	return (struct tnode *) malloc(sizeof(struct tnode));
}

int currentline = 1; // start with 1

void skip_space() 
{
	int c, getch(void);
	void ungetch(int);
	while(isspace((c = getch()))) {
		if(c == '\n')
			currentline++;
	}
	ungetch(c);
}

void skip_strings()
{
	int c, getch(void);
	void ungetch(int);
	c = getch();
	if(c == '"') { 
		while((c = getch()) != '"' && c != EOF) {
			if(c == '\n')
				currentline++;
			if(c == '\\' && (c = getch()) == '"')
				continue;
			else if(c == EOF)
				break;
		}
	}
	else if(c == '\'') {
		c = getch(); // TODO Find out if it can be broken with \n or smth
		if(c == '\\') 
			c = getch();
		c = getch();
		assert(c == '\'');
	}
	ungetch(c);
}

void skip_comments()
{
	int c, getch(void);
	void ungetch(int);
	c = getch();
	if(c == '/') {
		c = getch();

		if(c == '*') { // multiline
			while(1) {
				c = getch();
				if(c == EOF)
					break;

				if(c == '*' && (c = getch()) == '/')
					break;

				if(c == '\n')
					currentline++;
			}
		}
		else if(c == '/') { // oneline
			while((c = getch()) != '\n' && c != EOF)
				;

			if(c == '\n')
				currentline++;
		}
	}
	ungetch(c);
}

/* skips all non word chars, comments, string constants. Stream is set to the first word char or EOF*/
void skip_non_word_chars()  
{
	int c, getch(void);
	void ungetch(int);

	do {
		skip_space();
		skip_strings();
		skip_comments();

		c = getch();
	} while(c != EOF && !isalnum(c) && c != '_');

	ungetch(c); 
}

int getword(char *word, int lim, int *lineptr)
{
	skip_non_word_chars();

	int c, getch(void);
	void ungetch(int);
	char *w = word;
	int wordlength = 0;

	// gather word if any
	for ( ; --lim > 0; w++) {
		*w = c = getch();
		wordlength++;
		if (!isalnum(*w) && *w != '_') {
			ungetch(*w);
			wordlength--;
			break;
		}
	}
	*w = '\0';
	*lineptr = currentline;
	if(c == EOF) {
		printf("EOF found\n");
		return EOF;
	}
	if(wordlength > 0 && !(isalpha(word[0]) || word[0] == '_')) { // skip non valid
		return getword(word, lim, lineptr);		
	}
	return wordlength;
}


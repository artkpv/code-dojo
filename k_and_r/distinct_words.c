// Exercise 6-4. Write a program that prints the distinct words in its input
// sorted into decreasing order of frequency of occurrence. Precede each word by
// its count. 
//
// Author: Artyom K. <w1ld at inbox dot ru>, Aug, 2015

#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <assert.h>
#include "getch.c"

struct tnode { /* the tree node: */
	char *word; /* points to the text */
	int count;  // frequency of occurrence
	struct tnode *left; /* left child */
	struct tnode *right; /* right child */
};
typedef struct tnode Node;
typedef struct tnode *NodePtr;

#define MAXWORD 10000
#define DEFAULT_CHARS_NUMBER 6

struct tnode *addtree(struct tnode *, char *, int);
int tree_size = 0;
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
		p->count = 1;
		p->left = p->right = NULL;
		tree_size++;
	} else if ((cond = strcmp(w, p->word)) == 0) {
		p->count++;
	}
	else if (cond < 0) /* less than into left subtree */
		p->left = addtree(p->left, w, line);
	else /* greater than into right subtree */
		p->right = addtree(p->right, w, line);
	return p;
}

NodePtr array = NULL;
int arraycount = 0;

void add_to_array(NodePtr p)
{
	if (p != NULL) {
		add_to_array(p->left);
		*(array + arraycount) = *p;
		arraycount++;
		add_to_array(p->right);
	}
}

void swap(NodePtr first, NodePtr second) 
{
	Node t = *first;
	*first = *second;
	*second = t;
}

void sort_array()
{
	int i, j;
	for(i = 0; i < arraycount; i++) {
		for(j = i+1; j < arraycount; j++) {
			NodePtr left = (array + i);
			NodePtr right = (array + j);
			if(left->count < right->count)
				swap(left, right);
		}
	}
}

void print_array()
{
	int i;
	for(i = 0; i < arraycount; i++) {
		NodePtr node = (array + i);
		printf("%5d %s\n", node->count, node->word); 
	}
}

/* treeprint: in-order print of tree p */
void treeprint(struct tnode *p)
{
	if(array == NULL) {
		array = (NodePtr) calloc(tree_size, sizeof(Node));
		arraycount = 0;
	}

	add_to_array(p);
	sort_array();
	print_array();
}

#include <stdlib.h>

/* talloc: make a tnode */
struct tnode *talloc(void)
{
	return (struct tnode *) malloc(sizeof(struct tnode));
}

/* skips all non word chars, comments, string constants. Stream is set to the first word char or EOF*/
void skip_non_word_chars()  
{
	int c, getch(void);
	void ungetch(int);

	while((c = getch()) != EOF && !isalnum(c) && c != '_')
		;
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
	if(c == EOF) {
		return EOF;
	}
	if(wordlength > 0 && !(isalpha(word[0]) || word[0] == '_')) { // skip non valid
		return getword(word, lim, lineptr);		
	}
	return wordlength;
}


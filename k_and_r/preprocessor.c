// Exercise 6-5. Write a function undef that will remove a name and definition
// from the table maintained by lookupand  install.  
//
// Exercise 6-6. Implement a simple version of the #define processor (i.e., no
// arguments) suitable for use with C programs, based on the routines of this
// section. You may also find getchand  ungetchhelpful.  
//
// NEXT: See bugs when processing this file. E.g. line 39.
//
// Author: Artyom K. <w1ld at inbox dot ru>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

void DEBUG(char *s)
{
	//printf("DEBUG: %s\n", s);
}

/* getline:  read a line into s, return length  */
int mygetline(char *s, int lim)
{
	int c, i;

	for (i=0; i < lim-1 && (c=getchar())!=EOF && c!='\n'; ++i)
		*(s++) = c;
	if (c == '\n') {
		*(s++) = c;
		++i;
	}
	*s = '\0';
	return i;
}

#define HASHSIZE 101
#define MAXLINE 1000
#define MAXWORD 1000

static struct nlist *hashtab[HASHSIZE]; /* pointer table */
static char *define_statement = "#define";

struct nlist { /* table entry: */
	struct nlist *next; /* next entry in chain */
	char *name; /* defined name */
	char *defn; /* replacement text */
};

struct nlist *lookup(char *);
//char *strdup(char *);

/* hash: form hash value for string s */
unsigned hash(char *s)
{
	unsigned hashval;
	for (hashval = 0; *s != '\0'; s++)
		hashval = *s + 31 * hashval;
	return hashval % HASHSIZE;
}

/* lookup: look for s in hashtab */
struct nlist *lookup(char *s)
{
	struct nlist *np = NULL;
	for (np = hashtab[hash(s)]; np != NULL; np = np->next)
		if (strcmp(s, np->name) == 0)
			return np; /* found */
	return NULL; /* not found */
}

/* install: put (name, defn) in hashtab */
struct nlist *install(char *name, char *defn)
{
	DEBUG("Installing value. Name:");
	DEBUG(name);
	DEBUG("Value:");
	DEBUG(defn);
	struct nlist *np = NULL;
	unsigned hashval;
	if ((np = lookup(name)) == NULL) { /* not found */
		np = (struct nlist *) malloc(sizeof(*np));
		if (np == NULL || (np->name = strdup(name)) == NULL)
			return NULL;
		hashval = hash(name);
		np->next = hashtab[hashval];
		hashtab[hashval] = np;
	} else /* already there */
		free((void *) np->defn); /*free previous defn */
	if ((np->defn = strdup(defn)) == NULL)
		return NULL;
	return np;
}

void end_processing() 
{
	exit(0);
}

char *substitude(char *line) 
{
	char *newline = (char *)calloc(sizeof(char), strlen(line) + 1);
	char *newlineptr = newline;

	char *p = line;

	while(*p != '\0') {
		while(!isalnum(*p) && *p != '_' && *p != '\0') // skip non word chars
			*(newlineptr++) = *(p++);

		if(isalnum(*p) || *p == '_') {
			char *wordptr = p;
			int wordlen = 0;
			while(isalnum(*p) || *p == '_')  {
				wordlen++;
				p++;
			}

			char *word = strndup(wordptr, wordlen);
			assert(strlen(word) == wordlen);

			struct nlist *entry = lookup(word);
			if(entry == NULL) {
				while(*word != '\0')
					*(newlineptr++) = *(word++);
			}
			else { 
				char *defn = entry->defn;
				while(*defn != '\0')
					*(newlineptr++) = *(defn++);
			}
		}
	}
	*newlineptr = '\0';
	return newline;
}

char *define_name_and_substitude(char *line)
{
	char *defineposition = strstr(line, define_statement);

	// assert that '#define' is preceeded with space:
	if(defineposition != line) { 
		char *lineptr = line;
		while(lineptr != defineposition)
			assert(isspace(*(lineptr++)));
	}
	
	char *p = defineposition + strlen(define_statement);

	while(isspace(*p))
		p++;
	
	// grab name:
	char *namelineptr = p;
	int namelen = 0;
	while(!isspace(*(p++))) {
		namelen++;
	}
	char *name = strndup(namelineptr, namelen);

	char *defn = strdup(p);
	char *newdefn = substitude(defn);

	*(newdefn + strlen(newdefn) - 1) = '\0';

	install(name, newdefn);

	//int newlinelen = strlen(define_statement) + strlen(newdefn) + 2; // \n and \0
	//char *newline = (char *)calloc(sizeof(char), newlinelen);

	//strcpy(newline, define_statement);
	//strcat(newline, " ");
	//strcpy(newline, name);
	//strcat(newline, " ");
	//strcat(newline, newdefn);
	//strcat(newline, "\n");
	return defineposition;
}

void main() 
{
	char *line = (char *)calloc(sizeof(char), MAXLINE);
	int lim = -1;
	// get line
	while(mygetline(line, MAXWORD) > 0) {
		//while(isspace(*line))
		//	line++;
		
		char *newline = NULL;
		char *founddefine = strstr(line, define_statement);
		if(line - founddefine == 0) {
			newline = define_name_and_substitude(line);
			assert(strlen(newline) > 0);
		}
		else {
			newline = substitude(line);
			assert(strlen(newline) > 0);
		}
		printf("%s", newline);
	}
	end_processing();
}

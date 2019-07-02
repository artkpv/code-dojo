// a list of ints with dynamic allocation

#include <assert.h>
#include <stdlib.h>

#define DEFAULT_SIZE 10

struct ints_list {
	int *ints;
	int size;
	int count;
};

typedef struct ints_list *IntsPtr;
typedef struct ints_list Ints;

IntsPtr ints_create() {
	IntsPtr list = (IntsPtr)malloc(sizeof(Ints));
	list->ints = (int *)calloc(DEFAULT_SIZE, sizeof(int));
	list->size = DEFAULT_SIZE;
	list->count = 0;
	return list;
}

void ints_add(IntsPtr list, int number) 
{
	assert(list->size >= list->count);

	if(list->size == list->count) { // resize
		int newsize = list->size * 2;
		int *new_ints = (int *)malloc(sizeof(int) * newsize);
		int i;
		for(i = 0; i < list->count; i++)
			*(new_ints + i) = *(list->ints + i);
		free(list->ints);
		list->ints = new_ints;
		list->size = newsize;
	}

	assert(list->size > list->count);
	*((list->ints) + (list->count)) = number;
	list->count++;
}

int ints_contains(IntsPtr list, int number) 
{
	int isfound = 0;
	int i;
	for(i = 0; i < list->count; i++) { 
		if(*(list->ints + i) == number){
			isfound = 1;
			break;
		}
	}
	return isfound;
}


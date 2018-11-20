/*
 * Binary search tree
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NONE 0

typedef struct tnode * NodePtr;

typedef struct tnode {
	char key;
	int value;
	struct tnode *left;
	struct tnode *right;
} Node;


NodePtr
talloc() {
	NodePtr x = (NodePtr) malloc(sizeof(Node));
	x->left = NONE;
	x->right = NONE;
	return x;
}


NodePtr 
tput(NodePtr x, char key, int value) {
	if (x == NONE) {
		x = talloc();
		x->key = key;
		x->value = value;
		return x;
	}
	int cmp = x->key - key;
	if (cmp > 0) 
		x->left = tput(x->left, key, value);
	else if (cmp < 0) 
		x->right = tput(x->right, key, value);
	else 
		x->value = value;
	return x;	
}


NodePtr 
tmin(NodePtr x) {
	while (x->left != NONE) 
		x = x->left;
	return x;
}


NodePtr 
tdelete_min(NodePtr x) {
	if (x->left != NONE) {
		x->left = tdelete_min(x->left);
		return x;
	}
	else {
		NodePtr t = x;
		free(x);
		return x->right;
	}
}


NodePtr
tdelete(NodePtr x, char key) {
	if (x == NONE) return x;
	int cmp = x->key - key;
	if (cmp > 0) 
		x->left = tdelete(x->left, key);
	else if (cmp < 0) 
		x->right = tdelete(x->right, key);
	else {  // == key
		if (x->left == NONE) {
			NodePtr t = x->right;
			free(x);
			x = t;
		}
		else if (x->right == NONE) {
			NodePtr t = x->left;
			free(x);
			x = t;
		}
		else {
			NodePtr t = x;
			x = tmin(t->right);
			x->right = tdelete_min(t->right);
			x->left = t->left;
		}
	}
	return x;
}


void 
inorder(NodePtr x, int level) {
	if (x->left != 0) inorder(x->left, level + 1);
	char pad[level+1];
	for (int i = 0; i < level; i++)
		pad[i] = ' ';
	pad[level] = '\0';
	printf("%s(%c,%d)\n", pad, x->key, x->value);
	if (x->right != 0) inorder(x->right, level + 1);
}


void 
main() {
	char *keys = "SEARCHMX";

	NodePtr root = NONE; 

	for (int i = 0; i < strlen(keys); i++) {
		root = tput(root, keys[i], i);
	}

	inorder(root, 0);

	root = tdelete(root, 'E');
	printf("\ndel E:\n");
	inorder(root, 0);

	root = tdelete(root, 'A');
	printf("\ndel A:\n");
	inorder(root, 0);
}

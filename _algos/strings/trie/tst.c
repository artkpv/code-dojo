//
// Author: Artyom K. <artyomkarpov [at] gmail [dot] com>
//
// Ternary search trie
//  Time: O(log(N))
//  Space: O(NW)
//
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

typedef struct node_s {
    struct node_s * left;
    struct node_s * right;
    struct node_s * middle;
    int val;
    char c;
} Node;

Node * put(Node * n, const char * key, int keylen, int d);

int search(Node * n, const char * key, int keylen, int d);

void printtrie(Node *n, int level);

int main()
{
    int n = 4;
    const char * strings[n];
    strings[0] = "abcd";
    strings[1] = "def";
    strings[2] = "fghi";
    strings[3] = "ijklm";
    Node * root = NULL;
    int i;
    for (i = 0; i < n; ++i) {
        root = put(root, strings[i], strlen(strings[i]), 0);
    }

    for (i = 0; i < n; ++i) {
        assert(search(root, strings[i], strlen(strings[i]), 0) == 1);
    }
    assert(search(root, "not present", 11, 0) == 0);
    assert(search(root, "another not present", 19, 0) == 0);

    printtrie(root, 0);

    printf("done\n");
    return 0;
}

Node * put(Node * n, const char * key, int keylen, int d)
{
    if (n == NULL)
    {
        n = (Node *) malloc(sizeof(Node));
        n->left = NULL;
        n->right = NULL;
        n->middle = NULL;
        n->val = 0;
        n->c = key[d];
    }
    if (n->c == key[d])
    {
        if (keylen - 1 == d)
            n->val = 1;
        else
            n->middle = put(n->middle, key, keylen, d+1);
    }
    else if (key[d] < n->c)
        n->left = put(n->left, key, keylen, d);
    else
        n->right = put(n->right, key, keylen, d);

    return n;
}

int search(Node * n, const char * key, int keylen, int d)
{
    if (n == NULL)
        return 0;

    if (n->c == key[d])
    {
        if (keylen - 1 == d)
            return n->val;
        else
            return search(n->middle, key, keylen, d+1);
    }
    else if (key[d] < n->c)
        return search(n->left, key, keylen, d);
    else 
        return search(n->right, key, keylen, d);
}

void printtrie(Node * n, int level)
{
    if (n == NULL)
        return;
    int i;
    for (i = 0; i < level; ++i) 
        printf(" ");

    printf("ch='%c' val=%d\n", n->c, n->val);
    printtrie(n->left, level + 1);
    printtrie(n->middle, level + 1);
    printtrie(n->right, level + 1);
}

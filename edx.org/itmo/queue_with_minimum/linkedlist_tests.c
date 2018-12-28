#include "linkedlist.c"
#include <stdio.h>
#include <assert.h>
#include <string.h>

void main() {
    linkedlist * ll = ll_ctor();

    // test 1:
    ll_addleft(ll, "1");
    assert(ll->right->value == "1");
    assert(ll->left->value == "1");
    ll_addleft(ll, "2");
    assert(ll->left->value == "2");
    assert(ll->right->value == "1");
    ll_addleft(ll, "3");
    assert(ll->left->value == "3");
    assert(ll->right->value == "1");
    assert(ll_popleft(ll) == "3");
    assert(ll->left->value == "2");
    assert(ll->right->value == "1");
    assert(ll_popleft(ll) == "2");
    assert(ll->left->value == "1");
    assert(ll->right->value == "1");
    assert(ll_popleft(ll) == "1");
    assert(ll->left == NULL);
    assert(ll->right == NULL);
    ll_addleft(ll, "4");
    ll_addright(ll, "5");

    // test 2:
    assert(ll->right->value == "5");
    assert(ll->left->value == "4");
    assert(ll_popright(ll) == "5");
    assert(ll->right->value == "4");
    assert(ll_popleft(ll) == "4");
    assert(ll->left == NULL);
    assert(ll->right == NULL);

    ll_free(ll);
    printf("Tests done.\n");
}
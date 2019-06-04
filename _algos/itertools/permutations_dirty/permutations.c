/*
 *
 * Permutaions. Hard way
 *
 */ 
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

int factorial(int n) {
    int result = 1;
    while (n > 1){
        result *= (n--);
    }
    return result;
}

void print_arr(int arr[], int size) {
    for (int i = 0; i < size; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int _permutationsCounter = 0;
int taken = 0;

void _permutations(
        int* nums,
        int numsSize, 
        int * result[], 
        int position,
        int resultLength) {
    if (position == numsSize) {
        print_arr(result[_permutationsCounter], numsSize);
        _permutationsCounter++;
        if (_permutationsCounter >= resultLength)
            return;
        // init next permutation:
        result[_permutationsCounter] = (int*) malloc(sizeof(int)*numsSize);
        for (int i = 0; i < numsSize; i++) {
            result[_permutationsCounter][i] = result[_permutationsCounter-1][i];
        }
        return;
    }

    for (int i = 0; i < numsSize; i++) {
        if (((taken >> i) & 1) > 0)
            continue;
        taken |= (1<<i);
        result[_permutationsCounter][position] = nums[i];
        _permutations(nums, numsSize, result, position+1, resultLength); 
        taken &= ~(1<<i);
    }
}

int** permute(
        int* nums, 
        int numsSize, 
        int* returnSize_p, 
        int** returnColumnSizes) {
    int length = factorial(numsSize);
    *returnSize_p = length;
    if ((int**) realloc(returnColumnSizes, sizeof(int**)*length) == NULL)
    {
        printf("Memory error\n");
        return NULL;
    }
    for (int i = 0; i < length; i++) {
        if ((int*) realloc(returnColumnSizes[i], sizeof(int)) == NULL) {
            printf("memory error\n");
            return NULL;
        }
        *(returnColumnSizes[i]) = numsSize;
    }
    int ** returnArr = (int**) malloc(sizeof(int*) * length);
    // init first permutation:
    returnArr[0] = (int*) malloc(sizeof(int)*numsSize);
    for (int i = 0; i < numsSize; i++) {
        returnArr[0][i] = 0;
    }

    _permutationsCounter = 0;
    taken = 0;
    _permutations(nums, numsSize, returnArr, 0, length); 

    return returnArr;
}



void test_3_elements() {
    int nums[] = {1,2,3};
    int * returnSize = (int*) malloc(sizeof(int));
    int ** returnColumnSizes;
    int ** perms;
    perms = permute(nums, 3, returnSize, returnColumnSizes);

    for (int i = 0; i < *returnSize; i++){
        print_arr(perms[i], 3);
    }
}

void test_4_elements() {
    int nums[] = {1,2,3,4};
    int * returnSize;
    int ** returnColumnSizes;
    int ** perms;
    perms = permute(nums, 4, returnSize, returnColumnSizes);

    for (int i = 0; i < *returnSize; i++){
        print_arr(perms[i], 4);
    }
}

int main() {
    // test_3_elements();
    test_4_elements();
    return 0;
}

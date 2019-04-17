#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

const int MAX_LEN = 1024*1024*10;

void merge(char * array, int left, int leftn, int right, int rightn) {
    char aux[leftn + rightn];
    int i = left;
    int j = right;
    for (int k = 0; k < leftn + rightn; k++) {
        if (j >= right + rightn || (i < left + leftn && array[i] < array[j]))
            aux[k] = array[i++];
        else
            aux[k] = array[j++];
    }
    // copy back:
    for (int k = 0; k < leftn + rightn; k++)
        array[k] = aux[k];
}

void printme(char * array, int count) {
    for (int i = 0; i < count; i++)
        printf("%d ", array[i]);
    printf("\n");
}


void exchinterval(int lengths[], int starts[], int i, int j) {
    int t = lengths[i];
    lengths[i] = lengths[j];
    lengths[j] = t;
    t = starts[i];
    starts[i] = starts[j];
    starts[j] = t;
}

void _sortintervals(int lengths[], int starts[], int lo, int hi) {
    if (lo >= hi)
        return;
    int p = lengths[(int)(lo+hi)/2];
    int i = lo;
    int j = hi;
    while (i <= j) {
        while (lengths[i] < p) 
            i++;
        while (p < lengths[j]) 
            j--;
        if (i <= j) 
            exchinterval(lengths, starts, i++, j--);
    }

    // Invariant:  a[lo..i-1] <= p <= a[i..hi]

    _sortintervals(lengths, starts, lo, i-1);
    _sortintervals(lengths, starts, i, hi);
}

void sortintervals(int k, int lengths[], int starts[]) {
    _sortintervals(lengths, starts, 0, k-1);
}

int main() {
    int k;
    scanf("%d", &k);
    char * array = (char*) calloc(MAX_LEN, sizeof(char));
    int count = 0;
    int intervals_len[k];
    int intervals_start[k];
    for (int i = 0; i < k; i++) {
        int thislength;
        scanf("%d", &thislength);
        intervals_len[i] = thislength;
        intervals_start[i] = count;
        for (int j = 0; j < thislength; j++) {            
            int el;
            scanf("%d", &el);
            array[count++] = (char)el;
            assert (count < MAX_LEN);
        }
    }

    // TODO: fix this part. Need 
    // sort interval in asc order 
    sortintervals(k, intervals_len, intervals_start);
    
    printme(array, count);
    // merge them in asc order by their length
    for (int i = 1; i < k; i++) {
        printf("merge %d %d %d %d \n",
            intervals_start[i-1],
            intervals_len[i-1],
            intervals_start[i],
            intervals_len[i]
        );
        merge(
            array, 
            intervals_start[i-1],
            intervals_len[i-1],
            intervals_start[i],
            intervals_len[i]
        );
    }
    printme(array, count);
    free(array);
}

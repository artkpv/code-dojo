#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <pthread.h>

/*
 * Producer-consumer solution using message passing.

const int N = 100; // Buffer size.

int empty = 1;

void producer() 
{
    int count = 100;
    while (count-- > 0) 
    {
        receive(consumer_mainbox, &empty);
        // produce
        void * item = ... ;
        send(&item);
    }
}

void consumer()
{
    for (int i = 0; i < N; i++) 
        send(&empty);

    int count = 100;
    while (count-- > 0) 
    {
        void * item = receive(producer_mailbox);
        send(&empty);
        // consume item
    }
}

int main( void )
{
    unsigned i;
    pthread_t tconsumer;
    pthread_t tproducer;

    if ( pthread_create( &tconsumer, NULL, consumer, NULL ) )
        return EXIT_FAILURE;
    if ( pthread_create( &tproducer, NULL, producer, NULL ) )
        return EXIT_FAILURE;

    if ( pthread_join( tproducer, NULL ) )
        return EXIT_FAILURE;
    if ( pthread_join( tconsumer, NULL ) )
        return EXIT_FAILURE;

    return EXIT_SUCCESS;
}

*/

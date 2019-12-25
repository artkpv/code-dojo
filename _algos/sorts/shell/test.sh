#!/bin/bash

PROG=./shell

g++ -std=c99 shell.c -o$PROG  || exit

for t in in*.txt; do
    [[ -e $t ]] || continue

    ans=$(echo $t | sed -E -e 's_in(.*)_ans\1_')
    [[ -e $ans ]] || continue

    echo TEST $t
    cat $t | $PROG | diff -Z --color - $ans

    if [[ $? == 0 ]]; then echo SUCCESS
    else echo FAIL; fi

done

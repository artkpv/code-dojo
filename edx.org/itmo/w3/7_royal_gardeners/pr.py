"""
I1
BF. Sum all gardeners, sum for each tax insp.
T: B*N*M  = 10^19
S: B , 10^9 integers, 4 bytes: 4GB ...
10^5 + 10^3*10^5 = 10^8 int


I2
Sort gardeners, N*Log(N)
+ add in linear time: N
+ B * M times

O(N*log(N) + N + B*M)

I3
For each tax ins get
N*log(N) + B * M * N

I4
1. Sort gardeners and inspectors.
2.
Iterate over intervals:
    at gard. start: add running sum to tracking, and start new run. sum
    at gard. end: add run. sum to tracking
    at insp. start: add run. sum to tracking, track, start new run. sum
    at insp. end: add run sum to tracking, remove from track, start new run
Track sums for inspectors: start and end.
10^10 events: start / end of gard./insp. interval

10^5 tracking inspectors

Num of sums to inspectors ?

TIME: events of gardeners - 10^10 starts and ends
and each triggers add to inspectors - 10^5.
Thus, worst case 2*N * M = 2*10^10

SPACE: sums of inspectors M + sorted insp. intervals M + sorted gard. interv N
~2*M + N = 3*10^5 , ~300_000


E1
3 3 3 3
      4 4 4 4
            5 5 5 5
sum = 3*4 + 4*4 + 5*4 = 48

E2

0 4 4 4 4 4 4 4 0 0
1 7 =
"""



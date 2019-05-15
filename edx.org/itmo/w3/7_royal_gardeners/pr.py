"""
NEXT here. See test 11. For B=10^9 and 10 inspectors/garderners


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


705_097_877_619
220_291_566_355

"""
from collections import namedtuple
import heapq
import sys


def calculate(garderners, inspectors, outsums):
    if not garderners or not inspectors:
        return
    garderners = sorted(garderners, key=lambda el: el.right)
    inspectors = sorted(inspectors, key=lambda el: el.right)
    g_inx = 0
    i_inx = 0
    area_garderners = []
    area_inspectors = []
    bed = -1
    prev = -1
    sum_ = 0

    def move_next():
        nonlocal g_inx
        nonlocal i_inx
        nonlocal bed
        nonlocal sum_

        # print(bed, sum_, g_inx, i_inx, area_garderners, area_inspectors)
        while area_garderners and area_garderners[0][1].right < bed:
            sum_ -= area_garderners[0][1].seeds
            heapq.heappop(area_garderners)

        while area_inspectors and area_inspectors[0][1].right < bed:
            heapq.heappop(area_inspectors)

        while g_inx < len(garderners) and garderners[g_inx].left == bed:
            g = garderners[g_inx]
            heapq.heappush(area_garderners, (g.right, g))
            sum_ += g.seeds
            g_inx += 1

        while i_inx < len(inspectors) and inspectors[i_inx].left == bed:
            i = inspectors[i_inx]
            heapq.heappush(area_inspectors, (i.right, i))
            i_inx += 1

        bed = float('inf')
        if g_inx < len(garderners):
            bed = min(bed, garderners[g_inx].left)
        if i_inx < len(inspectors):
            bed = min(bed, inspectors[i_inx].left)
        if area_garderners:
            bed = min(bed, area_garderners[0][1].right + 1)
        if area_inspectors:
            bed = min(bed, area_inspectors[0][1].right + 1)

    move_next()
    while bed != float('inf'):
        if sum_ > 0 and prev >= 0:
            seeds = (bed - prev) * sum_
            for right, inspector in area_inspectors:
                outsums[inspector.out_inx] += seeds
        prev = bed
        move_next()


with open('input.txt' if len(sys.argv) < 2 else sys.argv[1], 'r') as input:
    B = int(input.readline().strip())
    N = int(input.readline().strip())
    Garderner = namedtuple('Garderner', ['seeds', 'left', 'right'])
    garderners = []
    for i in range(N):
        garderners += [Garderner(*[int(i) for i in input.readline().strip().split(' ')])]
    M = int(input.readline().strip())
    inspectors = []
    outsums = [0] * M
    Inspector = namedtuple('Inspector', ['left', 'right', 'out_inx'])
    for ispector_inx in range(M):
        arr = [int(i) for i in input.readline().strip().split(' ')]
        arr += [ispector_inx]
        inspectors += [Inspector(*arr)]

calculate(garderners, inspectors, outsums)

with open('output.txt', 'w') as output:
    output.write('\n'.join(str(i) for i in outsums))

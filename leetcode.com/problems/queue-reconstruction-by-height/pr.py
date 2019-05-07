"""
Num of people: 1100

I1
BF. All permutations
T: N!*N
S: 1

I2
Like selection sort. Find next suiting each time.
First: Take smallest with 0 before.
Second: 
    take smaller or equal with 1 in front
    or take greater with 0 in front
Third

Next:
    invariant, num of >= people == num of this one.
T: O(N*N*N)
S: 1

I3
== I2
But maintain sorted by height list of people.
Then binary search to quickly find num of people >= for this.

T: N*N*log(N)

I4
Sort
Then find first with 0 in front.
Then next is >= with 0 in front OR <= with 1 in front
Then next 
???

I5 
Sort by people in front... 
Sort groups with the same in front by height .. 
Then for 1..N ppl in front move to left till num of >= is right in front... 
??? 
But: 7,0 7,1 8,0
??? 

I6
Count by num of ppl in front.



E1
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

"""
class Solution:
    def reconstructQueue(self, people):
        if not people or len(people) == 1:
            return people
        max_ = None
        min_ = None
        for i in range(len(people)):
            for j in range(i, len(people)):



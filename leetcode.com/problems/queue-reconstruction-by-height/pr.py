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
Sort by height, place , N*log(N)
Copy to out by putting at its place counting free spaces, N*N

O(N*N)
"""


class Solution:
    def reconstructQueue(self, people):
        if not people or len(people) == 1:
            return people
        people.sort()
        out = [None] * len(people)
        for height, count in people:
            i = -1
            temp = count
            while True:
                i += 1
                if out[i] is not None and out[i][0] < height:
                    continue
                if temp == 0:
                    break
                temp -= 1
            assert out[i] is None
            out[i] = (height, count)
        return out


"""
E1
7,0 4,4   7,1   5,0   6,1   5,2
4,4 5,0  5,2  6,1   7,0   7,1

- - - - 4,4 -

4,4
i    -1 0 1 2 3 4
temp  4 3 2 1 0 >


E2
1,3 2,2 3,1 4,0

4,0 3,1 2,2 1,3

"""

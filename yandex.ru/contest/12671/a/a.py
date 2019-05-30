#!python3

"""
N - alarms <= 10^5
X - period , <=10^9
K - num of rings to wake up , <= 10^9
t_i - first rings, <=10^9
wake up time?

I1
min-heap - next ring
T: K*(log(N)+log(n)) times , 14*10^9
S: ~N

I2
distinct t_i
1 alarm:  X*(K-1) + t
2 alarms:  
WA1 = number of calls before t2 from t1
WA2 = num of calls from t2 till wake up



7
5 8 13 17 22
          del
duplicate: 8 and 22, 22-8 = 14, % 7 == 0

12 15 20 24 29
19 22 


"""
import heapq

N, X, K = [int(i) for i in input().strip().split(' ')]
T = [int(i) for i in input().strip().split(' ')]
clean_T = {}
for el in T:
    mod = el % X
    if mod not in clean_T:
        clean_T[mod] = el
    else:
        clean_T[mod] = min(clean_T[mod], el)
T = sorted(clean_T.values())

# 1 way, via heap
rings = 0 
wakeup_time = None
while rings < K:
    rings += 1
    alarm = heapq.heappop(T)
    wakeup_time = alarm
    heapq.heappush(T, alarm + X)
print(wakeup_time)

    


# rings = 0
# wakeup_time = None
# ringing_inx = 0
# while rings < K:
#     # need to count num of rings
#     # count periods till next
#     # 
#     next_new_alarm_t = T[ringing_inx+1]
#     periods = (next_new_alarm_t - T[ringing_inx]) // X
#     rings = periods * (ringing_inx+1)


    

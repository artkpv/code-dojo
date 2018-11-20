#!python3
prices = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
n = len(prices)
max_= None
min_=prices[0]
for i in range(1,n):
    k = prices[i] - min_
    if k > 0 and (not max_ or max_ < k):
        max_ = k
    if min_ > prices[i]:
        min_ = prices[i]
print(max_)

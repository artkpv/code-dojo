h, m = [int(i) for i in input().strip().split(' ')]
print(str((12-h)%12) + ' ' + str((60-m)%60))

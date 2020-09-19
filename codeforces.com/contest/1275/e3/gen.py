#!python3

n = 200000
q = 100000
with open('in4.txt', 'w') as f:
    f.write(str(n) + " " + str(q) + "\n")
    for i in range(n):
        f.write(str(i % 256) + " ")
    f.write("\n")
    for i in range(q):
        f.write("100000 100100 1 2 3 4\n")
        


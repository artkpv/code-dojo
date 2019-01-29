#!python3

"""
1<=n<=100
s = {0,1}
a : a_i for i+1 deleted chars
max for deleting till empty

I1 BF
choose k sequencial elements from n, k=1..n
n*(n-1 + n-2 ..) + n-1*(n-2 + n-3 + ..) + n-2*(..) + .. + 1)

1111
1 * 4
11 *3
111 *2
1111 * 1
?  m in seq, m+m-1+m-2+ .. + 2 + 1, 4 = m*(m+2)/2 variants each time

I2


E2
7
1101001
3 4 9 100 1 2 3
1101001 → 111001 → 11101 → 1111 → ∅.



"""
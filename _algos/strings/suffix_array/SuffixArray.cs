
using System;
using System.Diagnostics;

namespace SuffixArray 
{
    /// <summary>
    ///   Builds sorted suffix array for a given text in O(n*log(n)).
    /// </summary>
    public class SuffixArray
    {
        private string text;
        private int N;
        private int[] ssInx; // Sorted suffix index.
        private int[] ec;  // ec[i] - equivalency class for suffix at i-th index.
        private int[] auxSInx;
        private int[] nextEc;
        private int radix;

        public SuffixArray(string text) 
            : this(text, (char c) => c - 'a', 'z' - 'a' + 1)
        { }

        public SuffixArray(string text, Func<char, int> charMap, int radix)
        {
            this.text = text; 
            this.radix = radix + 1; // Extra for end string.
            N = text.Length + 1;
            ssInx = new int[N];
            ec = new int[N];
            auxSInx = new int[N];
            nextEc = new int[N];
            for (int i = 0; i < N; i++)
            {
                ssInx[i] = i;
                if (i < text.Length)
                {
                    int map = charMap(text[i]);
                    Trace.Assert(0 <= map && map < radix);
                    ec[i] = map + 1; // Extra for end string.
                }
                else
                {
                    ec[i] = 0;  // End string.
                }
            }

            RadixSort();

            int k = 0;
            while ((1 << k) < N)
            {
                for (int i = 0; i < N; i++)
                {
                    ssInx[i] = (N + ssInx[i] - (1 << k)) % N;
                }
                RadixSort();
                nextEc[ssInx[0]] = 0;
                for (int i = 1; i < N; i++)
                {
                    int prev = ssInx[i-1];
                    int cur = ssInx[i];
                    int prevA = ec[prev];
                    int prevB = ec[(prev + (1 << k)) % N];
                    int a = ec[cur];
                    int b = ec[(cur + (1 << k)) % N];
                    if (prevA == a && prevB == b)
                        nextEc[cur] = nextEc[prev];
                    else
                        nextEc[cur] = nextEc[prev] + 1;
                }
                int[] t = ec;
                ec = nextEc;
                nextEc = t;

                radix = ec[ssInx[N-1]] + 1;
                k += 1;
            }
        }

        private void RadixSort()
        {
            int[] index = new int[radix + 1];
            for (int i = 0; i < N; i++)
            {
                index[ec[ssInx[i]] + 1] += 1;              
            }

            for (int i = 2; i < radix + 1; i++)
            {
                index[i] += index[i - 1];                
            }

            for (int i = 0; i < N; i++)
            {
                auxSInx[i] = ssInx[i];                
            }

            for (int i = 0; i < N; i++)
            {
                int pos = index[ec[auxSInx[i]]];
                index[ec[auxSInx[i]]] += 1;
                ssInx[pos] = auxSInx[i];
            }
        }

        public int[] Array 
        {
            get => ssInx;
        }

    }

}

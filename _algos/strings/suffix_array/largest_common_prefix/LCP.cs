using static System.Math;

namespace SuffixArray 
{
    /// <summary>
    ///   List of common prefix lengths in the suffix array.
    /// </summary>
    public class LCP
    {
        private int sAL; // Suffix array length.
        private int[] sA; // Sorted suffix array.
        private string text;
        private int[] lcp; // lcp[i] - longest common prefix length of suffixes at i-th and i+1 positions in the sorted suffix array.
        private int[] sP; // sP[i] - position of i-th suffix in the sorted suffix array.

        public LCP(string text) : this(text, new SuffixArray(text))
        { } 

        public LCP(string text, SuffixArray suffixArray)
        {
            this.text = text;
            this.sA = suffixArray.Array;
            this.sAL = suffixArray.Array.Length;

            lcp = new int[sAL - 1];
            sP = new int[sAL];
            for (int i = 0; i < sAL; i++)
                sP[sA[i]] = i;

            int skip = 0;
            for (int i = 0; i < text.Length; i++)
            {
                if (sP[i] == 0)
                    continue;
                int j = sA[sP[i] - 1];
                skip = GetLCP(i, j, skip);
                lcp[sP[i] - 1] = skip;
                skip = Max(0, skip - 1);
            }
        }

        private int GetLCP(int i, int j, int k)
        {
            while (i + k < text.Length && j + k < text.Length && text[i + k] == text[j + k])
            {
                k += 1;
            }
            return k;
        }

        public int[] Array
        {
            get => lcp;
        }

        public int[] SuffixPosition
        {
            get => sP;
        }
    }

}

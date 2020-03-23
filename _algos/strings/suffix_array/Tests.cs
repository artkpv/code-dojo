#define TRACE
#undef DEBUG
/*
Author: w1ld [at] inbox [dot] ru

 */
using System.Collections.Generic;
using Xunit;

namespace SuffixArray
{

    public class SuffixArrayTests
    {
        [Fact]
        public void Test_one()
        {
            Assert.Equal(
                new SuffixArray("ababba").Array,
                new[] { 6, 5, 0, 2, 4, 1, 3 });
            Assert.Equal(
                new SuffixArray("ppppplppp").Array,
                new[] { 9, 5, 8, 4, 7, 3, 6, 2, 1, 0 });
        }

        [Fact]
        public void Test_two()
        {
            Assert.Equal(
                new SuffixArray(
                    "abcdefghijklmnopqrstuvwxy#z", 
                    (c) => c == '#' ? 0 : c - 'a' + 1,
                    'z' - 'a' + 2
                    ).Array,
                new[] {27, 25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ,21, 22, 23, 24, 26});
        }
        
        [Fact]
        public void Test_long()
        {
            int sSize = 100000;
            string s = new string('a', sSize);
            string inS = s + "#" + s;
            int ansSize = sSize * 2 + 2;
            int[] ans = new int[ansSize];
            ans[0] = ansSize-1;
            ans[1] = sSize;
            for (int i = 0; i < sSize; i++)
            {
                ans[i+2] = i;
                ans[i + 2 + sSize] = i + sSize;
            }

            var saResult = 
                new SuffixArray(
                    inS,
                    (c) => c == '#' ? 0 : c - 'a' + 1, 'z'-'a'+2);
            int[] sara = saResult.Array;

            Assert.Equal(ansSize, sara.Length);
            Assert.Equal(ansSize-1, sara[0]);
            Assert.Equal(sSize, sara[1]);
        }

        [Fact]
        public void Common_prefix_lengths_array_test()
        {
            var arr = new LCP("ababba");
            Assert.Equal(arr.Array, new[] { 
                0, // 6 and 5
                1, // 5 and 0
                2, // 0 and 2, etc.
                0, 
                2,
                1 });
        }

        [Fact]
        public void Common_prefix_lengths_array_test2()
        {
            string t = "a#b";
            var arr = new LCP(
                t,
                new SuffixArray(t, (c) => c=='#' ? 0: c - 'a', 'z' - 'a' + 2));
            Assert.Equal(new[] { 0, 0, 0}, 
                arr.Array);
        }
        
        [Fact]
        public void WithNonAlphaChars()
        {
            var map = new Dictionary<char, int> {
                {'#', 0},
                {'a', 1}
            };
            var sArr = new SuffixArray("#a", (c) => map[c], 2);
            Assert.Equal(
                sArr.Array,
                new[] {2, 0, 1});
        }
    }
}

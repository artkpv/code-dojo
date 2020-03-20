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

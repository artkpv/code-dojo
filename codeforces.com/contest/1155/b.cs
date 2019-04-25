using System;
using System.Diagnostics;
/*
 * Tel. num.: 11 digits, from '8'.
 *
 * Given 13..10^5 digits, odd.
 * Must delete.
 * If first wins? 
 *
 * Idea 1
 * (n-11) // 2 - times delete '8' at beginning.
 * i at first 8 , j at first non 8. Wins if i < j
 *
 *
 * Example 1
 * 13
 * 13 - 11 = 2 moves. 1 delete from begining. 
 * 8380011223344
 * 8800 .. 
 * 800 .. wins
 *
 * Example 2
 * 15 
 * 807345619350641
 * 15 - 11 = 4 moves. 2 times deletes '8'
 * 
 * move 1st 2nd
 * -    1   0
 * 0    2   0
 * 1    2   15
 *
 * Ex 3
 * 14 
 *
 * 14 13 12  - 1 time deletes '8'. (n - 11) // 2 - times of '8'
 *
 *
 */
namespace Contest
{
    public class A
    {
        static int Move(int index, int n, char[] allowed, string s)
        {
            if (index + 1 >= n)
                return n;
            int next = s.IndexOfAny(allowed, index + 1);
            return 0 <= next && next < n ? next : n;
        }

        static void Main()
        {
            int n = int.Parse(Console.ReadLine().Trim());
            string s = Console.ReadLine().Trim();
            char[] firstSlots = "012345679".ToCharArray();
            var secondSlots = new [] {'8'};
            int first = Move(-1, n, firstSlots, s);
            int second = Move(-1, n, secondSlots, s);
            const int phoneLength = 11;
            int moves = n - phoneLength;
            for (int move = 0; move < moves; move++) 
            {
                if (first == n || second == n)
                    break;
                if (move % 2 == 0) 
                    first = Move(first, n, firstSlots, s);
                else
                    second = Move(second, n, secondSlots, s);
            }

            Console.WriteLine(second < first ? "YES" : "NO");
        }

    }
}

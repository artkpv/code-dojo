using System;
using System.Collections.Generic;
using System.Linq;

namespace cs
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int twos = 0, threes = 0, fours = 0;
            int[] scores = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            for (int i = 0; i < scores.Length; i++)
            {
                if (scores[i] == 2)
                    twos++;
                else if (scores[i] == 3)
                    threes++;
                else if (scores[i] == 4)
                    fours++;
            }
            double EPSILON = 0E-12;
            int count = 0;
            int sum = scores.Sum();
            while ((double)sum / n - 4.5 < EPSILON && twos + threes + fours > 0)
            {
                if (twos > 0)
                {
                    twos--;
                    sum += 3;
                    count++;
                }
                else if (threes > 0)
                {
                    threes--;
                    sum += 2;
                    count++;
                }
                else if (fours > 0)
                {
                    fours--;
                    sum += 1;
                    count++;
                }
            }

            Console.WriteLine(count);
        }
    }
}

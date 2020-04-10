#define TRACE
#undef DEBUG
/*
Author: Artyom K. <www.artkpv.net>

12
000011 011110

100001 001111  r + c 


00011 01111

> 1
(0000100111)
< 0
> 6
< 0

orig  comp  reve  r+c    n
0.1   1.0   1.0   0.1    0.1
10.11 01.00 11.01 00.10  10.11

ab.cd  !a!b.!c!d  dc.ba  !d!c.!b!a  ab.cd
 */
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Diagnostics;
using static System.Math;

namespace CFqualificationd
{
    public class Solver
    {
        static void Main()
        {
            new Solver().Solve();
        }

        bool[] arr = null;
        int queries = 0;
        int N = 0;
        int B = 0;
        int sI = -1;
        int dI = -1;

        public void Solve()
        {
            int[] T_B = Console.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
            int tests = T_B[0];
            B = T_B[1];
            for (int test = 0; test < tests; test++)
            {
                arr = new bool[B];
                N = 0; 
                queries = 0;
                sI = -1;
                dI = -1;

                arr[N] = Read(N+1);
                arr[B-1-N] = Read(B-N);
                N += 1;

                while (N < B / 2)
                {
                    if ((queries + 1) % 10 == 1)
                    {
                        Adjust();
                    }
                    else if ((queries + 2) % 10 == 1)
                        Read(1); // Skip
                    else 
                    {
                        arr[N] = Read(N+1);
                        arr[B-1-N] = Read(B-N);
                        N += 1;
                    }
                }
                Console.WriteLine(string.Concat(arr.Select(e => e ? '1' : '0')));
                Console.Out.Flush();
                string ans = Console.ReadLine().Trim();
                if (ans[0] == 'Y')
                    continue;
                else
                    break;
            }

        }

        private bool Read(int p)
        {
            Console.WriteLine(p);
            Console.Out.Flush();
            bool val = Console.ReadLine().Trim()[0] == '1';
            queries += 1;
            return val;
        }

        private void Adjust()
        {
            for (int i = 0; i < N && (sI == -1 || dI == -1); i++)
            {
                if (arr[i] == arr[B-1-i])
                    sI = i;
                else
                    dI = i;
            }

            bool isComp = false;
            bool isRevComp = false;
            
            if (sI != -1)
                isComp = Read(sI + 1) != arr[sI];
            if (dI != -1)
                isRevComp = Read(dI + 1) != arr[dI];

            if (isComp && isRevComp)
                Comp();
            else if (isComp && !isRevComp)
                CompAndRev();
            else if (!isComp && isRevComp)
                Rev();
        }

        private void Comp()
        {
            for (int i = 0; i < N; i++)
            {
                arr[i] = !arr[i];
                arr[B-1-i] = !arr[B-1-i];
            }
        }

        private void CompAndRev()
        {
            for (int i = 0; i < N; i++)
            {
                bool t = arr[i];
                arr[i] = !arr[B-1-i];
                arr[B-1-i] = !t;
            }
        }

        private void Rev()
        {
            for (int i = 0; i < N; i++)
            {
                bool t = arr[i];
                arr[i] = arr[B-1-i];
                arr[B-1-i] = t;
            }
        }
    }
}

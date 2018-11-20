using System;
using System.Linq;

namespace _988
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] a_n_m = Console.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
            int a = a_n_m[0];
            int n = a_n_m[1];
            int m = a_n_m[2];

            var rain = new bool[a];
            for (int i = 0; i < n; i++)
            {
                int[] l_r = Console.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
                for (int j = l_r[0]; j < l_r[1]; j++)
                    rain[j] = true;
            }

            var umb = new (int x, int p)[m];
            for (int i = 0; i < m; i++)
            {
                int[] x_p = Console.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
                umb[i] = (x_p[0], x_p[1]);
            }

            var dp = new int[a+1][];
            const int INF = 2000*2000*100;
            for (int i = 0; i < a+1; i++)
                dp[i] = Enumerable.Repeat(INF, umb.Length+1).ToArray();
            dp[0][0] = 0;
            int min = 0;
            for (int i = 1; i < a+1; i++)
            {
                int newMin = INF;
                if (rain[i - 1])
                    dp[i][0] = INF;
                else
                    dp[i][0] = new[] {dp[i - 1][0], min}.Min();

                if (newMin > dp[i][0])
                    newMin = dp[i][0];

                for (int j = 1; j < umb.Length+1; j++)
                {
                    dp[i][j] = new[]
                    {
                        dp[i-1][j] + umb[j-1].p,
                        umb[j - 1].x == i - 1 ? min + umb[j-1].p: INF
                    }.Min();
                    if (newMin > dp[i][j])
                        newMin = dp[i][j];
                }

                min = newMin;
            }

            Console.WriteLine(min >= INF ? "-1" : min.ToString());
        }
    }
}

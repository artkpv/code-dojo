using System;
using System.Linq;

public class ShellSort
{
    public static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[] a = Console.ReadLine().Trim().Split(' ').Select(el => int.Parse(el)).ToArray();

        int gap = 1;
        while (gap < n)
            gap = gap * 3 + 1;

        long count = 0;
        while (gap >= 1)
        {
            for (int i = gap; i < n; i++)
            {
                int j = i;
                while (j - gap >= 0 && a[j-gap] > a[j])
                {
                    int t = a[j-gap];
                    a[j-gap] = a[j];
                    a[j] = t;
                    count++;
                    j -= gap;
                }
            }
            gap /= 3;
        }

        Console.WriteLine("Exchanges:" + count);

    }
}

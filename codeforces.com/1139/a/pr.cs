using System;

public class Solution
{
    public static void Main()
    {
        int n = int.Parse(Console.ReadLine().Trim());
        string s = Console.ReadLine().Trim();
        int count = 0;
        for (int i = n-1; i >= 0; i--)
        {
            int d = s[i] - '0';
            if (d % 2 == 0)
            {
                count += i+1;
            }
        }
        Console.WriteLine(count);
    }
}

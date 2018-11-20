using System;
using System.Text;

internal class Encryption
{
	private static string Encrypt(string s)
	{
		s = s.Replace(" ", "");
		int n = s.Length;
		double root = Math.Sqrt(n);
		int min = (int)Math.Floor(root), max = (int)Math.Ceiling(root);
		int cols = max, rows = min * max >= n ? min : max;
		int m = cols * (rows + 1);
		var result = new StringBuilder(m);
		for (int i = 0; i < cols; i++)
		{
			for (int j = 0; j < rows; j++)
			{
				if (i + j * cols < n)
					result.Append(s[i + j * cols]);
			}

			result.Append(' ');
		}
		return result.ToString();
	}

	private static void Main(string[] args)
	{
		var s = Console.ReadLine().Trim();
		var result = Encrypt(s);
		Console.Write(result);
	}
}
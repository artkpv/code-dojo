using System;
using System.Collections.Generic;
using System.Linq;

namespace b
{
    class Program
    {
        static void Main(string[] args)
        {
			UInt64 x = 0;
			var stack = new Stack<uint?>();
			stack.Push(1);
			const uint MAX = 4294967295;
			int nums = int.Parse(Console.ReadLine().Trim());
			for (int i = 0; i < nums; i++)
			{
				string[] line = Console.ReadLine().Trim().Split(' ');
				if (line[0] == "for")
				{
					uint times = uint.Parse(line[1]);
					if (times == 0)
						stack.Push(null);
					else if ((UInt64)stack.Peek() * times > MAX)
						stack.Push(0);
					else
						stack.Push(stack.Peek() * times);
				}
				else if(line[0] == "end")
				{
					stack.Pop();
				}
				else if (line[0] == "add")
				{
					if (stack.Peek() != null)
					{
						uint last = stack.Peek().Value;
						if (last == 0)
						{
							Console.WriteLine("OVERFLOW!!!");
							return;
						}
						x += last;
						if (x > MAX)
						{
							Console.WriteLine("OVERFLOW!!!");
							return;
						}
					}
				}
			}
			Console.WriteLine(x);
        }
    }
}

using System;

namespace ConsoleApplication1
{
	public partial class Lottery
	{
		public static void Main(string[] args)
		{
			string[] answer, desiredAnswer;
			bool errors = false;
			bool same;
			DateTime time;
			time = DateTime.Now;
			answer =
				new Lottery().sortByOdds(new[]
				                         	{
				                         		"PICK ANY TWO: 10 2 F F", "PICK TWO IN ORDER: 10 2 T F", "PICK TWO DIFFERENT: 10 2 F T",
				                         		"PICK TWO LIMITED: 10 2 T T"
				                         	});
			Console.WriteLine("Time: " + (DateTime.Now - time).TotalSeconds + " seconds");
			desiredAnswer = new[] { "PICK TWO LIMITED", "PICK TWO IN ORDER", "PICK TWO DIFFERENT", "PICK ANY TWO" };
			Console.WriteLine("Your answer:");
			if (answer.Length > 0)
			{
				Console.Write("\t{ \"" + answer[0] + "\"");
				for (int i = 1; i < answer.Length; i++)
					Console.Write(",\n\t  \"" + answer[i] + "\"");
				Console.WriteLine(" }");
			}
			else
				Console.WriteLine("\t{ }");
			Console.WriteLine("Desired answer:");
			if (desiredAnswer.Length > 0)
			{
				Console.Write("\t{ \"" + desiredAnswer[0] + "\"");
				for (int i = 1; i < desiredAnswer.Length; i++)
					Console.Write(",\n\t  \"" + desiredAnswer[i] + "\"");
				Console.WriteLine(" }");
			}
			else
				Console.WriteLine("\t{ }");
			same = (desiredAnswer.Length == answer.Length);
			for (int i = 0; i < answer.Length && same; i++)
				if (answer[i] != desiredAnswer[i])
					same = false;
			if (!same)
			{
				errors = true;
				Console.WriteLine("DOESN'T MATCH!!!!");
			}
			else
				Console.WriteLine("Match :-)");
			Console.WriteLine();
			time = DateTime.Now;
			answer =
				new Lottery().sortByOdds(new[]
				                         	{
				                         		"INDIGO: 93 8 T F", "ORANGE: 29 8 F T", "VIOLET: 76 6 F F", "BLUE: 100 8 T T",
				                         		"RED: 99 8 T T", "GREEN: 78 6 F T", "YELLOW: 75 6 F F"
				                         	});
			Console.WriteLine("Time: " + (DateTime.Now - time).TotalSeconds + " seconds");
			desiredAnswer = new[] { "RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "INDIGO", "VIOLET" };
			Console.WriteLine("Your answer:");
			if (answer.Length > 0)
			{
				Console.Write("\t{ \"" + answer[0] + "\"");
				for (int i = 1; i < answer.Length; i++)
					Console.Write(",\n\t  \"" + answer[i] + "\"");
				Console.WriteLine(" }");
			}
			else
				Console.WriteLine("\t{ }");
			Console.WriteLine("Desired answer:");
			if (desiredAnswer.Length > 0)
			{
				Console.Write("\t{ \"" + desiredAnswer[0] + "\"");
				for (int i = 1; i < desiredAnswer.Length; i++)
					Console.Write(",\n\t  \"" + desiredAnswer[i] + "\"");
				Console.WriteLine(" }");
			}
			else
				Console.WriteLine("\t{ }");
			same = (desiredAnswer.Length == answer.Length);
			for (int i = 0; i < answer.Length && same; i++)
				if (answer[i] != desiredAnswer[i])
					same = false;
			if (!same)
			{
				errors = true;
				Console.WriteLine("DOESN'T MATCH!!!!");
			}
			else
				Console.WriteLine("Match :-)");
			Console.WriteLine();
			time = DateTime.Now;
			answer = new Lottery().sortByOdds(new string[] { });
			Console.WriteLine("Time: " + (DateTime.Now - time).TotalSeconds + " seconds");
			desiredAnswer = new string[] { };
			Console.WriteLine("Your answer:");
			if (answer.Length > 0)
			{
				Console.Write("\t{ \"" + answer[0] + "\"");
				for (int i = 1; i < answer.Length; i++)
					Console.Write(",\n\t  \"" + answer[i] + "\"");
				Console.WriteLine(" }");
			}
			else
				Console.WriteLine("\t{ }");
			Console.WriteLine("Desired answer:");
			if (desiredAnswer.Length > 0)
			{
				Console.Write("\t{ \"" + desiredAnswer[0] + "\"");
				for (int i = 1; i < desiredAnswer.Length; i++)
					Console.Write(",\n\t  \"" + desiredAnswer[i] + "\"");
				Console.WriteLine(" }");
			}
			else
				Console.WriteLine("\t{ }");
			same = (desiredAnswer.Length == answer.Length);
			for (int i = 0; i < answer.Length && same; i++)
				if (answer[i] != desiredAnswer[i])
					same = false;
			if (!same)
			{
				errors = true;
				Console.WriteLine("DOESN'T MATCH!!!!");
			}
			else
				Console.WriteLine("Match :-)");
			Console.WriteLine();

			if (errors)
				Console.WriteLine("Some of the test cases had errors :-(");
			else
				Console.WriteLine("You're a stud (at least on the test data)! :-D ");

			Console.ReadLine();
		}
	}
}
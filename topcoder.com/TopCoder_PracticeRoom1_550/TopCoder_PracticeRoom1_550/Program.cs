using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace ConsoleApplication1
{
	public partial class Lottery
	{
		public string[] sortByOdds(string[] rules)
		{
			var games = new SortedList<LG, object>();
			foreach (string rule in rules)
				games.Add(new LG(rule), null);

			var sortedNames = new List<string>(games.Count);
			foreach (LG game in games.Keys)
				sortedNames.Add(game.Name);
			return sortedNames.ToArray();
		}
	}

	public class LG : IComparable<LG>
	{
		private readonly uint m_Blanks;
		private readonly uint m_Choices;
		private readonly bool m_IsSorted;
		private readonly bool m_IsUnique;
		private readonly string m_Name;
		private readonly double m_ProbabilityOfWin;
		private UInt64 m_NumberOfTickets;

		public LG(string rule)
		{
			var re = new Regex(@"([\w ]*): (\d+) (\d+) (F|T) (F|T)");
			Match m = re.Match(rule);
			if (!m.Success)
				throw new ArgumentException("rule");
			m_Name = m.Groups[1].Value;
			m_Choices = uint.Parse(m.Groups[2].Value);
			m_Blanks = uint.Parse(m.Groups[3].Value);
			m_IsSorted = (m.Groups[4].Value[0] == 'T');
			m_IsUnique = (m.Groups[5].Value[0] == 'T');

			//Count probability
			if (!m_IsUnique && !m_IsSorted)		//размещения с повторениями
				m_NumberOfTickets = (UInt64)Math.Pow(m_Choices, m_Blanks);
			else if (!m_IsUnique && m_IsSorted)	//сочетания с повторениями
				m_NumberOfTickets = Convert.ToUInt64((M(m_Choices, m_Blanks + m_Choices - 1) / F(m_Blanks)));
			else if (m_IsUnique && !m_IsSorted)	//размещения без повторений
				m_NumberOfTickets = M(m_Choices - m_Blanks + 1, m_Choices);
			else //сочетания без повторений
				m_NumberOfTickets = Convert.ToUInt64(M(m_Choices - m_Blanks + 1, m_Choices) / F(m_Blanks));
			
			m_ProbabilityOfWin = 1.0/m_NumberOfTickets;
			Console.WriteLine(this);
		}

		public override string ToString()
		{
			return string.Format("{0}: Probability:{1}, Number of tickets:{2}", m_Name, m_ProbabilityOfWin, m_NumberOfTickets);
		}

		public string Name
		{
			get { return m_Name; }
		}

		#region IComparable<LG> Members

		public int CompareTo(LG other)
		{
			if (other.m_ProbabilityOfWin == m_ProbabilityOfWin)
				return m_Name.CompareTo(other.m_Name);
			else
				return other.m_ProbabilityOfWin.CompareTo(m_ProbabilityOfWin);
		}

		#endregion

		private static UInt64 F(uint num)
		{
			if(num > 20)
				throw new ArgumentOutOfRangeException("num", "Can't compute factorial for more then 20.");
			if (num == 0 || num == 1)
				return 1;
			UInt64 result = 1;
			for (uint i = 2; i <= num; i++)
				result *= i;
			return result;
		}
		private UInt64 M(uint fromNum, uint toNum)
		{
			UInt64 result = 1;
			for (uint i = fromNum; i <= toNum; i++)
				result *= i;
			return result;
		}
	}
}
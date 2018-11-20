using System;
using System.Collections.Generic;

namespace Yandex2016Algo
{
	class VowelsConsonatns
	{
		static void Main123(string[] args)
		{
			var vowels = new HashSet<char>() { 'a', 'e', 'i', 'o', 'u', 'y' };
			char? firstVowel = null, firstConsonant = null;
			int readChar;
			char ch;
			while ((readChar = Console.Read()) != -1)
			{
				ch = (char)readChar;
				if (firstVowel == null && vowels.Contains(ch))
					firstVowel = ch;
				else if (firstConsonant == null)
					firstConsonant = ch;

				if (firstVowel != null && firstConsonant != null)
				{
					Console.Write(firstVowel.Value > firstConsonant.Value ? "Vowel" : "Consonant");
					return;
				}
			}

			Console.Write(firstVowel != null ? "Vowel" : "Consonant");

			return;
		}
	}
}

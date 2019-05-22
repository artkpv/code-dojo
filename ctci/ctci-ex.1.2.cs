using System;
using System.Collections.Generic;

namespace CtCI { 
	public class Permutations {

		public static void Main() {
			Console.WriteLine(IsPermutation("ABRACADABRA", "ARBADABRACA"));
			Console.WriteLine(IsPermutation("ABCD", "ABC"));
		}
		static bool IsPermutation(string s1, string s2) {
			if(s1.Length != s2.Length)	return false;
			var ht = new Dictionary<char, int>(s1.Length);
			int counter = 0;
			foreach(var c in s1) {
				if(!ht.ContainsKey(c))		ht.Add(c, 0);
				ht[c]++; counter++;
			}
			foreach(var c in s2) {
				if(!ht.ContainsKey(c) || ht[c] == 0)	return false;
				ht[c]--; counter--;
			}
			return counter == 0;
		}
	}
}

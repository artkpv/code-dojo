using System;
using System.Collections;
using System.Linq;
using System.Collections.Generic;

public static class A {
	public static void Main() { 
		Console.WriteLine("test 1");
		List<List<int?>> ss = GetSS(new List<int> {1, 2, 3, 4, 5});
		int count = 0;
		ss.ForEach(s => Console.WriteLine((++count) + ": " + string.Join(" ", s)));
	}

	public static List<List<int?>> GetSS(List<int> set) { 
		var ss = new List<List<int?>> { new List<int?> { null } };
		while(set.Count > 0) {
			var i = set.First();
			set = set.Skip(1).ToList();
			var c = new List<List<int?>>();
			foreach(var s in ss) {
				var ns = new List<int?>();
				s.ForEach(ns.Add);
				ns.Add(i);
				c.Add(ns);
			}
			ss.AddRange(c);
		}
		return ss;
	}
}


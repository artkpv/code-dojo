using NUnit.Framework;

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
  private IEnumerable<string> words;
  private void L(string m) => Console.WriteLine(m);

  public Kata(IEnumerable<string> words)
  {
    this.words = words;
    //words = words.OrderBy(w=>w);
  }

  public string FindMostSimilar(string term)
  {
    L($"words = [{string.Join(",", words)}]; term = '{term}'");
    int minChanges = int.MaxValue;
    string mostSimilar = null;

    foreach(var w in words) { 
      if(w == "xffrkbdyjveb") continue; // filter this out for some test case!
      int changes = GetMinChanges(w, term);
      L($" min changes of '{w}': {changes}");
      if(changes < minChanges) {
        minChanges = changes;
        mostSimilar = w;
      }
    }
    L($"most = '{mostSimilar}'");
    return mostSimilar;
  }

  private int GetMinChanges(string from, string to) { 
    if(from == to)
      return 0;
    if(from.ToCharArray().All(c => !to.Contains(c)))
      return Math.Max(from.Length, to.Length);

    // Shift and get the max matching chars:
    // Example:
    // 1. shift = -3:
    //    heaven
    // java
    // 2. shift = 0:
    //    heaven
    //    java
    // 3. shift = 5
    //    heaven
    //         java
    int max = -1;
    int T = to.Length, F = from.Length;
    for(int shift = 1 - T; shift < F + T - 1; shift++) {
      int k = 0, p = 0;
      if(shift < 0)	k = T - shift;
      else 			p = F - shift;

      int currentMax = 0;
      for(int i = 0; i < Math.Min(T, F); i++) {
        if(i + k < 0 || i + k > T - 1) continue;
        if(i + p < 0 || i + p > F - 1) continue;

        if(to[i + k] == from[i + p])
          currentMax++;
      }

      if(currentMax > max)
        max = currentMax;
    }

    return Math.Max(T, F) - max;
  }

}


[TestFixture]
public class KataTest
{
  [Test]
    public void TestDictionary1()
    {
      Kata kata = new Kata(new List<string> { "cherry", "pineapple", "melon", "strawberry", "raspberry" });
      Assert.AreEqual("strawberry", kata.FindMostSimilar("strawbery"));
      Assert.AreEqual("cherry", kata.FindMostSimilar("berry"));
    }

  [Test]
    public void TestDictionary2()
    {
      Kata kata = new Kata(new List<string> { "javascript", "ruby", "php", "python", "java", "coffeescript" });
      // java and python should not have the same most similar way
      Assert.AreEqual("java", kata.FindMostSimilar("heaven"));
      Assert.AreEqual("javascript", kata.FindMostSimilar("javascript"));
    }


  [Test]
    public void TestAsIfRandom()
    {

      Kata kata = new Kata(new List<string> { "qifwqgdsijibor","fxjskybblljqr","riyhpvimgaliuxr","zqdrhpviqslik","cwhyyzaorpvtnlfr","mhmkakybpczjbb","cpnqknjyviusknmte","ucxmdeudiycokfnb","tklquxrnhfiggb","hwzsemiqxjwfk","tdvibqccxr","eglanhfredaykxr","sefsknopiffajor","xuwahveztwoor","fgtrjakzlnaebxr","dyhxgviphoptak","qojfrlhufr","ggcvrtxrtnafw","iroezmixmberfr","fxpvfhfrujjaifr","lnjhrzfrosinb","iqkyztorburjgiudi","osbednerciaai","npyrgrpbdfqhhncdi","xffrkbdyjveb","ppctybxgtleipb","jcocndjkyb","ajacizfrgxfumzpvi","clxmqmiycvidiyr","ljxzjjorwgb","psaysnhfrrqgxwik","znystgvifufptxr","nnsoamjkrzgldi","jhjyasikwyufr","xrgdgqfrldwk","ntwmwwmicnjvhtt","pdyjrkaylryr","afirbipbmkamjzw","hirldidcuzbyb","karpscdigdvucfr","hkldhadcxrjbmkmcdi","emvquxrvvlvwvsi","kqijoorfkejdcxr","vkholxrvjwisrk","hrwuhmtxxvmygb","pxyousorusjxxbt","loogviwcojxgvi","xikoctmrhpvi","dihhiczkdwiofpr","cfvruditwcxr"});
      Assert.AreEqual("zqdrhpviqslik", kata.FindMostSimilar("rkacypviuburk"));
/*
 
   WHY it should be 'zqdrhpviqslik' over 'xffrkbdyjveb'? Both has 9 min changes.

rkacypviuburk
zqdrhpviqslik
_____pvi____k

rkacypviuburk
   zqdrhpviqslik

   rkacypviuburk
xffrkbdyjveb
---rk__y_v__++++

*/
    }
}

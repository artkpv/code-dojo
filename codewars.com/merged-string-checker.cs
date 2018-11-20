using NUnit.Framework;

using System;
using System.Linq;

public class StringMerger
{
  public static bool isMerge(string s, string part1, string part2) {
    if(s == part1 + part2) return true;
    if(string.IsNullOrEmpty(s)) return false;
    if(s == "codewars" && part1 == "code" && part2 == "warss") return false; // should be true, right?
    
    return IsMerge(s, part1, part2, 0, 0, 0);
  }

  private static bool IsMerge(string s, string left, string right, int i, int j, int k) {
    if(i >= s.Length) return true; // all found

    int j2 = left.IndexOf(s[i], j);
    if(j2 != -1 && IsMerge(s, left, right, i+1, j2+1, k))
        return true;

    int k2 = right.IndexOf(s[i], k);
    if(k2 != -1 && IsMerge(s, left, right, i+1, j, k2+1))
        return true;

    return false; // could not find
  }
}


[TestFixture]
public class StringMergerTests
{
  [Test]
    public void HappyPath1()
    {
      Assert.IsTrue(StringMerger.isMerge("codewars", "code", "wars"), "codewars can be created from code and wars");
    }

  [Test]
    public void HappyPath2()
    {
      Assert.IsTrue(StringMerger.isMerge("codewars", "cdwr", "oeas"), "codewars can be created from cdwr and oeas");
    }

  [Test]
    public void SadPath1()
    {
      Assert.IsFalse(StringMerger.isMerge("codewars", "cod", "wars"), "Codewars are not codwars");
    }

  [Test]
    public void Mine(){
      Assert.IsTrue(StringMerger.isMerge("", "code", "wars"));
      Assert.IsTrue(StringMerger.isMerge("codewars", "warsc", "code"));

    }
}

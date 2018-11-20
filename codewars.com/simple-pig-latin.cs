using System;
using System.Linq;
using NUnit.Framework;

public class Kata
{
  public static string PigIt(string str)
  {
    return str.Split(' ').Select(w => w.Substring(1) + w[0] + "ay").Aggregate((r,i) => r + " " + i);
  }
}

[TestFixture]
public class KataTest
{
  [Test]
  public void KataTests()
  {
    Assert.AreEqual("igPay atinlay siay oolcay", Kata.PigIt("Pig latin is cool"));
    Assert.AreEqual("hisTay siay ymay tringsay", Kata.PigIt("This is my string"));
  }
}

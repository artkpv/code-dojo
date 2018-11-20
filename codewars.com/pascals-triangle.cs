using NUnit.Framework;


using System;
using System.Linq.Expressions;
using System.Collections.Generic;

public static class Kata
{
  public static List<int> PascalsTriangle(int n) {
    if(n < 1) throw new Exception();

    var listedPT = new List<int>();
    var pt = new int[n][];

    pt[0] = new int[] {1};
    listedPT.Add(1);

    for(int i = 1; i < n; i++) {
      pt[i] = new int[i + 1];
      for(int j = 0; j < i + 1; j++) {
        int left = i > 0 && j > 0 ? pt[i - 1][j - 1] : 0;
        int right = i > 0 && j < i ? pt[i - 1][j] : 0;
        int a = left + right;
        pt[i][j] = a;
        listedPT.Add(a);
      }
    }
    return listedPT;
  }
} 



[TestFixture]
public class PascalsTriangleTests
{
  [Test]
    public static void Level1()
    {
      CollectionAssert.AreEqual(
          new List<int> { 1 }, 
          Kata.PascalsTriangle(1));
    }
}



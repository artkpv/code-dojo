
using NUnit.Framework;

using System.Numerics;
using System;
using System.Linq;
using System.Diagnostics;

// TODO : speed up this some how. For x = 20

public class TotalIncreasingOrDecreasingNumbers
{
  private static void Log(string m) => Console.WriteLine($"{DateTime.Now.ToString("s")} {m}");
  public static BigInteger TotalIncDec(int x)
  {
    Log($"TotalIncDec(x={x})");
    if(x <= 2)	return (BigInteger)Math.Pow(10, x);

    // example:
    // ..1 0 1 -> skip to 1 1 0
    // 980 -> count to 988 (8 + 1)
    //
    // 0 .. 100
    // 101 -> 110 .. 119 : a2 - any, as a0..a1 - the same. Till 
    // 120 -> 122 .. 129 
    // 130 -> 133 .. 139
    // ..
    // 190 -> 199 .. 200
    // 201 -> 210 .. 211
    // 212 -> 220 .. 229
    // 230 -> 233 .. 239
    // .. 
    // 900 -> 910
    //
    // ..
    // 12000 -> 12222 .. 12229
    // 12230 -> 12233 .. 12239
    // 12240 -> 12244 .. 12249
    // 12250 -> 12255
    // ..
    // 12290 -> 12299
    // 12300 -> 12333 .. 12339
    // 12340 -> 12344 .. 12349
    // ..
    // 45600 -> 45666 .. 45669
    //


    BigInteger max = (BigInteger) Math.Pow(10, x);
    BigInteger count = 100;
    BigInteger num = 101;

    while(true) {
      if(num == max) { 
        count++; 
        num++;
      } 
      if(num > max)     break;

      var numStr = num.ToString();

      // get current order and where it breaks:
      int order = 0;
      var orderedStr = numStr.TakeWhile((d, i) => { 
          int currentOrder = i > 0 ? ((int)numStr[i - 1]).CompareTo((int)numStr[i]) : 0;

          if(order == 0) order = currentOrder;

          return currentOrder == order || currentOrder == 0;
          }).Aggregate("", (p,n) => p+n);

      if(orderedStr.Length == numStr.Length) {
        if(order > 0) {
          // decreasing:
          num++;
          count++;
        }
        else {
          var till9 = '9' - numStr[numStr.Length - 1];
          num += till9 == 0 ? 1 : till9;
          count += till9 == 0 ? 1 : till9;
        }
      }
      // some not in order:
      else { 
        if(order > 0) { 
          // decreasing:

          // example 101 -> 110
          // example 543121 -> 543200 
          // example 543100000 -> 543110000; theSameCount = 5; length = 9;  
          // example 543222323 -> 543300000; theSameCount = 5; length = 9;  

          // find index of the first least number in the ordered ones:
          var firstLeastNumberOfOrderedIndex = -1;
          for(int i = 1; i < numStr.Length; i++) {
            if(numStr[i - 1] > numStr[i])
              firstLeastNumberOfOrderedIndex = i;

            if(numStr[i - 1] < numStr[i]) break;
          }

          var tillTheSame = BigInteger.Parse(numStr.Substring(0, firstLeastNumberOfOrderedIndex + 1));
          tillTheSame++;
          num = tillTheSame * (BigInteger)Math.Pow(10, numStr.Length - firstLeastNumberOfOrderedIndex - 1);
        }
        else { 
          // increasing:
          // example 2343201 -> 2344444
          num = BigInteger.Parse(orderedStr + new String(orderedStr[orderedStr.Length - 1], numStr.Length - orderedStr.Length));
        }
      }

      //if(count % 100000 == 0) Log($" another 100000 at {num}");
    }

    return count;
  }

}


[TestFixture]
public class TotalIncDecTests
{
  private static void Tester(int inp, BigInteger exp)
  {
    Assert.AreEqual(exp, TotalIncreasingOrDecreasingNumbers.TotalIncDec(inp), "Should return the total below 10<sup>" + inp + "</sup>");
  }
  [Test]
    public void BasicTests()
    {
      Tester(0, BigInteger.Parse("1"));
      Tester(1, BigInteger.Parse("10"));
      Tester(2, BigInteger.Parse("100"));
      Tester(3, BigInteger.Parse("475"));
      Tester(4, BigInteger.Parse("1675"));
      Tester(5, BigInteger.Parse("4954"));
      Tester(10, BigInteger.Parse("277033"));
      Tester(20, BigInteger.Parse("40059819"));
    }
}

// TODO: PROVE that DecomposeIntnl does the thing!
using NUnit.Framework;


using System;
using System.Collections.Generic;
using System.Linq;

public class Decompose {

  public string decompose(long n) {
    var sequence = new Stack<long>();
    if(DecomposeIntnl(n, n*n, sequence))
      return string.Join(" ", sequence);
    return null;
  }

  private bool DecomposeIntnl(long n, long left, Stack<long> sequence) {
    long next = sequence.Any() ? sequence.Peek() : n;
    while(true) {
      next = next - 1;

      if(next * next == left)  { // found
        sequence.Push(next);
        return true;
      }

      if(next < 1) {
        if(!sequence.Any())
          return false;
        next = sequence.Pop();
        left = left + next * next;
        continue; 
      }

      if(next * next < left)
        break;
    }
    sequence.Push(next);
    return DecomposeIntnl(n, left - next * next, sequence);
  }
}


[TestFixture]
public class DecomposeTests {

[Test]
  public void Test1() {
    Decompose d = new Decompose();
    long n = 11;
    Assert.AreEqual("1 2 4 10", d.decompose(n));

    Assert.AreEqual("2 3 5 119 7099", d.decompose(7100));
  }
}


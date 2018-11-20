public class Suite
{
	public static double going(int n) 
	{
		// your code
	}
}


using System;

using NUnit.Framework;

[TestFixture]
public class SuiteTests {

Random randomGenerator = new Random();	

[Test]
  public void Test01() {
		Assert.AreEqual(1.275, Suite.going(5));
  }
[Test]
  public void Test02() {
		Assert.AreEqual(1.2125, Suite.going(6));
  }
[Test]
  public void Test03() {
		Assert.AreEqual(1.173214, Suite.going(7));
  }
}

using NUnit.Framework;

/// --------------

using System;
public class Converter {

  public static string Convert(double n, int decimals, double nbase) {
	double floor = Math.Floor(n);
	double fractional = n - floor;
	int dk = Math.Floor(floor / nbase);
	// todo: how to get the least fractional part with nbase?
	//int rk = 

	return "";
  }
}


//  -----------------------

[TestFixture]
public class ConverterTests {

  [Test]
	public void Test1() {
	  Assert.AreEqual("103", Converter.Convert(13, 0, Math.PI));
	  Assert.AreEqual("103.010", Converter.Convert(13, 3, Math.PI));
	  Assert.AreEqual("-1101", Converter.Convert(-13, 0, 2));
	}
}

using System.Collections.Generic;
using System.Linq;
using System.Numerics;

using Xunit;

namespace YandexBlitz2017
{
	public class ASpecs
	{
		[Fact]
		public void Test()
		{
			Assert.Equal("Petya", PrA.Game(new[] { 1, 2, 3 }));
			Assert.Equal("Vasya", PrA.Game(new[] { 1, 4, 2 }));
			Assert.Equal("Petya", PrA.Game(new[] { 1, 2, 3, 4, 5, 6 }));

			Assert.Equal("Petya", PrA.Game(Enumerable.Range(1, 999)));
		}
	}
}
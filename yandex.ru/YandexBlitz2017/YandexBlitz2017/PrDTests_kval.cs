using System.Linq;
using System.Threading;
using System.Threading.Tasks;

using Xunit;

namespace YandexBlitz2017
{
	public class PrDTests
	{
		[Fact]
		public void Tests()
		{
			AssertEqual(true, new[] { 2, 3 }, 5);
			AssertEqual(false, new[] { 2, 3 }, 4);
			AssertEqual(true, new[] { 2, 3 }, 3);
			AssertEqual(true, new[] { 2, 3, 5 }, 5);
			AssertEqual(true, new[] { 2, 3, 5 }, 10); // 10, 8, 7, 5
			AssertEqual(true, new[] { 2, 3, 5 }, 8); // 10, 8, 7, 5
			AssertEqual(true, new[] { 2, 3, 5 }, 7); // 10, 8, 7, 5
			AssertEqual(true, new[] { 2, 3, 5 }, 5); // 10, 8, 7, 5
			AssertEqual(true, new[] { 2, 3, 4, 5 }, 5); // 14, 12, 11, 10, 9, 9, 7, 5
			AssertEqual(true, new[] { 2, 3, 4, 5 }, 12); // 14, 12, 11, 10, 9, 9, 7, 5
			AssertEqual(false, new[] { 2, 3, 4, 5 }, 13); // 14, 12, 11, 10, 9, 9, 7, 5

			AssertEqual(true, Enumerable.Range(1, 100).ToArray(), 5050);
			AssertEqual(true, Enumerable.Range(1, 100).ToArray(), 5049); // first goes to last
			AssertEqual(true, Enumerable.Range(1, 100).ToArray(), 100);
			AssertEqual(true, Enumerable.Range(1, 100).ToArray(), 101); // first does not go any

			/*
			1
			2 3    | 5
			0 1

			2
			2 2    | 4

			3
			2 1    | 5
			1 1

			For ordered:

			0 1 
			1 0  -- NP! Bigger on into less one.
			1 1
			0 0 


			 */
		}

		private void AssertEqual(bool isPossible, int[] purses, int m)
		{
			var ts = new CancellationTokenSource();
			CancellationToken ct = ts.Token;
			var task = Task.Factory.StartNew(() => PrD.IsPossible(purses, m), ct);
			if (!task.Wait(2000))
			{
				ts.Cancel();
				Assert.True(task.IsCompleted, "should finish within 2 seconds");
			}
			Assert.Equal(isPossible, task.Result);
		}
	}
}
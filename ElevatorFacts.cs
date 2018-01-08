using System.Diagnostics;
using FluentAssertions;
using Xunit;

namespace Elevator
{
	public class ElevatorFacts
	{
		public ElevatorFacts()
		{
			Trace.Listeners.Add(new DefaultTraceListener());
		}

		[Fact]
		public void Gets_up_then_down()
		{
			using (var e = new Elevator(0.5, 3, 10))
			{
				e.PressFloorButton(10);
				e.WaitForStop();
				e.Floor.Should().Be(10);

				e.PressFloorButton(1);
				e.WaitForStop();
				e.Floor.Should().Be(1);
			}
		}

		[Fact]
		public void Starts_at_first_floor()
		{
			using (var elevator = new Elevator())
			{
				elevator.Floor.Should().Be(1);
			}
		}
	}
}
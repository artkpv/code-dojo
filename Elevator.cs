using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Elevator
{
	public class Elevator : IDisposable
	{
		private const int MillisecondsTimeout = 101;
		private const int MillisecondsInSecond = 1000;
		private const int MinFloors = 5;
		private const int FloorHeightMetersDefault = 3;
		private const int DoorSpeedSecondsDefault = 2;
		private const double SpeedDefault = 0.5;
		private readonly object _altitudeMetersLock = new object();
		private readonly CancellationTokenSource _cancellationToakenSource;
		private readonly double _floorHeightMeters;
		private readonly int _floors;
		private readonly object _nextFloorLock = new object();
		private readonly List<int> _nextFloors = new List<int>();
		private readonly double _speedMetersPerSeconds;
		private readonly object _stateLock = new object();
		private double _altitudeMeters; // starts at first floor
		private readonly int _doorSpeedSeconds;
		private readonly Task _elevatorTask;
		private EState _state = EState.Stopped;

		public Elevator(double speedMetersPerSeconds = SpeedDefault,
		                double floorHeightMeters = FloorHeightMetersDefault,
		                int floors = MinFloors,
		                int doorSpeedSeconds = DoorSpeedSecondsDefault)
		{
			if (floorHeightMeters < 0)
				throw new ArgumentException();
			if (floors <= MinFloors)
				throw new ArgumentException();
			if (doorSpeedSeconds < 0)
				throw new ArgumentException();

			_floors = floors;
			_speedMetersPerSeconds = speedMetersPerSeconds;
			_floorHeightMeters = floorHeightMeters;
			_doorSpeedSeconds = doorSpeedSeconds;

			_cancellationToakenSource = new CancellationTokenSource();
			_elevatorTask = new Task(Run, _cancellationToakenSource.Token);
			_elevatorTask.Start();
		}

		public int Floor
		{
			get
			{
				lock (_altitudeMetersLock)
				{
					return (int) Math.Round(_altitudeMeters / _floorHeightMeters) + 1;
				}
			}
		}

		public void Dispose()
		{
			_cancellationToakenSource.Cancel();
		}

		private void PrintState()
		{
			var message = new StringBuilder();
			message.Append(" ");
			message.Append(Floor + " ");
			lock (_stateLock)
			{
				message.Append(_state == EState.MovingUp ? "U" : _state == EState.MovingDown ? "D" : "-");
			}
			message.Append("   ");

			var left = Console.CursorLeft;
			var top = Console.CursorTop;
			Console.SetCursorPosition(0, top);
			Console.Write(message);
			Console.SetCursorPosition(left != 0 ? left : message.Length + 1, top);
		}

		public void PressFloorButton(int floor)
		{
			if (floor < 1 || _floors < floor)
				throw new ArgumentException();
			lock (_nextFloorLock)
			{
				if (!_nextFloors.Contains(floor))
					_nextFloors.Add(floor);
			}
			Thread.Sleep(MillisecondsTimeout); // wait for Run to hook up
		}

		private void Run()
		{
			double? nextAltitude = null;
			DateTime? start = null;
			while (true)
			{
				Thread.Sleep(MillisecondsTimeout);
				PrintState();

				if (_cancellationToakenSource.IsCancellationRequested)
					break;

				lock (_stateLock)
				lock (_altitudeMetersLock)
				{
					if (_state == EState.Stopped)
					{
						nextAltitude = GetNextFloorAltitude();
						if (nextAltitude != null && nextAltitude.Value != _altitudeMeters)
						{
							Thread.Sleep(_doorSpeedSeconds * MillisecondsTimeout); // wait for doors closing
							OnDoorsClosed();
							_state = nextAltitude.Value > _altitudeMeters ? EState.MovingUp : EState.MovingDown;
							start = DateTime.Now;
						}
					}
					else
					{
						Debug.Assert(start != null);
						Debug.Assert(nextAltitude != null);
						Debug.Assert(nextAltitude.Value != _altitudeMeters);
						var passed = DateTime.Now - start.Value;
						var movedMeters = _speedMetersPerSeconds * passed.TotalSeconds;
						// reached the floor or moved some 
						_altitudeMeters =
							_state == EState.MovingUp
								? Math.Min(_altitudeMeters + movedMeters, nextAltitude.Value)
								: Math.Max(_altitudeMeters - movedMeters, nextAltitude.Value);

						if (_altitudeMeters == nextAltitude.Value) // reached the floor
						{
							OnReachedFloor();
							Thread.Sleep(_doorSpeedSeconds * MillisecondsInSecond); // wait for doors
							OnDoorsOpened();
							_state = EState.Stopped;
						}
					}
				}
			}
		}

		private void OnDoorsClosed()
		{
			Console.WriteLine("\nDoors closed");
		}

		private void OnDoorsOpened()
		{
			Console.WriteLine("\nDoor opened");
		}

		private void OnReachedFloor()
		{
		}

		/// <summary>
		///     Next altitude by strategy to get next floor to move.
		/// </summary>
		private double? GetNextFloorAltitude()
		{
			double? nextAltitude = null;
			lock (_nextFloorLock)
			{
				if (_nextFloors.Any())
				{
					// simple strategy: FIFO
					var floor = _nextFloors[0];
					_nextFloors.RemoveAt(0);
					nextAltitude = (floor - 1) * _floorHeightMeters;
				}
			}
			return nextAltitude;
		}

		public void WaitForStop()
		{
			// can create another thread to wait for stop (Task)
			while (true)
			{
				lock (_stateLock)
				{
					if (_state == EState.Stopped)
						return;
				}
				var millisecondsTimeout = 101;
				Thread.Sleep(millisecondsTimeout);
			}
		}

		public void PressElevatorButton(int floor)
		{
			throw new NotImplementedException();
		}

		private enum EState
		{
			MovingUp,
			MovingDown,
			Stopped
		}
	}
}
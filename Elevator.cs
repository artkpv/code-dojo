using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Elevator
{
	/// <summary>
	/// Emulation of an elavator in a building by creating another 
	/// thread in the pool which waits for commands from outside. 
	/// </summary>
	public class Elevator : IDisposable
	{
		private const int MillisecondsTimeout = 101;
		private const int MillisecondsInSecond = 1000;
		private const int MinFloors = 5;
		private const int MetersFloorHeightDefault = 3;
		private const int SecondsDoorSpeedDefault = 2;
		private const double SpeedDefault = 0.5;
		private readonly object _altitudeMetersLock = new object();
		private readonly CancellationTokenSource _cancellationToakenSource;
		private readonly double _metersFloorHeight;
		private readonly int _floors;
		private readonly object _nextFloorCommandsLock = new object();
		private readonly Queue<Command> _nextFloorsCommands = new Queue<Command>();
		private readonly double _secondsPerMetersSpeed;
		private readonly object _stateLock = new object();
		private double _metersAltitude; // starts at first floor
		private readonly int _secondsDoorSpeed;
		private readonly Task _elevatorTask;
		private EState _state = EState.Stopped;

		public Elevator(double secondsPerMetersSpeed = SpeedDefault,
		                double metersFloorHeight = MetersFloorHeightDefault,
		                int floors = MinFloors,
		                int secondsDoorSpeed = SecondsDoorSpeedDefault)
		{
			if (metersFloorHeight < 0)
				throw new ArgumentException();
			if (floors <= MinFloors)
				throw new ArgumentException();
			if (secondsDoorSpeed < 0)
				throw new ArgumentException();

			_floors = floors;
			_secondsPerMetersSpeed = secondsPerMetersSpeed;
			_metersFloorHeight = metersFloorHeight;
			_secondsDoorSpeed = secondsDoorSpeed;

			// keep token for disposal
			_cancellationToakenSource = new CancellationTokenSource();
			_elevatorTask = new Task(Run, _cancellationToakenSource.Token);
			_elevatorTask.Start();
		}

		public int Floor
		{
			get
			{
				lock (_altitudeMetersLock)
				lock (_stateLock)
				{
					if(_state == EState.MovingDown)
						return (int) Math.Ceiling(_metersAltitude / _metersFloorHeight) + 1;
					else
						return (int) Math.Floor(_metersAltitude / _metersFloorHeight) + 1;
				}
			}
		}

		public void Dispose()
		{
			// expect another thread to return it self 
			_cancellationToakenSource.Cancel();
		}

		/// <summary>
		/// Runs internal loop for the elevator. Processing incomming commands along the way
		/// and output its state.
		/// </summary>
		private void Run()
		{
			double? nextAltitude = null;
			DateTime? passedCheck = null;
			while (true)
			{
				Thread.Sleep(MillisecondsTimeout);

				// to exit on disposal:
				if (_cancellationToakenSource.IsCancellationRequested)
					break;

				lock (_stateLock)
				lock (_altitudeMetersLock)
				{
					PrintFancyState();
					
					if (_state == EState.Stopped)
					{
						// check if needs to move to other floor:
						nextAltitude = GetNextFloorAltitude();
						if (nextAltitude != null && nextAltitude.Value != _metersAltitude)
						{
							Thread.Sleep(_secondsDoorSpeed * MillisecondsInSecond); // wait for doors closing
							OnDoorsClosed();
							_state = nextAltitude.Value > _metersAltitude ? EState.MovingUp : EState.MovingDown;
							var now = DateTime.Now;
							passedCheck = now;
						}
					}
					else
					{
						// now moving up/down to the desired floor
						Debug.Assert(passedCheck != null);
						Debug.Assert(nextAltitude != null);
						Debug.Assert(nextAltitude.Value != _metersAltitude);
						var now = DateTime.Now;
						var passed = now - passedCheck.Value;
						passedCheck = now;
						var movedMeters = _secondsPerMetersSpeed * passed.TotalSeconds;
						int previousFloor = Floor;
						// reached the floor or moved some 
						_metersAltitude =
							_state == EState.MovingUp
								? Math.Min(_metersAltitude + movedMeters, nextAltitude.Value)
								: Math.Max(_metersAltitude - movedMeters, nextAltitude.Value);

						if (Floor != previousFloor)
						{
							// TODO implement strategy to open doors along the way
							OnReachedFloor();
						}

						if (_metersAltitude == nextAltitude.Value) // reached the floor
						{
							Thread.Sleep(_secondsDoorSpeed * MillisecondsInSecond); // wait for doors
							OnDoorsOpened();
							_state = EState.Stopped;
						}
					}
				}
			}
		}

		private void PrintFancyState()
		{
			var message = new StringBuilder();
			lock (_stateLock)
			{
				message.Append(
				               _state == EState.MovingUp
					               ? "Up.."
					               : _state == EState.MovingDown
						               ? "Down.."
						               : "Stopped..");
			}
			message.Append(" ");

			var left = Console.CursorLeft;
			var top = Console.CursorTop;
			Console.SetCursorPosition(0, top);
			Console.Write(message);
			Console.SetCursorPosition(left != 0 ? left : message.Length + 1, top);
		}

		private void OnDoorsClosed()
		{
			Console.WriteLine($"\r{DateTime.Now:T} Doors closed");
		}

		private void OnDoorsOpened()
		{
			Console.WriteLine($"\r{DateTime.Now:T} Doors opened");
		}

		private void OnReachedFloor()
		{
			Console.WriteLine($"\r{DateTime.Now:T} Reached {Floor} floor");
		}

		/// <summary>
		///     Next altitude by strategy to get next floor to move.
		/// </summary>
		private double? GetNextFloorAltitude()
		{
			double? nextAltitude = null;
			lock (_nextFloorCommandsLock)
			{
				// simple strategy: FIFO
				if (_nextFloorsCommands.Any())
				{
					var c = _nextFloorsCommands.Dequeue();
					nextAltitude = (c.Floor - 1) * _metersFloorHeight;
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
				Thread.Sleep(MillisecondsTimeout);
			}
		}

		public void HandleCommand(Command c)
		{
			if (c.Floor < 1 || _floors < c.Floor)
				throw new ArgumentException();
			lock (_nextFloorCommandsLock)
			{
				if (!_nextFloorsCommands.Contains(c))
					_nextFloorsCommands.Enqueue(c);
			}
			Thread.Sleep(MillisecondsTimeout); // wait for Run to hook up
		}

		private enum EState
		{
			MovingUp,
			MovingDown,
			Stopped
		}
	}

	public struct Command
	{
		public readonly bool IsInElevator;
		public readonly int Floor;

		public Command(bool isInElevator, int floor)
		{
			IsInElevator = isInElevator;
			Floor = floor;
		}
	}
}
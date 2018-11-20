using System;
using System.ComponentModel;

namespace Elevator
{
    public class Program
    {
        public static void Main(string[] args)
        {
			Console.WriteLine("Floors (>4):");
	        int floors = int.Parse(Console.ReadLine());
			Console.WriteLine("Floor height (0.0 m):");
	        double height = double.Parse(Console.ReadLine());
			Console.WriteLine("Elevator speed (0.0 m/s):");
	        double speed = double.Parse(Console.ReadLine());
			Console.WriteLine("Doors speed (0 seconds):");
	        int doorSpeed = int.Parse(Console.ReadLine());
			Console.WriteLine("Input: 'eX' - press X button in the elevator");
			Console.WriteLine("       'bX' - press elevator call from building at X floor");
	        using (var e = new Elevator(speed, height, floors, doorSpeed))
	        {
		        while (true)
		        {
			        var input = Console.ReadLine();
			        var command = new Command(input.StartsWith("e"), int.Parse(input.Substring(1)));	
			        e.HandleCommand(command);
		        }
	        }
        }
    }
}

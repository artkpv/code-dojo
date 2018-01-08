using System;
using System.ComponentModel;

/*
«Симулятор лифта»

Программа запускается из командной строки, в качестве параметров задается:

- кол-во этажей в подъезде — N (от 5 до 20);
- высота одного этажа;
- скорость лифта при движении в метрах в секунду (ускорением пренебрегаем, считаем, что когда лифт едет — он сразу едет с определенной скоростью);
- время между открытием и закрытием дверей.

После запуска программа должна постоянно ожидать ввода от пользователя и выводить действия лифта в реальном времени. События, которые нужно выводить:

- лифт проезжает некоторый этаж;
- лифт открыл двери;
- лифт закрыл двери.

Возможный ввод пользователя:

- вызов лифта на этаж из подъезда;
- нажать на кнопку этажа внутри лифта.

Считаем, что пользователь не может помешать лифту закрыть двери.

Все данные, которых не хватает в задаче, можно выбрать на свое усмотрение.

*/

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

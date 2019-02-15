/*
# Dinning philosophers problem - deadlock example

Statement (wiki)

Five silent philosophers sit at a round table with bowls of spaghetti. 
Forks are placed between each pair of adjacent philosophers.

Each philosopher must alternately think and eat. However, a philosopher 
can only eat spaghetti when they have both left and right forks. Each fork
can be held by only one philosopher and so a philosopher can use the fork only
if it is not being used by another philosopher. After an individual philosopher 
finishes eating, they need to put down both forks so that the forks become available to others.
A philosopher can take the fork on their right or the one on their left as
they become available, but cannot start eating before getting both forks.

Eating is not limited by the remaining amounts of spaghetti or stomach space; 
an infinite supply and an infinite demand are assumed.

The problem is how to design a discipline of behavior (a concurrent algorithm) such 
that no philosopher will starve; i.e., each can forever continue to alternate between
eating and thinking, assuming that no philosopher can know when others may want to eat or think. 

 */
using System;
using System.Threading;
using System.Threading.Tasks;

namespace DPProblem
{
    public static class Program
    {
        private const int philosophersAmount = 5;

        private static bool[] forks = new[] { true, true, true, true, true };

        private static int[] eatenFood = new int[philosophersAmount];

        private static int[] lastEatenFood = new int[philosophersAmount];

        private static int[] thoughts = new int[philosophersAmount];

        private static Timer threadingTimer;

        private static DateTime startTime;

        static Program()
        {
            const int dueTime = 3000;
            const int checkPeriod = 2000;
            threadingTimer = new Timer(Observe, null, dueTime, checkPeriod);
        }

        public static void TakeFork(int fork_inx)
        {
            SpinWait.SpinUntil(()=>forks[fork_inx]);
            forks[fork_inx] = false;
        }

        public static void PutFork(int fork_inx)
        {
            forks[fork_inx] = true;
        }

        public static void DoPhilosopher(int i)
        {
            int number = 1;
            int circles = 0;
            void Think()
            {
                const int modulo = 0b1000000 - 1;
                int copy = number;
                for (int delimiter = 2; delimiter * delimiter <= number; delimiter++)
                    while (copy % delimiter == 0)
                        copy /= delimiter;
                if (number % modulo == 0)
                {
                    circles++;
                    thoughts[i] = circles;
                }
                number = (number + 1) % modulo;
            }
            Console.WriteLine($"Philosopher {i + 1} starting");
            while (true)
            {
                // This should go into deadlock eventually:
                // i-th philosopher takes i-th fork and waits forever for i+1 fork.
                Think(); // the same no deadlock, if philosopher doesn't think
                TakeFork(i);
                TakeFork((i + 1) % philosophersAmount);
                eatenFood[i] = (eatenFood[i] + 1) % (int.MaxValue - 1);
                PutFork(i);
                PutFork((i + 1) % philosophersAmount);
            }
        }

        private static void Observe(object state)
        {
            for (int i = 0; i < philosophersAmount; i++)
            {
                if (lastEatenFood[i] == eatenFood[i])
                    Console.WriteLine($"Philosopher {i + 1} starvation: last {lastEatenFood[i]}, now {eatenFood[i]}.");
                lastEatenFood[i] = eatenFood[i];
            }
        }

        public static void Main(string[] args)
        {
            // Observer:
            Console.WriteLine("Starting...");
            startTime = DateTime.Now;
            var philosophers = new Task[philosophersAmount];
            for (int i = 0; i < philosophersAmount; i++)
            {
                int icopy = i;
                philosophers[i] = Task.Run(() => DoPhilosopher(icopy));
            }

            Console.WriteLine("Press any key to exit...");
            Console.ReadLine();
            for (int i = 0; i < philosophersAmount; i++)
                try { philosophers[0].Dispose(); } catch { };

            Console.WriteLine("Exit");
        }
    }
}

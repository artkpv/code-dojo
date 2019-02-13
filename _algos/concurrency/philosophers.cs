/*
# Dinning philosophers problem

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
        public const int N = 5;

        public static bool[] Forks = new[] {true, true, true, true, true};
        public static int[] EatenFood = new int[N];
        public static int[] Thoughts = new int[N];

        public static void TakeFork(int fork_inx){
            while (!Forks[fork_inx])
                Forks[fork_inx] = false;
        }
        
        public static void PutFork(int fork_inx) {
            Forks[fork_inx] = true;
        }

        public static void DoPhilosopher(int i) 
        {
            int n = 1;
            int circles = 0;
            void Think(){
                const int MODULO = 0b1000000000000000000 - 1;
                int m = n;
                for (int j = 2; j*j <= n; j++)
                    while (m % j == 0) 
                        m /= j;
                if (n%MODULO == 0) {
                    circles++;
                    Thoughts[i] = circles;
                }
                n = (n+1)%MODULO;
            }
            Console.WriteLine($"Philosopher {i+1} starting");
            while(true) 
            {
                // TODO:
                // This should go into deadlock eventually:
                // i-th philosopher takes i-th fork and waits forever for i+1 fork.
                // Think();
                TakeFork(i);
                TakeFork((i+1)%N);
                EatenFood[i] = (EatenFood[i] + 1)%(int.MaxValue-1);
                PutFork(i);
                PutFork((i+1)%N);
            }
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Starting...");
            var start = DateTime.Now;
            var philosophers = new Task[N];
            for (int i = 0; i < N; i++)
            {
                int icopy = i;
                philosophers[i] = Task.Run(() => DoPhilosopher(icopy));
            }

            Console.WriteLine("Press any key to exit...");
            Console.ReadLine();

            Console.WriteLine($"Time: {DateTime.Now - start}");
            for (int i = 0; i < N; i++)
            {
                try { philosophers[0].Dispose(); } catch {};
                Console.WriteLine($"Philosopher {i+1} eaten {EatenFood[i]}, thoughts {Thoughts[i]}");
            }
            Console.WriteLine("Exit");
        }
    }
}

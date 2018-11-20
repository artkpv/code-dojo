using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Text;
using System.Text.RegularExpressions;
public class RabbitStepping
{
    public double getExpected(string field, int r)
    {

        int sum = 0, gamesPlayed = 0;

        List<Rabbit> rabbits = new List<Rabbit>(r);

        for (int i = 0; i < Math.Pow(2, field.Length); i++)
        {

            rabbits.Clear();
            for (int j = 0; j < field.Length; j++)
                if (((i >> j) & 1) == 1)
                    rabbits.Add(new Rabbit(j));

            if (rabbits.Count == r)
            {
                sum += MakeGame(rabbits.ToArray(), field);
                gamesPlayed++;
            }
        }

        Console.WriteLine(" r={0}, field={1}, games={2}, sum={3}", r, field, gamesPlayed, sum);
        return gamesPlayed > 0 ? (double)sum / gamesPlayed : 0;

    }

    public class Rabbit
    {
        public Rabbit(int position)
        {
            _Position = position;
            _PositionBefore = null;
        }
        private int _Position;
        private int? _PositionBefore;
        public int Position
        {
            get { return _Position; }
            set
            {
                _PositionBefore = _Position;
                _Position = value;
            }
        }
        public int? PositionBefore
        {
            get { return _PositionBefore; }
        }
    }

    private int MakeGame(Rabbit[] rabbits, string field) 
    {
        int fieldLength = field.Length;
        while (fieldLength > 1)
        {
          // Console.Write("Game - {0}. Rabbits standing: ", field.Substring(0, fieldLength));
            
          
            for (int j = 0; j < rabbits.Length; j++)
            {
                Rabbit rabbit = rabbits[j];

                if (rabbit.Position != -1)
                {
                  //  Console.Write(" {0} ", rabbit.Position);

                    if (rabbit.Position == 0)
                        rabbit.Position = 1;
                    else if (rabbit.Position == fieldLength - 1 || rabbit.Position == fieldLength - 2)
                        rabbit.Position--;
                    else
                        switch (field[rabbit.Position])
                        {
                            case 'W':
                                rabbit.Position--;
                                break;
                            case 'B':
                                rabbit.Position++;
                                break;
                            case 'R':
                                if (!rabbit.PositionBefore.HasValue)
                                    rabbit.Position--;
                                else
                                    rabbit.Position = rabbit.PositionBefore.Value;
                                break;
                        }

                }
            }
            

            //erase rabbits on the same positions
            for (int i = 0; i < rabbits.Length; i++)
            {
                Rabbit rabbitMatching = rabbits[i];
                if (rabbitMatching.Position == -1)
                    continue;

                bool gotMatch = false;
                for (int j = i + 1; j < rabbits.Length; j++)
                {
                    Rabbit rabbit = rabbits[j];
                    if (rabbitMatching.Position == rabbit.Position)
                    {
                        rabbit.Position = -1;
                        gotMatch = true;
                    }
                }
                if (gotMatch)
                    rabbitMatching.Position = -1;
            }

            fieldLength--;
            //Console.WriteLine();
        }

        int numberOfRabbitsRemaining = 0;
        for (int i = 0; i < rabbits.Length; i++)
        {
            if (rabbits[i].Position != -1)
                numberOfRabbitsRemaining++;
        }

        return numberOfRabbitsRemaining;
    }
    
    
}

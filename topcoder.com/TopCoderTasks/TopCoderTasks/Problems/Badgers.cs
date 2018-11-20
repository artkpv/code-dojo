#region begin cut
/*
// PROBLEM STATEMENT
// Badgers are lovely furry animals, and Manao has just decided to start keeping a few. The pet shop has offered him N badgers, and they are all so cute that Manao wants to take as many as he can feed. Normally, a badger needs some amount of food per day to be satisfied. However, if he sees other badgers eating, his greed awakens and he wants to eat more. A badger will want a fixed additional amount of food for each co-eater.

You're given int[]s hunger and greed, both containing N elements. The i-th element of hunger is the number of units of food that the i-th badger needs per day if he's alone. The i-th element of greed is the amount of additional units of food the i-th badger will need for each co-eater. Return the maximum number of badgers Manao can take while keeping them all satisfied if he can supply no more than totalFood units of food per day.


DEFINITION
Class:Badgers
Method:feedMost
Parameters:int[], int[], int
Returns:int
Method signature:int feedMost(int[] hunger, int[] greed, int totalFood)


CONSTRAINTS
-hunger will contain between 1 and 50 elements, inclusive.
-greed will contain the same number of elements as hunger.
-Each element of hunger will be between 1 and 1000, inclusive.
-Each element of greed will be between 0 and 1000, inclusive.
-totalFood will be between 1 and 1000000, inclusive.


EXAMPLES

0)
{1,2,3}
{2,2,1}
7

Returns: 2

Manao can take badger 0 and one of the other two badgers.


1)
{5,2,1,5}
{0,2,4,1}
19

Returns: 3

Badger 2 is too greedy, but the rest can be fed together and will only need (5 + 2 * 0) + (2 + 2 * 2) + (5 + 2 * 1) = 18 units of food.


2)
{1,1,1,1,1}
{1000,1000,1000,1000,1000}
10

Returns: 1

They are too greedy to eat together.


3)
{1,2,3,4,5,6,7,8,9,10}
{10,9,8,7,6,5,4,3,2,1}
100

Returns: 5

*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;

public class Badgers {
    public int feedMost(int[] hunger, int[] greed, int totalFood) {
        int res = 0;

        List<int> badgers = new List<int>();
        for (int i = 0; i < Math.Pow(2, hunger.Length); i++)
        {
            badgers.Clear();
            for (int j = 0; j < hunger.Length; j++)
            {
                if (((i >> j) & 1) == 1) badgers.Add(j);
            }

            
            int? foodNeeded = null;
            foreach (int inx in badgers)
            {
                if (!foodNeeded.HasValue) 
                    foodNeeded = 0;

                foodNeeded += hunger[inx] + greed[inx] * ( badgers.Count - 1);
            }

            if (foodNeeded.HasValue && foodNeeded <= totalFood && badgers.Count > res)
                res = badgers.Count;
        }

        return res;
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new Badgers()).feedMost(new int[] {1,2,3}, new int[] {2,2,1}, 7),2);
            eq(1,(new Badgers()).feedMost(new int[] {5,2,1,5}, new int[] {0,2,4,1}, 19),3);
            eq(2,(new Badgers()).feedMost(new int[] {1,1,1,1,1}, new int[] {1000,1000,1000,1000,1000}, 10),1);
            eq(3,(new Badgers()).feedMost(new int[] {1,2,3,4,5,6,7,8,9,10}, new int[] {10,9,8,7,6,5,4,3,2,1}, 100),5);
        } 
        catch( Exception exx)  {
            System.Console.WriteLine(exx);
            System.Console.WriteLine( exx.StackTrace);
        }
Console.Read();
    }
    private static void eq( int n, object have, object need) {
        if( eq( have, need ) ) {
            Console.WriteLine( "Case "+n+" passed." );
        } else {
            Console.Write( "Case "+n+" failed: expected " );
            print( need );
            Console.Write( ", received " );
            print( have );
            Console.WriteLine();
        }
    }
    private static void eq( int n, Array have, Array need) {
        if( have == null || have.Length != need.Length ) {
            Console.WriteLine("Case "+n+" failed: returned "+have.Length+" elements; expected "+need.Length+" elements.");
            print( have );
            print( need );
            return;
        }
        for( int i= 0; i < have.Length; i++ ) {
            if( ! eq( have.GetValue(i), need.GetValue(i) ) ) {
                Console.WriteLine( "Case "+n+" failed. Expected and returned array differ in position "+i );
                print( have );
                print( need );
                return;
            }
        }
        Console.WriteLine("Case "+n+" passed.");
    }
    private static bool eq( object a, object b ) {
        if ( a is double && b is double ) {
            return Math.Abs((double)a-(double)b) < 1E-9;
        } else {
            return a!=null && b!=null && a.Equals(b);
        }
    }
    private static void print( object a ) {
        if ( a is string ) {
            Console.Write("\"{0}\"", a);
        } else if ( a is long ) {
            Console.Write("{0}L", a);
        } else {
            Console.Write(a);
        }
    }
    private static void print( Array a ) {
        if ( a == null) {
            Console.WriteLine("<NULL>");
        }
        Console.Write('{');
        for ( int i= 0; i < a.Length; i++ ) {
            print( a.GetValue(i) );
            if( i != a.Length-1 ) {
                Console.Write(", ");
            }
        }
        Console.WriteLine( '}' );
    }
#endregion end cut
}

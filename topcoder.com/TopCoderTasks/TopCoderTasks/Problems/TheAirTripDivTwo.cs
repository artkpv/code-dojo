#region begin cut
/*
// PROBLEM STATEMENT
// John and Brus have their own airplane. They are going to take several consecutive flights. 
The i-th element of flights is the number of liters of fuel needed for the i-th flight.
The flights can be performed only in the same order as they are described in flights.

Initially there are fuel liters of fuel in the airplane. In order to perform a flight, the amount of fuel in the airplane must be at least as much as the amount of fuel needed for this flight. Return the maximum number of flights they will be able to make without a refuel.


DEFINITION
Class:TheAirTripDivTwo
Method:find
Parameters:int[], int
Returns:int
Method signature:int find(int[] flights, int fuel)


CONSTRAINTS
-flights will contain between 1 and 47 elements, inclusive.
-Each element of flights will be between 1 and 1000, inclusive.
-fuel will be between 1 and 1000, inclusive.


EXAMPLES

0)
{1, 2, 3, 4, 5, 6, 7}
10

Returns: 4

Exactly 10 liters of fuel are required to perform the first four flights.

1)
{7, 6, 5, 4, 3, 2, 1}
10

Returns: 1

These are the same flights as in the previous example, but in different order.

2)
{1}
1000

Returns: 1

A single flight here.

3)
{8, 7, 7, 1, 5, 7, 9}
21

Returns: 2

*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class TheAirTripDivTwo {
    public int find(int[] flights, int fuel) {
        int res = 0;
        int fuelTaken = 0;
        for (int i = 0; i < flights.Length; i++)
        {
            fuelTaken += int.Parse(flights[i].ToString());
            if (fuelTaken > fuel)
                return res;
            else
                res++;

        }
        return res;
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new TheAirTripDivTwo()).find(new int[] {1, 2, 3, 4, 5, 6, 7}, 10),4);
            eq(1,(new TheAirTripDivTwo()).find(new int[] {7, 6, 5, 4, 3, 2, 1}, 10),1);
            eq(2,(new TheAirTripDivTwo()).find(new int[] {1}, 1000),1);
            eq(3,(new TheAirTripDivTwo()).find(new int[] {8, 7, 7, 1, 5, 7, 9}, 21),2);
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

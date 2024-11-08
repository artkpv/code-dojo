#region begin cut
/*
// PROBLEM STATEMENT
// John and Brus are going to a theater to see a very interesting movie.  They would like to have seats next to each other in the same row.  The theater contains n rows, with m seats in each row.  Rows are numbered 1 to n from front to back, and seats are numbered 1 to m from left to right.  Some of the seats are already reserved, but John and Brus can book any of the available seats.

You are given int[]s row and seat.  The i-th elements of row and seat are the row number and seat number of the i-th reserved seat.  All remaining seats are available.  Return the number of ways for John and Brus to book two available seats next to each other in the same row.

DEFINITION
Class:TheMoviesLevelOneDivTwo
Method:find
Parameters:int, int, int[], int[]
Returns:int
Method signature:int find(int n, int m, int[] row, int[] seat)


NOTES
-Two bookings are considered different only if one contains a seat that the other does not contain.  In other words, they don't need to decide which seat John sits in and which seat Brus sits in.


CONSTRAINTS
-n and m will each be between 1 and 47, inclusive.
-row will contain between 1 and 47 elements, inclusive.
-row and seat will contain the same number of elements.
-Each element of row will be between 1 and n, inclusive.
-Each element of seat will be between 1 and m, inclusive.
-All pairs (row[i], seat[i]) will be distinct.


EXAMPLES

0)
2
3
{1, 2}
{2, 3}

Returns: 1

The first and the second seat in the second row are the only two free seats next to each other in the same row.

1)
2
3
{1, 1, 1, 2, 2, 2}
{1, 2, 3, 1, 2, 3}

Returns: 0

There are no free seats in the theater.

2)
4
7
{1}
{1}

Returns: 23

3)
10
8
{1, 9, 6, 10, 6, 7, 9, 3, 9, 2}
{7, 7, 3, 3, 7, 1, 5, 1, 6, 2}

Returns: 54

*/
#endregion end cut
using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Text;
using System.Text.RegularExpressions;

public class TheMoviesLevelOneDivTwo
{
    public int find(int n, int m, int[] row, int[] seat)
    {
        int numberOfSeats = 0;

        int r = 1, i = 0;
        while (r <= n)
        {
            if (i < row.Length && row[i] == r)
            {
                while (i < row.Length && row[i] == r)
                {
                    numberOfSeats += GetAvailable((i > 0 && row[i - 1] == r ? seat[i - 1] : 1), seat[i]);
                    i++;
                }
                numberOfSeats += GetAvailable(seat[i - 1], m);
            }
            else numberOfSeats += m - 1;


            r++;
        }
        return numberOfSeats;
    }

    private int GetAvailable(int seat1, int seat2)
    {
        int available = seat2 - seat1;

        return available > 1 ? (available == 2 ? 1 : available - 1) : 0;
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new TheMoviesLevelOneDivTwo()).find(2, 3, new int[] {1, 2}, new int[] {2, 3}),1);
            eq(1,(new TheMoviesLevelOneDivTwo()).find(2, 3, new int[] {1, 1, 1, 2, 2, 2}, new int[] {1, 2, 3, 1, 2, 3}),0);
            eq(2,(new TheMoviesLevelOneDivTwo()).find(4, 7, new int[] {1}, new int[] {1}),23);
            eq(3,(new TheMoviesLevelOneDivTwo()).find(10, 8, new int[] {1, 9, 6, 10, 6, 7, 9, 3, 9, 2}, new int[] {7, 7, 3, 3, 7, 1, 5, 1, 6, 2}),54);
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

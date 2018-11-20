#region begin cut
/*
// PROBLEM STATEMENT
// Elly and some of her friends (possibly none) are going to the movies. Their company consists of numFriends people, including Elly. Since they don't want to be spread across the entire hall, they decided to sit either in the same row or in the same column (though not necessarily next to one another).

Your are given a string[] hall representing the layout of seats in the theater that are already taken. The j-th character of the i-th element of hall will be '#' if the seat at row i, column j is already taken and '.' if it is empty.

Return the number of different ways for Elly and her friends to choose numFriends different empty seats so that their seating requirement is fulfilled. Two ways are considered different if there exists a person in their company that will sit in different seats in these two ways.

DEFINITION
Class:MovieSeating
Method:getSeatings
Parameters:int, string[]
Returns:long
Method signature:long getSeatings(int numFriends, string[] hall)


CONSTRAINTS
-numFriends will be between 1 and 8, inclusive.
-hall will contain between 1 and 50 elements, inclusive.
-Each element of hall will contain between 1 and 50 characters, inclusive.
-All elements of hall will contain the same number of characters.
-Each character in hall will be either '.' or '#'.


EXAMPLES

0)
2
{ ".#..",
  ".##.",
  "...." }

Returns: 34

Here the movie hall has 3 rows and 4 columns. The second seat in the first row is taken, as well as the seats in the middle of the second row.

1)
2
{ "..#",
  ".##",
  "..." }

Returns: 16

Elly and her friend can sit in two ways in the first row, they cannot sit in the second row, and they can sit in six ways in the third row. If they choose to sit in the same column, they can do it in six ways in the leftmost column, two ways in the middle column, and not in the rightmost column because there is only one seat.

2)
5
{ "..####..", 
  ".###.##.",
  ".######.",
  "#.#.#.#." }

Returns: 0

There are enough places for the company, but since they want to sit in the same row or same column, none of the possible seatings satisfies them.

3)
8
{ "........" }

Returns: 40320

Just enough seats for all of them.

*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class MovieSeating {
    public long getSeatings(int numFriends, string[] hall) {
        long res = 0;

		int[] columns = new int[hall[0].Length];
		

		for (int i = 0; i < hall.Length; i++)
		{
			string row = hall[i];
			int emptySeatsInRow =0;
			for (int j = 0; j < row.Length; j++)
			{
				if (row[j] == '.')
				{
					emptySeatsInRow++;
					columns[j]++;

					if (i == hall.Length - 1)
						res += GetArrangements(columns[j], numFriends);
				}
			}
			if (emptySeatsInRow >= numFriends)
				res += GetArrangements(emptySeatsInRow, numFriends);
		}

		

        return res;
    }

	private static int GetArrangements(int seats, int friends)
	{
		if(friends == 1) return seats;
		return seats * GetArrangements(seats - 1, friends - 1);
	}

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new MovieSeating()).getSeatings(2, new string[] { ".#..",
                 ".##.",
                 "...." }),34L);
            eq(1,(new MovieSeating()).getSeatings(2, new string[] { "..#",
                 ".##",
                 "..." }),16L);
            eq(2,(new MovieSeating()).getSeatings(5, new string[] { "..####..", 
                 ".###.##.",
                 ".######.",
                 "#.#.#.#." }),0L);
            eq(3,(new MovieSeating()).getSeatings(8, new string[] { "........" }),40320L);
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

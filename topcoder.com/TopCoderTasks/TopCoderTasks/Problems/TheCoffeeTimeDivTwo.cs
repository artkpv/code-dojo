#region begin cut
/*
// PROBLEM STATEMENT
// John and Brus are flying on an airplane and now it's coffee time.

There are n seats in the plane numbered from 1 to n, one seat in each row. All seats are occupied, thus there are n passengers overall (including John and Brus). A stewardess will serve a cup of coffee or tea to each passenger. She needs to serve tea to all passengers whose seat numbers are listed in int[] tea, and she needs to serve coffee to all other passengers.

A coffee and tea machine is located just before the first seat of the plane. The stewardess has a flask that can contain enough coffee or tea to serve at most 7 passengers. Initially, the stewardess is located near the coffee and tea machine and the flask is empty.

The stewardess can perform the following kinds of actions:

Move from the coffee and tea machine to seat 1 or move from seat 1 to the coffee and tea machine. Each of these two actions takes 1 second.
Move from seat i, i > 1, to seat i-1. It takes 1 second.
Move from seat i, i < n, to seat i+1. It takes 1 second.
If she is near seat i, the passenger at this seat has not yet been served and the current type of drink in the flask is the same as the drink this passenger wants, she can serve this passenger with a cup of drink he/she wants. It takes 4 seconds.
If she is near the coffee and tea machine and the flask is empty, she can fill the flask with either tea or coffee (but not both simultaneously). It takes 47 seconds. Note that she can fill the flask partially (to serve less than 7 passengers), but it still takes 47 seconds.


Given int n and int[] tea, return the minimal time needed for the stewardess to serve all passengers with proper drinks and return to the coffee and tea machine.

DEFINITION
Class:TheCoffeeTimeDivTwo
Method:find
Parameters:int, int[]
Returns:int
Method signature:int find(int n, int[] tea)


CONSTRAINTS
-n will be between 2 and 1000, inclusive.
-tea will contain between 1 and 47 elements, inclusive.
-Each element of tea will be between 1 and n, inclusive.
-All elements of tea will be distinct.


EXAMPLES

0)
2
{1}

Returns: 108

The stewardess will serve coffee in 47+2+4+2=55 seconds and tea in 47+1+4+1=53 seconds.

1)
2
{2, 1}

Returns: 59

Here she only needs to serve tea.

2)
15
{1, 2, 3, 4, 5, 6, 7}

Returns: 261

The stewardess will fill the flask three times overall: once with tea and two times with coffee.

3)
47
{1, 10, 6, 2, 4}

Returns: 891

*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class TheCoffeeTimeDivTwo {
    delegate void PourOut(bool isTea);
    public int find(int n, int[] tea) {
        if (n == 0)
            return 0;
        
        Array.Sort(tea);

        int res = 47, 
            flask = 7,
            currentSeat = 0, 
            previousSeat = 0 ;

        PourOut pourOut = delegate(bool isTea)
        { 
           
            for (int i = (isTea ? tea.Length : n); i > 0 ; i--)
            {
                if (!isTea && Array.IndexOf(tea, i) != -1)
                    continue;

                if (flask == 0)
                {
                    res += currentSeat + 47;
                    flask = 7;
                    previousSeat = 0;
                }
                currentSeat = isTea ? int.Parse(tea[i - 1].ToString()) : i;
                res += Math.Abs(currentSeat - previousSeat) + 4;

                flask--;
                previousSeat = currentSeat;
            }

            if (currentSeat != 0)
            {
                flask = 0;
                res += currentSeat;
                currentSeat = 0;
                previousSeat = 0;
            }
        };

        pourOut(false);
        pourOut(true);

        return res;
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new TheCoffeeTimeDivTwo()).find(2, new int[] {1}),108);
            eq(1,(new TheCoffeeTimeDivTwo()).find(2, new int[] {2, 1}),59);
            eq(2,(new TheCoffeeTimeDivTwo()).find(15, new int[] {1, 2, 3, 4, 5, 6, 7}),261);
            eq(3,(new TheCoffeeTimeDivTwo()).find(47, new int[] {1, 10, 6, 2, 4}),891);
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

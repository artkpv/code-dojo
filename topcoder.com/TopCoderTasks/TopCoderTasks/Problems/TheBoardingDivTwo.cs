#region begin cut
/*
// PROBLEM STATEMENT
// John and Brus are going to board a plane.

The boarding can be described using the following simplified model. There are 2 * n cells numbered from 1 to 2 * n from left to right. There are n seats in the plane numbered from 1 to n. The seat i is located near cell n + i. There are n passengers numbered from 1 to n. Initially they stand
in some order in cells 1, 2, ..., n. The order can be described using a permutation p[1], p[2], ..., p[n] of integers from 1 to n, where p[i] is the number of the passenger who initially stands in cell i. It is known that passenger i wants to take seat i during boarding.

The boarding process can be divided into primitive steps, each of which takes exactly 1 second. During each step, we can check all passengers from right to left and determine for each passenger what he/she will do according to the following rules:

Denote the number of the passenger we're currently checking as X and the current cell of this passenger as Y.
If Y < n + X and cell Y + 1 is currently empty, the passenger will move to this cell. It takes him exactly one step to complete this move, so at the beginning of the next step he/she will be in cell Y + 1.
If Y < n + X, cell Y + 1 contains a passenger and the passenger at cell Y + 1 will perform a move during the current step, the passenger at cell Y will also move to the next cell during the current step (exactly as described in the previous rule).
If Y < n + X, cell Y + 1 contains a passenger and the passenger at cell Y + 1 will not move during the current step, the passenger at cell Y will skip the current step (so he/she will still be in cell Y in the beginning of the next step).
If Y = n + X, it means that the passenger in cell Y has reached the cell near which his seat is located. Therefore he will take a seat and it takes 74 steps to do it. So cell Y will be occupied during steps S, S+1, ..., S+73 (where S is the number of the current step) because the passenger at this cell will be taking his/her seat. In the beginning of step S+74 this cell will become empty because the passenger has completed taking the seat.


The boarding time is defined as the number of steps performed until each passenger has taken his/her seat. Obviously, the boarding time can depend on the initial order of passengers. For example, if p[1] = 1, p[2] = 2, the boarding time is 76 (during the first two steps both passengers reach the cells with their seats, and during the next 74 steps they simultaneously take their seats). And if p[1] = 2, p[1] = 1, the boarding time is 151 (after one step passenger 1 will reach the cell with his/her seat, during the next 74 steps he/she will take his/her seat and passenger 2 will wait until it's finished, and then passenger 2 will need 76 more steps to reach the required cell and take a seat).

You are given a int[] pattern that imposes some restrictions on the initial order of passengers (described by permutation p). This int[] contains exactly n elements. If pattern[i] (1-based) is an integer between 1 and n, inclusive, it means that p[i] must be equal to pattern[i], and if pattern[i] is -1, it means that p[i] can be an arbitrary integer between 1 and n, inclusive.

The initial order of passengers is considered to be good if the boarding time for this order is not greater than boardingTime. Return the number of good initial orders of passengers that match the given pattern.

DEFINITION
Class:TheBoardingDivTwo
Method:find
Parameters:int[], int
Returns:int
Method signature:int find(int[] pattern, int boardingTime)


CONSTRAINTS
-pattern will contain between 2 and 8 elements, inclusive.
-Each element of pattern will be either -1 or between 1 and n, inclusive, where n is the number of elements in pattern.
-For each X between 1 and n, inclusive, there will be at most one occurrence of X in pattern.
-boardingTime will be between 2 and 222, inclusive.


EXAMPLES

0)
{-1, -1}
100

Returns: 1

Here we have two possible permutations. In case of (1, 2) the boarding takes 76 seconds and in case of (2, 1) it takes 151 seconds.

1)
{-1, 2, -1}
222

Returns: 1

The only one good order is (1, 2, 3).

2)
{2, 1, 3, 5, 4, 6}
155

Returns: 1

Only one order matches pattern and the boarding for it takes exactly 155 seconds.

3)
{-1, -1, -1, -1, -1, -1, -1}
198

Returns: 233

*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class TheBoardingDivTwo {
    public int find(int[] pattern, int boardingTime) {
        int res;
        return res;
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new TheBoardingDivTwo()).find(new int[] {-1, -1}, 100),1);
            eq(1,(new TheBoardingDivTwo()).find(new int[] {-1, 2, -1}, 222),1);
            eq(2,(new TheBoardingDivTwo()).find(new int[] {2, 1, 3, 5, 4, 6}, 155),1);
            eq(3,(new TheBoardingDivTwo()).find(new int[] {-1, -1, -1, -1, -1, -1, -1}, 198),233);
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

#region begin cut
/*
// PROBLEM STATEMENT
// Gogo owns N wine cellars, numbered 0 through N-1. He possesses a time machine and will use it to advance time in one of the cellars, maturing all the wine inside. However, as a side effect, he must also choose one other cellar and turn back time there, making the wine inside younger.


You are given two int[]s, profit and decay. Advancing time in cellar i will gain Gogo a profit of profit[i]. Turning back time in cellar i will lose him decay[i] in profit. Return the maximum profit that Gogo can gain by advancing time in one cellar and turning time back in another cellar. It is guaranteed that this profit will be positive.

DEFINITION
Class:TimeTravellingCellar
Method:determineProfit
Parameters:int[], int[]
Returns:int
Method signature:int determineProfit(int[] profit, int[] decay)


CONSTRAINTS
-profit will contain between 2 and 50 elements, inclusive.
-Each element of profit will be between 1 and 10000, inclusive.
-decay will contain the same number of elements as profit.
-Each element of decay will be between 1 and 10000, inclusive.
-The maximum profit that Gogo can gain will be positive.


EXAMPLES

0)
{1,2,3}
{3,1,2}

Returns: 2

Advance time in cellar 2 and turn back time in cellar 1. The total profit is 3 - 1 = 2.

1)
{3,2}
{1,2}

Returns: 1

He can't advance and turn back time in the same cellar.

2)
{3,3,3}
{1,1,1}

Returns: 2



3)
{1000,500,250,125}
{64,32,16,8}

Returns: 992



*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class TimeTravellingCellar {
    public int determineProfit(int[] profit, int[] decay) {
        int res;

		int maxP = -1;
		int maxI = -1;
		for (int i=0; i< profit.Length; i++)
		{
			if (profit[i] > maxP)
			{
				maxP = profit[i];
				maxI = i;
			}
		}

		int minD = int.MaxValue;
		int minJ = -1;
		for (int j = 0; j < decay.Length; j++)
		{
			if (minD > decay[j] && j != maxI)
			{
				minD = decay[j];
				minJ = j;
			}
		}


        return maxP - minD;
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new TimeTravellingCellar()).determineProfit(new int[] {1,2,3}, new int[] {3,1,2}),2);
            eq(1,(new TimeTravellingCellar()).determineProfit(new int[] {3,2}, new int[] {1,2}),1);
            eq(2,(new TimeTravellingCellar()).determineProfit(new int[] {3,3,3}, new int[] {1,1,1}),2);
            eq(3,(new TimeTravellingCellar()).determineProfit(new int[] {1000,500,250,125}, new int[] {64,32,16,8}),992);
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

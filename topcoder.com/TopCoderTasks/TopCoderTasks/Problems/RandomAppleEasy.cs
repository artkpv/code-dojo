#region begin cut
/*
// PROBLEM STATEMENT
// Taro likes apples very much. He has N boxes numbered from 0 to N-1. Box i contains red[i] red apples and green[i] green apples. He decided to choose one apple from his boxes, and he does so in the following way:



First Step: He chooses a non-empty subset of his N boxes randomly and transfers all apples from those boxes to another box (this is a box other than the original N boxes and it is initially empty). Each non-empty subset of boxes has the same probability of being chosen.



Second Step: He chooses one apple from the new box randomly. Each apple in the box has the same probability of being chosen.



Return the probability that Taro chooses a red apple.



DEFINITION
Class:RandomAppleEasy
Method:theRed
Parameters:int[], int[]
Returns:double
Method signature:double theRed(int[] red, int[] green)


NOTES
-Your return value must have an absolute or relative error less than 1e-9.


CONSTRAINTS
-red will contain between 1 and 50 elements, inclusive.
-red and green will contain the same number of elements.
-Each element of red and green will be between 1 and 10, inclusive.


EXAMPLES

0)
{5}
{8}

Returns: 0.38461538461538464

There is only one box which contains 5 red apples and 8 green apples. The probability of choosing a red apple is 5 / 13.

1)
{1, 2}
{1, 1}

Returns: 0.5888888888888888

If he chooses only box 0 in the first step, the probability of choosing a red apple is 1 / 2.

If he chooses only box 1 in the first step, the probability of choosing a red apple is 2 / 3.

If he chooses both boxes in the first step, the probability of choosing a red apple is 3 / 5.


So the probability of choosing a red apple is (1 / 2 + 2 / 3 + 3 / 5) / 3 = 53 / 90.

2)
{2, 5, 6, 4, 9, 10, 6, 2}
{2, 5, 6, 4, 9, 10, 6, 2}

Returns: 0.4999999999999999



3)
{2, 5, 6, 4, 9, 10, 6, 2}
{6, 7, 4, 5, 3, 2, 9, 1}

Returns: 0.5429014970733334



4)
{5, 1, 2, 8, 4, 1, 1, 2, 3, 4, 5, 2, 10, 2, 6, 2, 8, 7, 9, 3}
{4, 7, 1, 1, 10, 3, 4, 1, 6, 2, 7, 6, 10, 5, 2, 9, 3, 8, 1, 8}

Returns: 0.46460213827476854



*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class RandomAppleEasy {
    public double theRed(int[] red, int[] green) {
        double res;
        return res;
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new RandomAppleEasy()).theRed(new int[] {5}, new int[] {8}),0.38461538461538464);
            eq(1,(new RandomAppleEasy()).theRed(new int[] {1, 2}, new int[] {1, 1}),0.5888888888888888);
            eq(2,(new RandomAppleEasy()).theRed(new int[] {2, 5, 6, 4, 9, 10, 6, 2}, new int[] {2, 5, 6, 4, 9, 10, 6, 2}),0.4999999999999999);
            eq(3,(new RandomAppleEasy()).theRed(new int[] {2, 5, 6, 4, 9, 10, 6, 2}, new int[] {6, 7, 4, 5, 3, 2, 9, 1}),0.5429014970733334);
            eq(4,(new RandomAppleEasy()).theRed(new int[] {5, 1, 2, 8, 4, 1, 1, 2, 3, 4, 5, 2, 10, 2, 6, 2, 8, 7, 9, 3}, new int[] {4, 7, 1, 1, 10, 3, 4, 1, 6, 2, 7, 6, 10, 5, 2, 9, 3, 8, 1, 8}),0.46460213827476854);
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

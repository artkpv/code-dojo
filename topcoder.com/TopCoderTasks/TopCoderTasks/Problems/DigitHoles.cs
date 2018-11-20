#region begin cut
/*
// PROBLEM STATEMENT
// Elly's evil teacher assistant Torb has given her the following puzzle: 42 -> 1, 1337 -> 0, 669 -> 3, 1882 -> 4, 688 -> 5, 12345 -> 1, 67890 -> 5, 123 -> 0, 456 -> 2, 789 -> 3. Given this information, 45678 -> ? Thanks to her fast thinking and problem-solving intuition she has found the solution: Google. The answer turned out to be the total number of "holes" in the digits of the number's decimal representation (with no extra leading zeroes). We can see that the digits 1, 2, 3, 5, and 7 contain no holes, 0, 4, 6, and 9 each has one hole, and 8 contains two holes. Therefore the answer to the puzzle is 45678 -> 1 + 0 + 1 + 0 + 2 = 4.
You want to impress Elly, so you decide to write a program that will find the correct answer for certain integers. Given an int number, return the total number of holes in that number.

DEFINITION
Class:DigitHoles
Method:numHoles
Parameters:int
Returns:int
Method signature:int numHoles(int number)


NOTES
-In some fonts, the digit '4' might not contain an enclosed hole, but for this problem you should assume it does.


CONSTRAINTS
-number will be between 1 and 1000, inclusive.


EXAMPLES

0)
42

Returns: 1

4 has one hole, and 2 has no holes.

1)
669

Returns: 3

Both sixes are counted.

2)
688

Returns: 5

Note that 8 is the only digit that has 2 holes.

3)
123

Returns: 0

A number without holes.

4)
456

Returns: 2



5)
789

Returns: 3

*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class DigitHoles {
    public int numHoles(int number) {
        int res =0;
		string numberString = number.ToString();
		for (int i = 0; i < numberString.Length; i++)
		{
			switch (numberString[i])
			{
				case '0':
				case '4':
				case '6':
				case '9':
					res++; break;
				case '8':
					res += 2; break;
					
			}
		}


        return res;
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new DigitHoles()).numHoles(42),1);
            eq(1,(new DigitHoles()).numHoles(669),3);
            eq(2,(new DigitHoles()).numHoles(688),5);
            eq(3,(new DigitHoles()).numHoles(123),0);
            eq(4,(new DigitHoles()).numHoles(456),2);
            eq(5,(new DigitHoles()).numHoles(789),3);
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

#region begin cut
/*
// PROBLEM STATEMENT
// NOTE: This problem statement contains images that may not display properly if viewed outside of the applet.


Taro shows a magic trick to Hanako.



Taro: Hello Hanako. I'll show you a magic trick. Please imagine a positive integer less than or equal to 16.
Hanako: OK. I imagined it.
Taro: (Taro shows card 1 to Hanako.) Does this card contain your number?
Hanako: Yes.
Taro: (Taro shows card 2 to Hanako.) Does this card contain your number?
Hanako: No.
Taro: (Taro shows card 3 to Hanako.) Does this card contain your number?
Hanako: Yes.
Taro: (Taro shows card 4 to Hanako.) Does this card contain your number?
Hanako: Yes.
Taro: Your number is 5!




(Card 1 contains 1, 2, 3, 4, 5, 6, 7 and 8. Card 2 contains 1, 2, 3, 4, 9, 10, 11 and 12. Card 3 contains 1, 2, 5, 6, 9, 10, 13 and 14. Card 4 contains 1, 3, 5, 7, 9, 11, 13 and 15.)


Your task is to write a program that simulates this magic trick. You are given Hanako's answers in the string answer. The i-th character is 'Y' if she answered "yes" to the i-th question, and 'N' if she answered "no" to the i-th question. Return the integer Hanako imagined.

DEFINITION
Class:NumberMagicEasy
Method:theNumber
Parameters:string
Returns:int
Method signature:int theNumber(string answer)


CONSTRAINTS
-answer will contain exactly 4 characters.
-Each character in answer will be 'Y' or 'N'.


EXAMPLES

0)
"YNYY"

Returns: 5

The example from the statement.

1)
"YNNN"

Returns: 8

8 is the only number that exists on the first card and does not exist on any other cards.

2)
"NNNN"

Returns: 16



3)
"YYYY"

Returns: 1



4)
"NYNY"

Returns: 11



*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class NumberMagicEasy {

	//(Card 1 contains 1, 2, 3, 4, 5, 6, 7 and 8. Card 2 contains 1, 2, 3, 4, 9, 10, 11 and 12. Card 3 contains 1, 2, 5, 6, 9, 10, 13 and 14. Card 4 contains 1, 3, 5, 7, 9, 11, 13 and 15.)
    public int theNumber(string answer) {
		int length = 16;
		int[] array = new int[length];
		for (int i = 0; i < length;i++) array[i] = i + 1;

		int[][] cards = new int[4][] { 
		new int[]{ 1, 2, 3, 4, 5, 6, 7, 8 }, 
		new int[]{1, 2, 3, 4, 9, 10, 11, 12}, 
		new int[]{1, 2, 5, 6, 9, 10, 13, 14}, 
		new int[]{1, 3, 5, 7, 9, 11, 13, 15}};

		for(int i=0;i<4;i++) 
			array = Array.FindAll<int>(array, 
					delegate(int j) {
						bool isFound = Array.IndexOf<int>(cards[i], j) != -1;
						return answer[i] == 'Y' ? isFound : !isFound;
					});

		return array[0];
    }

	#region begin cut
	public static void Main(String[] args)
	{
        try  {
            eq(0,(new NumberMagicEasy()).theNumber("YNYY"),5);
            eq(1,(new NumberMagicEasy()).theNumber("YNNN"),8);
            eq(2,(new NumberMagicEasy()).theNumber("NNNN"),16);
            eq(3,(new NumberMagicEasy()).theNumber("YYYY"),1);
            eq(4,(new NumberMagicEasy()).theNumber("NYNY"),11);
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

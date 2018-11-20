#region begin cut
/*
// PROBLEM STATEMENT
// Manao lives in a country where the prices of all goods are positive integers. He is setting up a company that sells microwaves, and needs to decide the best price at which to sell them. Recently, he heard of a new psychological discovery: the more trailing 9's a price has, the more attractive it is to the customer. For example, 9099 has two trailing 9's, and 8909 has only one trailing 9, so the first price is more attractive. 

Manao knows that he can only afford to sell microwaves at a price no less than minPrice, and believes that customers will only buy the microwaves if they cost no more than maxPrice. Help Manao by finding an integer between minPrice and maxPrice, inclusive, which has the maximum possible number of trailing 9's. If there are several candidates, return the largest one.


DEFINITION
Class:MicrowaveSelling
Method:mostAttractivePrice
Parameters:int, int
Returns:int
Method signature:int mostAttractivePrice(int minPrice, int maxPrice)


CONSTRAINTS
-minPrice will be between 1 and 1,000,000, inclusive.
-maxPrice will be between minPrice and 1,000,000, inclusive.


EXAMPLES

0)
460
680

Returns: 599

Of all the prices between 460 and 680, 499 and 599 have the maximum number of trailing 9's. Since 599 is larger, it is Manao's price of choice.

1)
10
1000

Returns: 999

999 has three trailing 9's, and no other number in the given range has this property.

2)
1255
2999

Returns: 2999

Note that 2999 is still an acceptable price.

3)
20
25

Returns: 25

There are no numbers with trailing 9's between 20 and 25.

*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class MicrowaveSelling {
    public int mostAttractivePrice(int minPrice, int maxPrice) {
		string maxPriceString = maxPrice.ToString();

		if(Regex.IsMatch( maxPriceString, @"9+"))
			return maxPrice;
		
		int res = 0;
		int numberOf9 =0;
		Match m;
		for (int i = maxPrice; i >= minPrice; i--)
		{
			m = Regex.Match(i.ToString(), @"(9+)");
			if (m.Success)
			{
				int newNumberOf9 = m.Groups[1].Value.Length ;
				if (newNumberOf9 > numberOf9)
				{
					res = i;
					numberOf9 = newNumberOf9;
				}
			}
		}

		return res == 0 ? maxPrice : res ;
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new MicrowaveSelling()).mostAttractivePrice(460, 680),599);
            eq(1,(new MicrowaveSelling()).mostAttractivePrice(10, 1000),999);
            eq(2,(new MicrowaveSelling()).mostAttractivePrice(1255, 2999),2999);
            eq(3,(new MicrowaveSelling()).mostAttractivePrice(20, 25),25);
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

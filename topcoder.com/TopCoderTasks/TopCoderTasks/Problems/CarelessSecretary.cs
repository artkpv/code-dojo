#region begin cut
/*
// PROBLEM STATEMENT
// The king needs to distribute instructions to all his ministers. Since each minister requires a unique set of instructions, he writes a personalized letter for each minister and hands them off to his secretary to deliver.

Unfortunately, the king's secretary is a really careless fellow. He forgets that each minister has his own personalized letter, and he delivers a random letter to each minister instead. After he realizes his mistake, he begins to call the ministers one by one and asks them if they got the correct letter. So far, he has called K of the N ministers, and to his horror, none of the K ministers has received the correct letter.

The king is furious with his secretary, but he decides to give him one last chance to save his job. He asks the secretary the following question. In how many ways was it possible for him to distribute the letters so that the current situation would arise? In other words, how many different ways could the letters have been distributed such that a wrong letter went to each of the K ministers that has been called so far? Two ways are considered different if at least one minister gets a different letter. If the secretary can answer this question correctly, he can keep his job. Your job is to help the secretary by calculating the correct answer for him. Since the answer can be very large, return the answer modulo 1,000,000,007.


DEFINITION
Class:CarelessSecretary
Method:howMany
Parameters:int, int
Returns:int
Method signature:int howMany(int N, int K)


CONSTRAINTS
-N will be between 1 and 1000, inclusive.
-K will be between 1 and N, inclusive.
-K will be between 1 and 12, inclusive.


EXAMPLES

0)
2
1

Returns: 1

There are two ministers, and one of them must not get his own letter. Therefore, the only possibility is that they get each other's letters.

1)
3
1

Returns: 4

The minister who must not get his own letter might get any of the two remaining letters. For each possibility, there are 2 ways to give the letters to the other ministers. Hence, the answer is 2*2 = 4. 


2)
3
3

Returns: 2

Three ministers, and none of them get their own letters. 

3)
7
4

Returns: 2790

4)
9
1

Returns: 322560



5)
714
9

Returns: 466134693

*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class CarelessSecretary {
    public int howMany(int N, int K) {
        int res;
        return res;
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new CarelessSecretary()).howMany(2, 1),1);
            eq(1,(new CarelessSecretary()).howMany(3, 1),4);
            eq(2,(new CarelessSecretary()).howMany(3, 3),2);
            eq(3,(new CarelessSecretary()).howMany(7, 4),2790);
            eq(4,(new CarelessSecretary()).howMany(9, 1),322560);
            eq(5,(new CarelessSecretary()).howMany(714, 9),466134693);
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

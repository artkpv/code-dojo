#region begin cut
/*
// PROBLEM STATEMENT
// Taro has prepared delicious kiwi fruit juice. He poured it into N bottles numbered from 0 to N-1. The capacity of the i-th bottle is capacities[i] liters, and he poured bottles[i] liters of kiwi juice into this bottle.


Now he wants to redistribute juice in the bottles. In order to do this, he will perform M operations numbered from 0 to M-1 in the order in which he will perform them. For the i-th operation, he will pour kiwi juice from bottle fromId[i] to bottle toId[i]. He will stop pouring when bottle fromId[i] becomes empty or bottle toId[i] becomes full, whichever happens earlier.


Return an int[] that contains exactly N elements and whose i-th element is the amount of kiwi juice in the i-th bottle after all pouring operations are finished.



DEFINITION
Class:KiwiJuiceEasy
Method:thePouring
Parameters:int[], int[], int[], int[]
Returns:int[]
Method signature:int[] thePouring(int[] capacities, int[] bottles, int[] fromId, int[] toId)


CONSTRAINTS
-capacities will contain between 2 and 50 elements, inclusive.
-Each element of capacities will be between 1 and 1,000,000, inclusive.
-capacities and bottles will contain the same number of elements.
-For each i, bottles[i] will be between 0 and capacities[i], inclusive.
-fromId will contain between 1 and 50 elements, inclusive.
-fromId and toId will contain the same number of elements.
-Each element of fromId and toId will be between 0 and N-1, inclusive, where N is the number of elements in capacities.
-For each i, fromId[i] and toId[i] will be distinct.


EXAMPLES

0)
{20, 20}
{5, 8}
{0}
{1}

Returns: {0, 13 }

He pours kiwi juice from bottle 0 to bottle 1. After pouring, bottle 0 will become empty and bottle 1 will contain 13 liters of kiwi juice.

1)
{10, 10}
{5, 8}
{0}
{1}

Returns: {3, 10 }

He will stop pouring when bottle 1 becomes full.

2)
{30, 20, 10}
{10, 5, 5}
{0, 1, 2}
{1, 2, 0}

Returns: {10, 10, 0 }



3)
{14, 35, 86, 58, 25, 62}
{6, 34, 27, 38, 9, 60}
{1, 2, 4, 5, 3, 3, 1, 0}
{0, 1, 2, 4, 2, 5, 3, 1}

Returns: {0, 14, 65, 35, 25, 35 }



4)
{700000, 800000, 900000, 1000000}
{478478, 478478, 478478, 478478}
{2, 3, 2, 0, 1}
{0, 1, 1, 3, 2}

Returns: {0, 156956, 900000, 856956 }



*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class KiwiJuiceEasy {
    public int[] thePouring(int[] capacities, int[] bottles, int[] fromId, int[] toId) {
        
        for (int i = 0; i < fromId.Length; i++)
        {
            int from = fromId[i], to = toId[i];

            int pouring = bottles[from];
            int freeSpace = capacities[to] - bottles[to];
            int poured = pouring > freeSpace ? freeSpace : pouring;

            bottles[from] = bottles[from] - poured;
            bottles[to] += poured;
        }
        return bottles;
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new KiwiJuiceEasy()).thePouring(new int[] {20, 20}, new int[] {5, 8}, new int[] {0}, new int[] {1}),new int[] {0, 13 });
            eq(1,(new KiwiJuiceEasy()).thePouring(new int[] {10, 10}, new int[] {5, 8}, new int[] {0}, new int[] {1}),new int[] {3, 10 });
            eq(2,(new KiwiJuiceEasy()).thePouring(new int[] {30, 20, 10}, new int[] {10, 5, 5}, new int[] {0, 1, 2}, new int[] {1, 2, 0}),new int[] {10, 10, 0 });
            eq(3,(new KiwiJuiceEasy()).thePouring(new int[] {14, 35, 86, 58, 25, 62}, new int[] {6, 34, 27, 38, 9, 60}, new int[] {1, 2, 4, 5, 3, 3, 1, 0}, new int[] {0, 1, 2, 4, 2, 5, 3, 1}),new int[] {0, 14, 65, 35, 25, 35 });
            eq(4,(new KiwiJuiceEasy()).thePouring(new int[] {700000, 800000, 900000, 1000000}, new int[] {478478, 478478, 478478, 478478}, new int[] {2, 3, 2, 0, 1}, new int[] {0, 1, 1, 3, 2}),new int[] {0, 156956, 900000, 856956 });
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

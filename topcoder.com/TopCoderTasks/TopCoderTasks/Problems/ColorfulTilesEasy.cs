#region begin cut
/*
// PROBLEM STATEMENT
// Taro likes colorful things, especially colorful tiles.


Taro's room is divided into L square tiles arranged in a row. Each tile is one of the following four colors: red, green, blue or yellow. You are given a string room. If the i-th character of room is 'R', 'G', 'B' or 'Y', the color of the i-th tile is red, green, blue or yellow, respectively.


He decided to change the color of some tiles so that no two adjacent tiles have the same color. Return the minimal number of tiles he must change.

DEFINITION
Class:ColorfulTilesEasy
Method:theMin
Parameters:string
Returns:int
Method signature:int theMin(string room)


CONSTRAINTS
-room will contain between 1 and 10 characters, inclusive.
-Each character in room will be 'R', 'G', 'B' or 'Y'.


EXAMPLES

0)
"RRRRRR"

Returns: 3

For example, he can change three tiles in the following way:
"RRRRRR" -> "RGRGRG".

1)
"GGGGGGG"

Returns: 3

For example, "GGGGGGG" -> "GRGRGRG".

2)
"BBBYYYYYY"

Returns: 4

For example, "BBBYYYYYY" -> "BRBYRYRYR".

3)
"BRYGYBGRYR"

Returns: 0

The condition is already satisfied, so he doesn't need to change any tiles.

4)
"RGGBBBRYYB"

Returns: 3



*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class ColorfulTilesEasy {
    public int theMin(string room) {
        int res = 0;
        Char[] array = room.ToCharArray();

        for (int i = 1; i < array.Length; i++)
        {
            if (array[i - 1] == array[i])
            {
                array[i] = Array.Find<Char>("RGBY".ToCharArray(), delegate(char c) { return c != array[i - 1] && (i + 1 >= array.Length || c != array[i + 1]); });
                res++;
            }
        }

        return res;
    }

    private bool IsSatisfies(string room)
    {
        for (int i = 1; i < room.Length - 1; i++)
        {
            if (room[i - 1] == room[i] || room[i + 1] == room[i])
                return false;
        }
        return true;
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new ColorfulTilesEasy()).theMin("RRRRRR"),3);
            eq(1,(new ColorfulTilesEasy()).theMin("GGGGGGG"),3);
            eq(2,(new ColorfulTilesEasy()).theMin("BBBYYYYYY"),4);
            eq(3,(new ColorfulTilesEasy()).theMin("BRYGYBGRYR"),0);
            eq(4,(new ColorfulTilesEasy()).theMin("RGGBBBRYYB"),3);
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

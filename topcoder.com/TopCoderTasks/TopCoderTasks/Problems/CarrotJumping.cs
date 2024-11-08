#region begin cut
/*
// PROBLEM STATEMENT
// Rabbits often feel hungry, so when they go out to eat carrots, they jump as quickly as possible.


Initially, rabbit Hanako stands at position init. From position x, she can jump to either position 4*x+3 or 8*x+7 in a single jump. She can jump at most 100,000 times because she gets tired by jumping.


Carrots are planted at position x if and only if x is divisible by 1,000,000,007 (i.e. carrots are planted at position 0, position 1,000,000,007, position 2,000,000,014, and so on). Return the minimal number of jumps required to reach a carrot. If it's impossible to reach a carrot using at most 100,000 jumps, return -1.



DEFINITION
Class:CarrotJumping
Method:theJump
Parameters:int
Returns:int
Method signature:int theJump(int init)


CONSTRAINTS
-init will be between 1 and 1,000,000,006, inclusive.


EXAMPLES

0)
125000000

Returns: 1

She can jump from 125000000 to 1000000007.

1)
281250001

Returns: 2

281250001 -> 1125000007 -> 9000000063

2)
18426114

Returns: 58



3)
4530664

Returns: 478



4)
705616876

Returns: 100000

5)
852808441

Returns: -1

She can't reach any carrot by making at most 100,000 jumps.

*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;

public class CarrotJumping {
    const int bingo = 1000000007;
    const int N = 100000;
    public int theJump(int init) {

        int ans = N + 1;
        long near, far = init;
        for (int i = 0; i < 3; i++)
        {
            near = far;
            for (int j = 0; j <= N - i; j++)
            {
                if (near == 0) 
                    ans = Math.Min(ans, j + i);

                near = (8 * near + 7) % bingo;
            }

            far = (4 * far + 3) % bingo;
        }

        return ans == N + 1 ? -1 : ans;
    }


    //wrong: too resource heavy
    private int GetJumps(uint init)
    {
        if (init == bingo)
            return 0;

        init = init % bingo;
        Dictionary<uint, object> hash = new Dictionary<uint, object>();
        hash.Add(init, null);
        List<uint> jumps = new List<uint>();
        jumps.Add(init);


        uint near, far, current;
        int scipped;
        for (int i = 1; i <= 100000; i++)
        {
            scipped = 0;
            for (int j = jumps.Count - 1; j >= 0; j--)
            {
                current = jumps[j];
                if (current == int.MaxValue)
                {
                    continue;
                    scipped++;
                }

                near = (4 * current + 3) % bingo;
                if (near == 0)
                    return i;

                far = (8 * current + 7) % bingo;
                if (far == 0)
                    return i;

                if (hash.ContainsKey(near))
                    jumps[j] = int.MaxValue;
                //jumps.Remove(near);
                else
                {
                    jumps[j] = near;
                    hash.Add(near, null);
                }


                if (!hash.ContainsKey(far))
                {
                    jumps.Add(far);
                    hash.Add(far, null);
                }
            }

            if (jumps.Count == scipped)
                break;
        }

        return -1;
    }

    //wrong: too resource heavy
    private int GetJumpsIter(int init)
    {
        if (init == bingo)
            return 0;
        const int numberOfJumps = 100000;
        int[] jumps = new int[(int)Math.Pow(2, numberOfJumps)];
        jumps[0] = 4 * init + 3;
        jumps[1] = 8 * init + 7;

        int middle;
        int numberOfPaths;
        int parent;
        bool isAllOverJumped = false;
        for (int i = 2; i <= numberOfJumps || isAllOverJumped; i++)
        {
            numberOfPaths = (int)Math.Pow(2, i);
            middle = numberOfPaths / 2;
            isAllOverJumped = true;

            for (int j = 0; j < numberOfPaths; j++)
            {
                if (jumps[j] > bingo)
                {
                    jumps[j] = int.MaxValue;
                    isAllOverJumped = isAllOverJumped & true;
                    continue;
                }
                else if (jumps[j] == bingo)
                    return i - 1;
                else
                    isAllOverJumped = false;


                if (j + 1 <= middle)
                    jumps[j] = 4 * jumps[j] + 3;
                else
                {
                    parent = jumps[j - middle];
                    if (parent != int.MaxValue) jumps[j] = 8 * parent + 7;
                }
            }
        }

        return -1;
    }

    //wrong: too resource heavy
    private int GetJumps(int x, int jumpsNumber)
    {
        if (x == bingo)
            return jumpsNumber;
        else if(x > bingo)
            return int.MaxValue;

        int near = GetJumps(4 * x + 3, jumpsNumber + 1), 
            far = GetJumps(8 * x + 7, jumpsNumber + 1);

        if (near < far)
            return near;
        else
           return far;            
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new CarrotJumping()).theJump(125000000),1);
            eq(1,(new CarrotJumping()).theJump(281250001),2);
            eq(2,(new CarrotJumping()).theJump(18426114),58);
            eq(3,(new CarrotJumping()).theJump(4530664),478);
            eq(4,(new CarrotJumping()).theJump(705616876),100000);
            eq(5,(new CarrotJumping()).theJump(852808441),-1);
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

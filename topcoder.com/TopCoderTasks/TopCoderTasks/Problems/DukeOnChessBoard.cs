#region begin cut
/*
// PROBLEM STATEMENT
// Let's define a duke as a chess figure that is only allowed to move 1 cell up, down, left or right.

A duke is placed on an n?n board in the cell initPosition. In this problem, columns are marked 'a', 'b', etc. from left to right, and rows are marked '1', '2', etc. from bottom to top.  Cells are notated as "cr" (quotes for clarity), where c is the column and r is the row.

Let's describe a duke's path as a dash-separated list of cells visited by the duke. For example, "c5-b5-b4" is a path consisting of two moves. The first move is one cell to the left (from c5 to b5), and the second is one cell down (from b5 to b4).

A path is called simple if it contains no repeated cells.



Return the lexicographically greatest simple path of a duke starting in initPosition. If the length of the path exceeds 40 characters, return only the first 20 and the last 20 characters, separated by three dots. (See Example #1).


DEFINITION
Class:DukeOnChessBoard
Method:dukePath
Parameters:int, string
Returns:string
Method signature:string dukePath(int n, string initPosition)


NOTES
-A string A is greater than a string B lexicographically if B is a proper prefix of A, or if A has a greater character at the first position where the strings differ.


CONSTRAINTS
-n will be between 2 and 8, inclusive.
-initPosition will contain exactly 2 characters.
-The first character of initPosition will be a lowercase letter between 'a' and 'h', inclusive.
-The second character of initPosition will be a digit between '1' and '8', inclusive.
-initPosition will denote a cell inside the n?n board.


EXAMPLES

0)
3
"b2"

Returns: "b2-c2-c3-b3-a3-a2-a1-b1-c1"

After the first move to the right, the duke will traverse the perimeter of the board in the counterclockwise direction.

1)
4
"d4"

Returns: "d4-d3-d2-d1-c1-c2-c3...b3-b2-b1-a1-a2-a3-a4"

The duke will move down three times, then left, then up three times and left, in a snake-like fashion.
The lexicographically greatest path is 47 characters long, so its middle part is replaced by "...".

2)
3
"a2"

Returns: "a2-b2-c2-c3-b3-a3"



3)
4
"d3"

Returns: "d3-d4-c4-c3-c2-d2-d1...b2-b3-b4-a4-a3-a2-a1"



4)
8
"a8"

Returns: "a8-b8-c8-d8-e8-f8-g8...a1-a2-a3-a4-a5-a6-a7"



*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
public class DukeOnChessBoard {
    private struct Point
    {
        public int X, Y;
        public override bool Equals(object o)
        {
            if (o is Point)
                return ((Point)o).X == X && ((Point)o).Y == Y;
            else return base.Equals(o);
        }
        public override int GetHashcode() { return X ^ Y; }

        public Point(int x, int y) { X = x; Y = y; }
    }

    public string dukePath(int n, string initPosition)
    {
        string res;



        return res;
    }

    private int CountMoves(List<Point> moves, int n)
    { 
        //can i move?
        Point last = moves[moves.Length-1];
        
        int x1, x2, y1, y2;
        Point p1 = new Point(last.X + 1, last.Y),
                p2 = new Point(last.X + 1, last.Y),
             p3 = new Point(last.X + 1, last.Y),
            p4 = new Point(last.X + 1, last.Y);

        if (last.X + 1 <= n && !moves.Contains(p1))
            x1 = CountMoves(new List<Point>(moves.Add(p1)));

            
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new DukeOnChessBoard()).dukePath(3, "b2"),"b2-c2-c3-b3-a3-a2-a1-b1-c1");
            eq(1,(new DukeOnChessBoard()).dukePath(4, "d4"),"d4-d3-d2-d1-c1-c2-c3...b3-b2-b1-a1-a2-a3-a4");
            eq(2,(new DukeOnChessBoard()).dukePath(3, "a2"),"a2-b2-c2-c3-b3-a3");
            eq(3,(new DukeOnChessBoard()).dukePath(4, "d3"),"d3-d4-c4-c3-c2-d2-d1...b2-b3-b4-a4-a3-a2-a1");
            eq(4,(new DukeOnChessBoard()).dukePath(8, "a8"),"a8-b8-c8-d8-e8-f8-g8...a1-a2-a3-a4-a5-a6-a7");
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

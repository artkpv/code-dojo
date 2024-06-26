#region begin cut
/*
// PROBLEM STATEMENT
// A pharmacist is making a mixture of several ingredients. She needs to know the density of the resulting mixture. Density is defined as the mass of the mixture divided by its volume.

You're given a string[] ingredients, each element of which describes a single ingredient and is formatted "<Volume> ml of <Name>, weighing <Mass> g" (quotes for clarity). <Volume> and <Mass> are integers representing the volume in milliliters and mass in grams, respectively.  <Name> is the name of the ingredient.

Return the density of the resulting mixture in grams per milliliters.

DEFINITION
Class:MixtureDensity
Method:getDensity
Parameters:string[]
Returns:double
Method signature:double getDensity(string[] ingredients)


NOTES
-The returned value must be accurate to within a relative or absolute value of 1E-9.


CONSTRAINTS
-ingredients will contain between 1 and 50 elements, inclusive.
-Each element of ingredients will contain between 23 and 50 characters, inclusive.
-Each element of ingredients will be formatted as described in the statement.
-Each <Volume> in ingredients will be an integer between 1 and 1000, inclusive, with no leading zeroes.
-Each <Mass> in ingredients will be an integer between 1 and 1000, inclusive, with no leading zeroes.
-Each <Name> in ingredients will contain only lowercase letters ('a'-'z') and spaces (' ').
-Each <Name> in ingredients will begin and end with a lowercase letter.


EXAMPLES

0)
{"200 ml of oil, weighing 180 g"}

Returns: 0.9

The density is mass/volume = 180g/200ml = 0.9g/ml, the answer is 0.9.

1)
{"100 ml of dichloromethane, weighing 130 g", "100 ml of sea water, weighing 103 g"}

Returns: 1.165

The volume of the resulting mixture is 200 ml and the mass is 233 g. Therefore, the density is 233g/200ml = 1.165g/ml.

2)
{"1000 ml of water, weighing 1000 g", "500 ml of orange juice concentrate, weighing 566 g"}

Returns: 1.044



3)
{"1000 ml of something   l i g h t, weighing 1 g"}

Returns: 0.0010



*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;

public class MixtureDensity {
    public double getDensity(string[] ingredients) {
        double res = 0;
        Regex r = new Regex(@"(\d+) ml of ([\w ]+), weighing (\d+) g");
        int mass = 0, volume = 0;
        foreach (string str in ingredients)
        {
            Match m = r.Match(str);
            volume += int.Parse(m.Groups[1].Value);
            mass += int.Parse(m.Groups[3].Value);
        }
        if (volume != 0)
            res = (double)mass / (double)volume;
        return res;
    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new MixtureDensity()).getDensity(new string[] {"200 ml of oil, weighing 180 g"}),0.9);
            eq(1,(new MixtureDensity()).getDensity(new string[] {"100 ml of dichloromethane, weighing 130 g", "100 ml of sea water, weighing 103 g"}),1.165);
            eq(2,(new MixtureDensity()).getDensity(new string[] {"1000 ml of water, weighing 1000 g", "500 ml of orange juice concentrate, weighing 566 g"}),1.044);
            eq(3,(new MixtureDensity()).getDensity(new string[] {"1000 ml of something   l i g h t, weighing 1 g"}),0.0010);
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

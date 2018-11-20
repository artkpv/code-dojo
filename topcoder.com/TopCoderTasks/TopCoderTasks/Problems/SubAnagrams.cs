#region begin cut
/*
// PROBLEM STATEMENT
// A string X is an anagram of string Y if X can be obtained by arranging all characters of Y in some order, without removing any characters and without adding new characters. For example, each of the strings "baba", "abab", "aabb" and "abba" is an anagram of "aabb", and strings "aaab", "aab" and "aabc" are not anagrams of "aabb".

A string X is a subsequence of string Y if X can be obtained by removing some characters (possibly none) from Y and preserving the order of the remaining characters. For example, each of the strings "ac", "abd", "abcd" is a subsequence of "abcd", and strings "ca", "abb" and "abcde" are not subsequences of "abcd".

A string X is called a subanagram of Y if there exists a string Z such that X is an anagram of Z and Z is a subsequence of Y.

Manao is a big fan of subanagrams and he tries to find them everywhere. This time, he works on splitting strings into several parts in such a way that each of the parts (except the last one) is a subanagram of the following part. Formally, for a given string X, Manao wants to split it into several non-empty strings S1, S2, ..., Sn such that their concatenation S1 + S2 + ... + Sn equals X and each string Si (0 &lt i &lt n) is a subanagram of string Si+1.

You're given a string[] suppliedWord. Concatenate all its elements in the order they are given to obtain a single string X. Return the maximum number of parts into which Manao can split X so that the condition from the previous paragraph is satisfied.

DEFINITION
Class:SubAnagrams
Method:maximumParts
Parameters:string[]
Returns:int
Method signature:int maximumParts(string[] suppliedWord)


CONSTRAINTS
-suppliedWord will contain between 1 and 10 elements, inclusive.
-Each element of suppliedWord will contain between 1 and 50 characters, inclusive.
-suppliedWord will consist of uppercase letters ('A'-'Z') only.


EXAMPLES

0)
{"ABABAB"}

Returns: 3

Manao can split the given string in three "AB"-s.

1)
{"A A XA AAABX"}

Returns: 4

One of the possible ways to split "AAXAAAABX" into 4 parts is "A"+"A"+"XA"+"AAABX". "XA" is the anagram of "AX", a subsequence of "AAABX".

2)
{"ABCDEFGHIJKL"}

Returns: 1

This word is not splittable.

3)
{"ABBAB","B","BBX","Z"}

Returns: 2

Don't forget to concatenate the given strings.

*/
#endregion end cut
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;

public class SubAnagrams {

    //TOO LONG!!!!
    public int maximumParts(string[] suppliedWord) {
        int res = 0;

        string concat = String.Concat(suppliedWord);

        List<int> devs = new List<int>();
        List<string> cut = new List<string>();
        for (int i = 0; i < Math.Pow(2, concat.Length - 1); i++)
        {
            devs.Clear();
            for (int j = 0; j < concat.Length - 1; j++)
            {
                if (((i >> j) & 1) == 1) devs.Add(j);
            }

            cut.Clear();
            bool isAllSub = true;
            cut.Add(concat.Substring(0, devs.Count == 0 ? concat.Length : devs[0] + 1));
            for (int j = 0; j < devs.Count; j++)
            {
                int index = devs[j] + 1;
                int length =  (j + 1 == devs.Count ? concat.Length - 1: devs[j + 1]) - devs[j];

                cut.Add(concat.Substring(index, length));

                if (!IsSubanagram(cut[j], cut[j + 1]))
                {
                    isAllSub = false;
                    break;
                }
            }


            if (isAllSub && res < cut.Count)
                res = cut.Count;
        }

        return res;
    }

    private bool IsSubanagram(string a, string b)
    {

        Dictionary<Char, int> aChars = new Dictionary<char, int>();
        for (int i = 0; i < a.Length; i++)
        {
            char ai = a[i];
            if (aChars.ContainsKey(ai))
                aChars[ai]++;
            else
                aChars.Add(ai, 1);
        }

        foreach (Char c in aChars.Keys)
        {
            if (Regex.Matches(b, c.ToString()).Count < aChars[c])
                return false;
        }
        return true;


    }

#region begin cut
    public static void Main(String[] args) {
        try  {
            eq(0,(new SubAnagrams()).maximumParts(new string[] {"ABABAB"}),3);
            eq(1,(new SubAnagrams()).maximumParts(new string[] {"AAXAAAABX"}),4);
            eq(2,(new SubAnagrams()).maximumParts(new string[] {"ABCDEFGHIJKL"}),1);
            eq(3,(new SubAnagrams()).maximumParts(new string[] {"ABBAB","B","BBX","Z"}),2);
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

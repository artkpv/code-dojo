using System;
using System.Diagnostics;
using System.Linq;

public static class Program
{
    public static int Search(string p, string t) {
        Func<int, char, int> prefixFunc = ComputePrefixFunc(p);
        int state = 0;
        for (int i = 0; i < t.Length; i++)
        {
            char c = t[i];
            state = prefixFunc(state, c);
            if (state == p.Length)
                return i-p.Length+1;
        }
        return -1;
    }

    private static Func<int, char, int> ComputePrefixFunc(string p)
    {
        char[] alphabeth = p.Distinct().OrderBy(c=>c).ToArray();
        int[,] func = new int[alphabeth.Length, p.Length + 1];

        for (int i = 0; i < p.Length+1; i++)
        {
            for (int j = 0; j < alphabeth.Length; j++)
            {
                char c = alphabeth[j];
                // find longest suffix of p[:i]c that is prefix of p:
                int k = Math.Min(i+1, p.Length); // length of the longest suffix/prefix
                while (k > 0)
                {
                    var p_k = p.Skip(i-k+1).Take(k-1).Append(c);
                    // check p_k is suffix of p:
                    int ii = 0;
                    foreach (var p_k_c in p_k) {
                        if (p[ii] != p_k_c) {
                            break;
                        }
                        ii++;
                    }
                    if (ii == k) // found
                        break;
                    k--;
                }
                func[j,i] = k;
            }
        }
        var char_to_inx = alphabeth.Select((c,i)=>new {c,i}).ToDictionary(i=>i.c,i=>i.i);
        return (int state, char c ) =>
            char_to_inx.ContainsKey(c) ? func[char_to_inx[c], state] : 0;
    }

    public static int Main() {
        Debug.Assert(Search("A", "BBA") == 2);
        Debug.Assert(Search("B", "AAA") == -1);
        Debug.Assert(Search("ABABACA", "AAAABBBDCAABABABACAA") == 12);
        Debug.Assert(Search("AAAB", "AABAABAABAABAAAB") == 12);
        Debug.Assert(Search("exam", "some more sophisticated example") == 24);
        Console.WriteLine("Done");
        return 1;
    }
}

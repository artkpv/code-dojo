using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;


public class DijkstraSP
{
    int[][] Adj = new [] {
        new [] {1, 2, 3},
        new [] {2},
        new [] {3},
        new [] {0}
    };

    const int INF = (int)1e9+7;

    int[] DistTo = {INF, INF, INF, INF};

    int[][] Weights = new [] {
        new [] {INF, 1, 1, 1},
        new [] {INF, INF, 1, INF},
        new [] {INF, INF, INF, 1},
        new [] {1, INF, INF, INF}
    };

    public void SP(int source)
    {
        var pq = new SortedDictionary<int, int>(); // Red-Black tree.
        pq.Add(source, 0);
        DistTo[source] = 0;
        while (pq.Any())
        {
            int v = pq.First().Key;
            pq.Remove(v);
            foreach (int w in Adj[v])
            {
                if (DistTo[w] > DistTo[v] + Weights[v][w])
                {
                    // Relax.
                    DistTo[w] = DistTo[v] + Weights[v][w];
                    if (pq.ContainsKey(w))
                        pq[w] = DistTo[w];
                    else
                        pq.Add(w, DistTo[w]);
                }
            }
        }
    }

    public static int Main()
    {
        var dsp = new DijkstraSP();
        dsp.SP(0);
        Console.WriteLine(string.Join(" ", dsp.DistTo));
        return 0;
    }

}

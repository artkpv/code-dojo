using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using System.IO;

public class Node {
    public Node Next;
    public int Height;
    public int Count;
}

public static class A {
    public static void Main() {
        var sr = File.OpenText("input.txt");
        int n = int.Parse(sr.ReadLine().Trim());
        int[] a = sr.ReadLine().Trim().Split(' ').Select(int.Parse).ToArray();
        Node first = null;
        int count = 0;
        foreach (var e in a)
        {
            if (e > 0) {
                if (first != null && first.Height == 1) 
                    first.Count++;
                else {
                    first = new Node {Height = 1, Count = 1, Next = first};
                    count++;
                }
            }
            else {
                if (first == null){
                    first = new Node {Height = 1, Count = 1};
                    count++;
                }
                else {
                    int h = first.Height + 1;
                    if (first.Next == null) {
                        if (first.Count == 1) {
                            first.Height = h;
                        }
                        else {
                            first.Count--;
                            first.Next = new Node {Height = h, Count = 1};
                            count++;
                        }
                    }
                    else {
                        if (first.Count == 1) {
                            first.Height = h;
                            if (first.Height == first.Next.Height){
                                first.Next.Count++;
                                first = first.Next;
                                count--;
                            }
                        }
                        else {
                            first.Count--;
                            if (first.Next.Height == h) {
                                first.Next.Count++;
                            }
                            else {
                                first.Next = new Node {Height = h, Count = 1, Next = first.Next};
                                count++;
                            }
                        }
                    }
                }
            }
        }
        var tw = new StreamWriter("output.txt", append: false);
        tw.WriteLine(count);
        var nn = first;
        while (nn != null) {
            tw.Write(string.Format("{0} {1}\n", nn.Height, nn.Count));
            nn = nn.Next;
        }
        tw.Flush();
    }
}
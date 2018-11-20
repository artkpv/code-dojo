using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {

    static string acidNaming(string acid_name) {
        if(acid_name.EndsWith("ic")) 
          if(acid_name.StartsWith("hydro"))
            return "non-metal acid";
          else
            return "polyatomic acid";
        return "not an acid";
    }

    static void Main(String[] args) {
        int n = Convert.ToInt32(Console.ReadLine());
        for(int a0 = 0; a0 < n; a0++){
            string acid_name = Console.ReadLine();
            string result = acidNaming(acid_name);
            Console.WriteLine(result);
        }
    }
}

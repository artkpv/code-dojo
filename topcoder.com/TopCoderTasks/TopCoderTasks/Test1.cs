using System;
using System.Collections.Generic;
using System.Text;

namespace TopCoderTasks
{
    class Test1
    {
        public readonly string Value;
        public static string Check= "check";

        static Test1() 
        { 
            Test1 t = new Test1("aa");
            
            throw new Exception();
        }
        
        public Test1(string t) { 
            Value = t;
            Console.Write("yahoo");
        }

       

        public static void M(object A) { }
        public static void M(short B) { }

    }

    class B
    {
        public static void Main()
        {
            //try
            //{
            //    Test1 t = new Test1("aa");
            //}
            //catch { }

            //Console.Write(Test1.Check);

            string str = "abcd";
            string str2 = str;//.ToLower();

            Console.WriteLine(M1(str, str2));
            Console.WriteLine(M2(str, str2));
            Console.Read();

        }

        public static bool M1(object o1, object o2)
        {
            return o1 == o2;
        }

        public static bool M2(object o1, object o2)
        {
            return o1.Equals(o2);
        }
    }
}

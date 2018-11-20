using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Text;
using System.Text.RegularExpressions;
using System.Diagnostics;

namespace TopCoderTasks
{
    public class Prerequisites : IComparer<Prerequisites.C>
    {
        Dictionary<string, bool> _Prerequisites = new Dictionary<string, bool>();
        bool _IsValid = true;

        private void CheckPrerequisites(C c)
        {
            if (_Prerequisites.ContainsKey(c.Name))
                _Prerequisites[c.Name] = true;

            foreach (string prerequisites in c.Prerequisites)
                if (!_Prerequisites.ContainsKey(prerequisites))
                    _Prerequisites.Add(prerequisites, false);
        }

        public int Compare(C c1, C c2)
        {
            CheckPrerequisites(c1);
            CheckPrerequisites(c2);            

            if (c1.Prerequisites.Contains(c2.Name) && c2.Prerequisites.Contains(c1.Name))
                _IsValid = false;

            return c1.CompareTo(c2);
        }

        public string[] orderClasses(string[] param0)
        {
            SortedList<C, string> classes = new SortedList<C, string>(this);

            foreach (string param in param0)
            {
                C c = new C(param);
                classes.Add(new C(param), c.Name);
            }

            _IsValid = !_Prerequisites.ContainsValue(false);

            if (classes.Count == 1 && classes.Keys[0].Prerequisites.Count != 0)
                _IsValid = false;
                        
            if (!_IsValid)
                return new string[] { };
            else
                return (new List<string>(classes.Values)).ToArray();
        }

        public class C : IComparable<C>
        {
            public int CompareTo(C other)
            {
                if(other.name == name)
                    throw new  Exception(string.Format("Invalid comparing: names equal - {0}", name));
                if (other.prerequisites.Contains(name))
                    return -1;
                if(prerequisites.Contains(other.Name))
                    return 1;
                if (other.number > number)
                    return -1;
                if (other.number < number)
                    return 1;

                return name.CompareTo(other.Name);
            }

            List<string> prerequisites = new List<string>();
            string name;
            int number;
            public string Name { get { return name; } }
            public List<string> Prerequisites { get { return prerequisites; } }
            public C(string str)
            {
                name = str.Substring(0, str.IndexOf(':'));
                number = int.Parse(Regex.Match(str, @"\d+").Value);
                foreach (string prerequisite in str.Split(' '))
                {
                    if (prerequisite[prerequisite.Length - 1] == ':')
                        continue;
                    prerequisites.Add(prerequisite);
                }
            }
        }



        // Regex _r = new Regex(@"(?<name>\w{1,4})(?<number>\d)");
        //public string[] orderClasses(string[] param0)
        //{
        //    SortedList<C, string> classes = new SortedList<C, string>();
            

        //    for (int i = 0; i < param0.Length; i++)
        //    {
        //        C c = new C(param0[i]);
        //        classes.Add(c, c.Name);
        //    }

        //    bool isValid = true;
        //    for (int i = 0; i < classes.Count; i++)
        //    {
        //        C checkingC = classes.Keys[i];
        //        for (int j = 0; j < classes.Count; j++)
        //        {
        //            if (i == j)
        //                continue;

        //            C c = classes.Keys[j];
        //            if (checkingC.Prerequisites.Contains(c.Name) && c.Prerequisites.Contains(checkingC.Name))
        //                isValid = false;

                    
        //        }
        //    }

        //    return (new List<string>(classes.Values)).ToArray();
        //}




        public static void Test()
        {
            string[] desiredAnswer;
            string[] str = new string[] { "CSE121: CSE110", "CSE110:", "MATH122:" };
            desiredAnswer = new string[] { "CSE110", "CSE121", "MATH122" };
            TestString(desiredAnswer, str);

            str = new string[] { 
"ENGL111: ENGL110",
"ENGL110: ENGL111"
 };
            desiredAnswer = new string[] { };
            TestString(desiredAnswer, str);
            str = new string[] { "ENGL111: ENGL110" };
            TestString(desiredAnswer, str);
            str = new string[] {
"CSE258: CSE244 CSE243 INTR100",
"CSE221: CSE254 INTR100",
"CSE254: CSE111 MATH210 INTR100",
"CSE244: CSE243 MATH210 INTR100",
"MATH210: INTR100",
"CSE101: INTR100",
"CSE111: INTR100",
"ECE201: CSE111 INTR100",
"ECE111: INTR100",
"CSE243: CSE254",
"INTR100:",
};
            desiredAnswer = new string[] { "INTR100", "CSE101", "CSE111", "ECE111", "ECE201", "MATH210", "CSE254", "CSE221", "CSE243", "CSE244", "CSE258" };
            TestString(desiredAnswer, str);
        }
        private static string[] TestString(string[] desiredAnswer, string[] str)
        {
            string[] answer;
            Prerequisites p = new Prerequisites();
            answer = p.orderClasses(str);
            Debug.Assert(answer.Length == desiredAnswer.Length, "Invalid length");
            foreach (string ans in answer)
                Debug.WriteLine(ans);
            for (int i = 0; i < answer.Length; i++)
            {
                Debug.Assert(desiredAnswer[i] == answer[i], "Invalid member");
            }
            return answer;
        }
    }
}

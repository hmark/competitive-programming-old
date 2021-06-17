using System;
using System.Linq;
using System.Collections.Generic;

namespace b
{
    class Program
    {
        static int ReadInt()
        {
            return int.Parse(Console.ReadLine());
        }

        static int[] ReadIntArray()
        {
            return Array.ConvertAll(Console.ReadLine().Split(), s => int.Parse(s));
        }

        static void Main(string[] args)
        {
            int N = ReadInt();
            int[] A = ReadIntArray();

            Console.WriteLine(Execute(N, A.ToList()));
        }

        static string Execute(int N, List<int> A)
        {
            HashSet<int> cache = new HashSet<int>();
            foreach (int i in A)
            {
                if (cache.Contains(i))
                {
                    return "No";
                }
                else
                {
                    cache.Add(i);
                }
            }

            return "Yes";
        }
    }
}

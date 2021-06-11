using System;
using System.Linq;
using System.Collections.Generic;

namespace b
{
    class Program
    {
        static void Main(string[] args)
        {
            int T = int.Parse(Console.ReadLine());

            for (int i = 0; i < T; i++)
            {
                int N = int.Parse(Console.ReadLine());
                int[] A = Array.ConvertAll(Console.ReadLine().Split(), s => int.Parse(s));

                Console.WriteLine(Execute(N, A.ToList()));
            }
        }

        static int Execute(int N, List<int> A)
        {
            int sum = A.Sum();

            if (sum % N != 0)
            {
                return -1;
            }

            int target = sum / N;

            return A.Where(item => item > target).Count();
        }
    }
}

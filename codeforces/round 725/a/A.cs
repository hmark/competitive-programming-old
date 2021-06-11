using System;
using System.Linq;
using System.Collections.Generic;

namespace a
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
            int mn = A.Min();
            int mx = A.Max();
            int mnIndex = A.IndexOf(mn);
            int mxIndex = A.IndexOf(mx);

            int leftIndex = Math.Min(mnIndex, mxIndex);
            int rightIndex = Math.Max(mnIndex, mxIndex);

            int leftActions = leftIndex + 1;
            int rightActions = A.Count - rightIndex;
            int diffActions = rightIndex - leftIndex;

            return Math.Min(Math.Min(leftActions + rightActions, leftActions + diffActions), rightActions + diffActions);
        }
    }
}

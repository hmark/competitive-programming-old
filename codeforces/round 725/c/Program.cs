using System;
using System.Linq;
using System.Collections.Generic;

namespace c
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
            int T = ReadInt();

            for (int i = 0; i < T; i++)
            {
                int[] row = ReadIntArray();
                int N = row[0];
                int L = row[1];
                int R = row[2];
                int[] A = ReadIntArray();

                Console.WriteLine(Execute(N, L, R, A.ToList()));
            }
        }

        static int Execute(int N, int L, int R, List<int> A)
        {
            A.Sort();

            int result = 0;
            for (int i = 0; i < N; i++)
            {
                for (int j = i + 1; j < N; j++)
                {
                    int sum = A[i] + A[j];
                    if (L <= sum && sum <= R)
                    {
                        result++;
                    }
                    else if (A[i] > R)
                    {
                        return result;
                    }
                    else if (sum > R)
                    {
                        continue;
                    }

                }
            }

            return result;
        }
    }
}

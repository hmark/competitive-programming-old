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
            int[] row = ReadIntArray();
            int A = row[0];
            int B = row[1];
            int C = row[2];

            Console.WriteLine(Execute(A, B, C));
        }

        static string Execute(int A, int B, int C)
        {
            if (C % 2 == 0)
            {
                A = Math.Abs(A);
                B = Math.Abs(B);
            }

            if ((A >= 0 && B >= 0) || (A <= 0 && B <= 0))
            {
                if (A < B)
                {
                    return "<";
                }
                else if (A > B)
                {
                    return ">";
                }
                else
                {
                    return "=";
                }
            }
            else if (A > 0 && B < 0)
            {
                return ">";
            }
            else if (A < 0 && B > 0)
            {
                return "<";
            }

            return "";
        }
    }
}

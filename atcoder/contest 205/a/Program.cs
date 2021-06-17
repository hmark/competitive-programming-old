using System;
using System.Linq;
using System.Collections.Generic;

namespace a
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

            Console.WriteLine(Execute(A, B));
        }

        static float Execute(float A, float B)
        {
            return A / 100.0f * B;
        }
    }
}

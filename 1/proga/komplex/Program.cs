using System;
using System.Linq;

namespace KomplexBeadadnod
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int N;
            int M;

            bool jo;
            do {
                Console.ResetColor();
                if (Console.IsInputRedirected)
                {
                    Console.WriteLine("Napok szama, homersekletek szama: ");
                }
                string nm = Console.ReadLine();
                string[] nmsubs = nm.Split();
                jo = int.TryParse(nmsubs[0], out N) && N >= 0;
                if (!jo)
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Termeszetes szam kell!");
                }
                jo = int.TryParse(nmsubs[1], out M) && M >= 0;
                if (!jo)
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Termeszetes szam kell!");
                }
            } while (!jo);
            Console.ResetColor();
            if (N == 0 || M == 0)
            {
                Console.Write(0);
                return;
            }
            int[,] napok = new int[N, M];

            for (int i = 0; i < N; i++) {
                string s = Console.ReadLine();
                string[] ssubs = s.Split();
                for (int j = 0; j < M; j++) {
                    napok[i, j] = Convert.ToInt32(ssubs[j]);
                }
            }

            double[] avgs = new double[N];
            for (int i = 0; i < N; i++) {
                int sum = 0;
                for (int j = 0; j < M; j++)
                {
                    sum += napok[i, j];
                }
                avgs[i] = sum / (double)M;
            }

            var sortedIndexes = avgs.Select((value, index) => new { Value = value, Index = index })
                                     .OrderByDescending(x => x.Value)
                                     .Select(x => x.Index);

            Console.ResetColor();
            foreach (int index in sortedIndexes)
            {
                Console.Write($"{index + 1} ");
            }
        }
    }
}
using System;

namespace beadando
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string inputFile = args[0];
            int db = 0;
            double s = 0; 
            bool I = true;
            double kicsi = 0;

            using (StreamReader sr = new StreamReader(inputFile))
            {
                string line;
                bool isFirstFreezingReached = false;

                while ((line = sr.ReadLine()) != null)
                {
                    double temperature = double.Parse(line);

                    if (!isFirstFreezingReached)
                    {
                        if (temperature < 0)
                        {
                            isFirstFreezingReached = true;
                            kicsi = temperature;
                        } else
                        {
                            s += temperature;
                            db++;
                        }
                    }
                    else
                    {
                        I = I && temperature < 0;

                        if (temperature < kicsi)
                        {
                            kicsi = temperature;
                        }
                    }
                }
            }

            // Átlag
            Console.WriteLine(s / db);
            // Minden nap nulla fok alatt volt
            Console.WriteLine(I);
            // Minimum
            Console.WriteLine(kicsi);
        }
    }
}
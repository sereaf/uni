using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF3
{
    internal class Diag
    {
        public int n;
        public double[] x;
        public Diag(int n)
        {
            this.n = n;
            x = new double[n];
        }

        public double Get(int i, int j)
        {
            if (i < 0 || i > this.x.Length - 1 || j < 0 || j > this.x.Length - 1)
            {
                throw new Exception("i < 0 || i > this.x.Length-1 || j < 0 || j > this.x.Length-1");
            }
            if (i == j)
            {
                return x[i];
            }
            return 0.0;
        }

        public void Set(int i, int j, double e)
        {
            if (i < 0 || i > this.x.Length-1 || j < 0 || j > this.x.Length-1)
            {
                throw new Exception("i < 0 || i > this.x.Length-1 || j < 0 || j > this.x.Length-1");
            }
            if (i == j)
            {
                this.x[i] = e;
            } else
            {
                throw new Exception("i != j");
            }
        }

        public static Diag Add(Diag a, Diag b) {
            if (a.x.Length != b.x.Length)
            {
                throw new Exception("a.x.Length != b.x.Length");
            }
            Diag c = new Diag(a.x.Length);
            for (int i = 0; i < c.x.Length; i++)
            {
                c.x[i] = a.x[i] + b.x[i];
            }
            return c;
        }

        public static Diag operator +(Diag a, Diag b)
        {
            return Add(a, b);
        }


        public static Diag Multiply(Diag a, Diag b)
        {
            if (a.x.Length != b.x.Length)
            {
                throw new Exception("a.x.Length != b.x.Length");
            }
            Diag c = new Diag(a.x.Length);
            for (int i = 0; i < c.x.Length; i++)
            {
                c.x[i] = a.x[i] * b.x[i];
            }
            return c;
        }

        public static Diag operator *(Diag a, Diag b)
        {
            return Multiply(a, b);
        }

    }
}

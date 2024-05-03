using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF1
{
    public class Rational
    {
        public int n;
        public int d;
        public Rational(int i, int j)
        {
            if (j != 0)
            {
                this.n = i; this.d = j;
            }
            else
            {
                throw new Exception("0-val osztas");
            }
        }

        public static Rational Add(Rational a, Rational b)
        {
            return new Rational(a.n * b.d + a.d * b.n, a.d * b.d);
        }

        public static Rational operator +(Rational a, Rational b)
        {
            return Rational.Add(a, b);
        }

        public static Rational Substract(Rational a, Rational b)
        {
            return new Rational(a.n * b.d - a.d * b.n, a.d * b.d);
        }
        public static Rational operator -(Rational a, Rational b)
        {
            return Rational.Substract(a, b);
        }

        public static Rational Multiply(Rational a, Rational b)
        {
            return new Rational(a.n * b.n, a.d * b.d);
        }
        public static Rational operator *(Rational a, Rational b)
        {
            return Rational.Multiply(a, b);
        }

        public static Rational Divide(Rational a, Rational b)
        {
            if (b.n == 0)
            {
                throw new Exception("0-val osztas");
            }
            return new Rational(a.n * b.d, a.d * b.n);
        }
        public static Rational operator /(Rational a, Rational b)
        {
            return Rational.Divide(a, b);
        }

        public override string ToString()
        {
            return $"{n}/{d}";
        }
    }
}

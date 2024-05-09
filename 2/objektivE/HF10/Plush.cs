using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF10
{
    internal class Plush : Gift
    {

        public Plush(Size size) : base(size) { }

        public override int Point()
        {
            return 3;
        }
    }
}

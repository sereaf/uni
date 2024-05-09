using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF10
{
    internal class L : Size
    {

        private static L instance = null;

        public L() { }

        public static L Instance()
        {
            if (instance == null) { instance = new L(); }
            return instance;
        }
        public int Multi()
        {
            return 3;
        }
    }
}

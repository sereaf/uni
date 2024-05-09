using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF10
{
    internal class XL : Size
    {
        private static XL instance = null;

        public XL() { }

        public static XL Instance()
        {
            if (instance == null) { instance = new XL(); }
            return instance;
        }
        public int Multi()
        {
            return 4;
        }
    }
}

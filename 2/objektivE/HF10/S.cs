using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF10
{
    internal class S : Size
    {
        private static S instance = null;

        public S() { }

        public static S Instance()
        {
            if (instance == null) { instance = new S(); }
            return instance;
        }
        public int Multi() {
            return 1;
        }
    }
}

using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF10
{
    internal abstract class Gift
    {
        private Size size;
        public TargetShot targetShot;

        public Gift(Size size)
        {
            this.size = size;
        }

        public int Value() { return this.Point()*size.Multi(); }

        public abstract int Point();
    }
}

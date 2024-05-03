using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF9
{
    internal class Wallbreaker : Starship
    {
        public Wallbreaker(string name, int shield, int armor, int guardian) : base(name, shield, armor, guardian)
        {
        }
        public override double FireP()
        {
            return armor / 2;
        }
    }

}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF10
{
    internal class AmPark
    {
        private List<TargetShot> targetShots = new List<TargetShot>();
        private List<Guest> guests = new List<Guest>();

        public AmPark(List<TargetShot> t)
        {
            if (t.Count < 2)
            {
                throw new ArgumentException();
            }
            this.targetShots = t;
        }

        public string Best(TargetShot t)
        {
            if (guests.Count == 0)
            {
                throw new ArgumentException();
            }
            return guests.MaxBy(e => e.Result(t)).getName();
        }

        public void Receives(Guest g) {
            if (guests.Contains(g))
            {
                throw new Exception();
            }
            guests.Add(g);
        }
    }
}

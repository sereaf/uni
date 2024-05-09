using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF10
{
    internal class Guest
    {
        private string name { get; }
        private List<Gift> prizes = new List<Gift>();
        public Guest(string n) {
            this.name = n;
        }

        public string getName() { return name; }

        public void Wins(Gift g) {
            if (!g.targetShot.GetGifts().Contains(g))
            {
                throw new Exception();
            }
            g.targetShot.GetGifts().Remove(g);
            prizes.Add(g);
        }

        public int Result(TargetShot t)
        {
            return prizes.Sum(e => e.targetShot == t ? e.Value() : 0);
        }
    }
}

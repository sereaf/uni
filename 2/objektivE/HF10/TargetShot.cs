using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF10
{
    internal class TargetShot
    {
        private string site;
        private List<Gift> gifts = new List<Gift>();

        public TargetShot(string s)
        {
            this.site = s;
        }


        public List<Gift> GetGifts() { return gifts; }

        public void Shows(Gift g) {
            if (g.targetShot != null) {
                throw new Exception();
            }
            if (gifts.Contains(g))
            {
                throw new Exception();
            }
            g.targetShot = this;
            gifts.Add(g);
        }
    }
}

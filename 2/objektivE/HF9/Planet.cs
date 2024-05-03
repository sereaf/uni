using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF9
{
    internal class Planet
    {
        public string name;
        private List<Starship> ships = new List<Starship>();

        public Planet(string name) {
            this.name = name; 
        }

        public void Defends(Starship s)
        {
            if (this.ships.Contains(s)) {
                throw new Exception();
            }
            ships.Add(s);
        }


        public void Leaves(Starship s)
        {
            if (!this.ships.Contains(s))
            {
                throw new Exception();
            }
            ships.Remove(s);
        }

        public int ShipCount()
        {
            return ships.Count;
        }

        public int ShieldSum()
        {
            return ships.Sum((e) => e.GetShield());
        }

        public (bool, double, Starship?) MaxFireP()
        {
            Starship? max = ships.MaxBy(e => e.FireP())!;
            if (max == null)
                return (false, 0, null);
            return (true, max.FireP(), max);
        }
    }
}

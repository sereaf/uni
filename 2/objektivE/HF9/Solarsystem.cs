using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF9
{
    internal class Solarsystem
    {
        public List<Planet> planets = new List<Planet>();

        public (bool, Starship?) MaxFireP() {
            Planet? max = planets.MaxBy(e => e.MaxFireP());
            if (max?.MaxFireP().Item3 == null)
                return (false, null);
            return (true, max.MaxFireP().Item3);
        }

        public List<Planet> Defenseless()
        {
            return planets.FindAll(e => e.ShipCount() == 0);
        }
    }
}

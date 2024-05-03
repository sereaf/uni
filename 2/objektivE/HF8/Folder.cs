using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF8
{
    internal class Folder : Registration
    {
        private List<Registration> items = new List<Registration>();
        public override int GetSize()
        {
            return items.Sum((e) => e.GetSize());
        }

        public void Add(Registration r)
        {
            items.Add(r);
        }

        public void Remove(Registration r)
        {
            items.Remove(r);
        }
    }
}

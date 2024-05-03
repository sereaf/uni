using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF4
{
    struct Element
    {
        public int pr;
        public string data;
    }
    internal class PrQueue
    {
        public List<Element> seq;

        public PrQueue()
        {
            this.seq = [];
        }

        public void SetEmpty()
        {
            this.seq = [];
        }

        public bool isEmpty()
        {
            return this.seq.Count == 0;
        }

        public void Add(Element e)
        {
            seq.Add(e);
        }

        public Element GetMax()
        {
            if (seq.Count == 0)
            {
                throw new Exception("seq len = 0");
            }
            return seq.MaxBy((e) => e.pr);
        }

        public Element RemMax()
        {
            if (seq.Count == 0)
            {
                throw new Exception("seq len = 0");
            }
            Element e = seq.MaxBy((e) => e.pr);
            seq.RemoveAt(seq.IndexOf(e));
            return e;
        }

        public (int, int) MaxSelect()
        {
            if (seq.Count == 0)
            {
                throw new Exception("seq len = 0");
            }
            Element e = seq.MaxBy((e) => e.pr);
            int i = seq.IndexOf(e);
            return (e.pr, i);
        }
    }
}

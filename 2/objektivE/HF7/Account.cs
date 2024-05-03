using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF7
{
    internal class Account
    {
        public string accNum;
        private int balance = 0;
        public List<Card> cards = new List<Card>();

        public Account(string accNum)
        {
            this.accNum = accNum;
        }

        public int GetBalance() { return balance; }

        public void Change(int a) { balance += a; }
    }
}

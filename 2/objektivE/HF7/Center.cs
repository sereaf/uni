using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF7
{
    internal class Center
    {
        private List<Bank> banks = new List<Bank>();

        public Center(List<Bank> banks)
        {
            this.banks = banks;
        }

        public int GetBalance(string cNum)
        {
            bool I;
            Bank bank;
            (I, bank) = FindBank(cNum);
            if (I)
            {
                return bank.GetBalance(cNum);
            }
            return -1;
        }

        public void Transaction(string cNum, int amount)
        {
            bool I;
            Bank bank;
            (I, bank) = FindBank(cNum);
            if (I)
            {
                bank.Transaction(cNum, amount);
            }
        }

        private (bool, Bank) FindBank(string cNum)
        {
            for (int i = 0; i < banks.Count; i++)
            {
                if (banks[i].CheckAccount(cNum))
                {
                    return (true, banks[i]);
                }
            }
            return (false, new Bank());
            // return (false, null);
        }
    }
}

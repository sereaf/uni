using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.AccessControl;
using System.Text;
using System.Threading.Tasks;
using System.Transactions;

namespace HF7
{
    internal class Bank
    {
        private List<Account> accounts = new List<Account>();

        public void OpenAccount(string cNum, Customer c)
        {
            Account account = new Account(cNum);
            accounts.Add(account);
            c.AddAccount(account);
        }

        public void ProvidesCard(string cNum)
        {
            for (int i = 0; i < accounts.Count; i++)
            {
                if (accounts[i].accNum == cNum)
                {
                    accounts[i].cards.Add(new Card(cNum, "1234"));
                }
            }
        }

        public int GetBalance(string cNum)
        {
            bool I;
            Account account;
            (I, account) = FindAccount(cNum);
            if (I)
            {
                return account.GetBalance();
            }
            return -1;
        }
        public void Transaction(string cNum, int amount)
        {
            bool I;
            Account account;
            (I, account) = FindAccount(cNum);
            if (I)
            {
                account.Change(amount);
            }
        }
        public bool CheckAccount(string cNum)
        {
            for (int i = 0; i < accounts.Count; i++)
            {
                if (accounts[i].accNum == cNum)
                {
                    return true;
                }
            }
            return false;
        }
        private (bool, Account) FindAccount(string cNum)
        {
            for (int i = 0; i < accounts.Count; i++)
            {
                if (accounts[i].accNum == cNum)
                {
                    return (true, accounts[i]);
                }
            }
            return (false, new Account(cNum));
            //return (false, null);
        }
    }
}

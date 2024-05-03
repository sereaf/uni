using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HF7
{
    internal class Customer
    {
        private string pin;
        private int withdraw;
        private List<Account> accounts = new List<Account>();

        public Customer(string pin, int withdraw) {
            this.pin = pin;
            this.withdraw = withdraw;
        }

        public void Withdrawal(ATM atm)
        {
            atm.Process(this);
        }

        public Card ProvidesCard()
        {
            return accounts.First().cards.First();
        }
        public string ProvidesPIN()
        {
            return pin;
        }
        public int RequestMoney()
        {
            return withdraw;
        }
        public void AddAccount(Account a)
        {
            accounts.Add(a);
        }
    }
}

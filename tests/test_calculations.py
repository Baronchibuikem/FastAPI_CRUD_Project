from app.utils.calculations import BankAccount, InsufficientFunds
import unittest
import pytest


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.starting_balance = 1000
        self.bank_account = BankAccount(self.starting_balance)

    def test_deposit_success(self):
        amount = 2000
        self.bank_account.deposit(amount)
        assert self.bank_account.balance == 3000

    def test_withdraw_success(self):
        amount_to_withdraw = 500
        self.bank_account.withdraw(amount_to_withdraw)
        assert self.bank_account.balance == 500

    def test_withdraw_insufficient_funds(self):
        amount_to_withdraw = 2000
        with pytest.raises(InsufficientFunds):
            self.bank_account.withdraw(amount_to_withdraw)
        self.assertEqual(self.bank_account.balance, 1000)

    def test_collect_interest(self):
        self.bank_account.collect_interest()
        assert self.bank_account.balance == 10000


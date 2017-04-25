import unittest


class CurrentAccountTestCases(unittest.TestCase):
    def setUp(self):
        self.ca = CurrentAccount()

    def tearDown(self):
        del self.ca

    def test_current_account_is_instance_of_bank_account(self):
        self.assertTrue(isinstance(self.ca, BankAccount), msg='CurrentAccount is not a subclass of BankAccount')

    def test_current_account_can_deposit_valid_amounts(self):
        balance = self.ca.deposit(1500)
        self.assertEquals(balance, 1500)

    def test_current_account_cannot_withdraw_more_than_current_balance(self):
        message = self.ca.withdraw(1500)
        self.assertEquals(message, 'Cannot withdraw beyond the current account balance', msg='No overdrafts')

    def test_current_account_can_withdraw_valid_cash_amounts(self):
        self.ca.deposit(23001)
        self.ca.withdraw(437)
        self.assertEquals(self.ca.balance, 22564, msg='Incorrect balance after withdrawal')

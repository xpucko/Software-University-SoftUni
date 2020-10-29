import unittest


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account('Thierry', 100)

    def test_addTransaction_whenInvalidType_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            self.account.add_transaction('test')

    def test_addTransaction_whenValidType_shouldAppendTransaction(self):
        self.assertEqual(len(self.account), 0)
        self.account.add_transaction(14)
        self.assertEqual(len(self.account), 1)

    def test_balanceProperty_shouldSumAmountAndAllTransactions(self):
        self.assertEqual(self.account.balance, 100)
        self.account.add_transaction(10)
        self.assertEqual(self.account.balance, 110)

    def test_validateTransaction_whenValidTransaction(self):
        result = Account.validate_transaction(self.account, 14)
        self.assertEqual(result, f'New balance: 114')

    def test_validateTransaction_staticMethod(self):
        import inspect
        self.assertTrue(isinstance(inspect.getattr_static(self.account, 'validate_transaction'), staticmethod))

    def test_custom_str(self):
        result = str(self.account)
        self.assertEqual(result, 'Account of Thierry with starting amount: 100')

    def test_custom_repr(self):
        result = repr(self.account)
        self.assertEqual(result, 'Account(Thierry, 100)')

    def test_custom_len(self):
        self.account.add_transaction(50)
        result = len(self.account)
        self.assertEqual(result, 1)

    def test_getitem_valid_index(self):
        self.account.add_transaction(20)
        result = self.account[0]
        self.assertEqual(result, 20)

    def test_custom_reversed(self):
        self.account.add_transaction(50)
        self.account.add_transaction(100)
        result = list(reversed(self.account))
        self.assertEqual(result, [100, 50])

    def test_custom_graterThan(self):
        account2 = Account('LeBron', 50)
        self.assertGreater(self.account, account2)
        self.assertTrue(self.account.balance > account2.balance)

    def test_custom_graterOrEqual(self):
        account2 = Account('LeBron', 100)
        self.assertGreaterEqual(self.account, account2)
        self.assertTrue(self.account.balance >= account2.balance)

    def test_lessThan(self):
        account2 = Account('LeBron', 200)
        self.assertLess(self.account, account2)
        self.assertTrue(self.account.balance < account2.balance)

    def test_lessOrEqual(self):
        account2 = Account('LeBron', 100)
        self.assertLessEqual(self.account, account2)
        self.assertTrue(self.account.balance <= account2.balance)

    def test_accountsAreEqual(self):
        account2 = Account('LeBron', 100)
        self.assertEqual(self.account, account2)
        self.assertTrue(self.account.balance == account2.balance)

    def test_notEqual(self):
        account2 = Account('LeBron', 500)
        self.assertNotEqual(self.account, account2)
        self.assertTrue(self.account.balance != account2.balance)

    def test_custom_add(self):
        account2 = Account('LeBron', 500)
        account_3 = self.account + account2
        self.assertEqual(repr(account_3), 'Account(Thierry&LeBron, 600)')
        self.assertEqual(account_3.balance, 600)
        self.assertEqual(account_3.owner, 'Thierry&LeBron')


if __name__ == '__main__':
    unittest.main()

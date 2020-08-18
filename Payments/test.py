import requests
import unittest
from payprocess.main import main_module
# URL = 'http://10.13.175.58:8000/ppayment'
# r = requests.post(url = URL, data={'CreditCardNumber': '1863937303639363', 'CardHolder': 'Andrew Joson', 'ExpirationDate': '2020/12/12 12:05:02','SecurityCode':'234','Amount':501})
# print(r,r.text)



class Test_main_module(unittest.TestCase):
    def test_main_module(self):
        self.assertAlmostEqual(main_module({'CreditCardNumber': '1863937303639363', 'CardHolder': 'Andrew Joson', 'ExpirationDate': '2020/12/12 12:05:02','SecurityCode':'234','Amount':501}),True)
        self.assertAlmostEqual(main_module({'CreditCardNumber': '1863937303639363', 'CardHolder': 'Andrew Joson', 'ExpirationDate': '2020/12/12 12:05:02','SecurityCode':'234','Amount':'501'}),False)
        self.assertAlmostEqual(main_module({'CreditCardNumber': '1863937303639363', 'CardHolder': 'Andrew Joson', 'ExpirationDate': '2020/12/12 12:05:02','SecurityCode':'234','Amount':12}),True)
        self.assertAlmostEqual(main_module({'CreditCardNumber': '1863937303639363', 'CardHolder': 'Andrew Joson', 'ExpirationDate': '2020/12/12 12:05:02','SecurityCode':'234','Amount':144}),True)
        self.assertAlmostEqual(main_module({'CreditCardNumber': '1863937303639363', 'CardHolder': 'Andrew Joson', 'ExpirationDate': '2020/12/12 12:05:02','SecurityCode':'','Amount':12}),True)
        self.assertAlmostEqual(main_module({'CreditCardNumber': '1863937303639363', 'CardHolder': 'Andrew Joson', 'ExpirationDate': '2020/07/12 12:05:02','Amount':12}),False)
        self.assertAlmostEqual(main_module({'CreditCardNumber': '1863937303363', 'CardHolder': 'Andrew Joson', 'ExpirationDate': '2020/12/12 12:05:02','Amount':12}),False)
        self.assertAlmostEqual(main_module({'CreditCardNumber': '1863937303363', 'CardHolder': 'Andrew Joson', 'ExpirationDate': '2020/ 12:05:02','Amount':12}),False)
        self.assertAlmostEqual(main_module({'CreditCardmber': '1863937303363', 'CardHolder': 'Andrew Joson', 'ExpirationDate': '2020/ 12:05:02','Amount':12}),False)
        self.assertAlmostEqual(main_module({'CreditCardmber': '1863937303363', 'CardHolder': 'Andrew Joson', 'Date': '2020/ 12:05:02','Amount':12}),False)

if __name__ == '__main__':
    unittest.main()

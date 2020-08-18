from payprocess.paymentGateway import CheapPaymentGateway, ExpensivePaymentGateway, PremiumPaymentGateway

class Payment():
    def module_pay(self, data):
        amount = int(data['Amount'])
        if amount <= 20:
            if CheapPaymentGateway().connect():
                CheapPaymentGateway().pay(data)
                return True
            else:return False

        elif 20 < amount <= 500:
            if ExpensivePaymentGateway().connect():
                ExpensivePaymentGateway().pay(data)
                return True
            elif CheapPaymentGateway().connect():
                CheapPaymentGateway().pay(data)
                return True
            else:return False

        elif amount > 500:
            for i in range(3):
                if PremiumPaymentGateway().connect():
                    PremiumPaymentGateway().pay(data)
                    return True

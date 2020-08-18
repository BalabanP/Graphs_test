from abc import ABC,abstractmethod

class Gatways(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def pay(self):
        pass

class CheapPaymentGateway(Gatways):
    def connect(self):
        """ Conecting to getway server"""
        connected = True
        if connected:
            return True
        else:
            return False

    def pay(self,data):
        print("this is cheap")

class ExpensivePaymentGateway(Gatways):
    def connect(self):
        """ Conecting to getway server"""
        connected = True
        if connected:
            return True
        else:
            return False

    def pay(self,data):
        print("this is Expensive")

class PremiumPaymentGateway(Gatways):
    def connect(self):
        """ Conecting to getway server"""
        connected = True
        if connected:
            return True
        else:
            return False

    def pay(self,data):
        print("this is Premium")

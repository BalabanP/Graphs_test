from abc import ABC, abstractmethod
from datetime import datetime

class Data_Verify(ABC):
    @abstractmethod
    def verify(self):
        pass


class CardNumber(Data_Verify):

    def verify(self, nr):
        if len(nr) == 16:
            return True
        else: return False

class CardHolder(Data_Verify):

    def verify(self, data):
        return True

class ExpirationDate(Data_Verify):

    def verify(self, ExpirationDate):
        
        try:
            if datetime.strptime(ExpirationDate,"%Y/%m/%d %H:%M:%S") > datetime.now():
                return True
        except:
            return False


class SecurityCode(Data_Verify):

    def verify(self, SecurityCode):
        if len(SecurityCode) == 3:
            if SecurityCode.isdigit():
                return True
        elif SecurityCode == '':
            return True
        else:
            return False

class Amount(Data_Verify):

    def verify(self, amount):
        if isinstance(amount, int):
            return True
        else:
            return False

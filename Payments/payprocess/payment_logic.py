
from payprocess.dataVerify import CardNumber,CardHolder,ExpirationDate,SecurityCode,Amount


class Card():
    def __init__(self):
        CreditCardNumber = None
        CardHolder = None
        ExpirationDate = None
        Amount = None
        SecurityCode = None

class Card_builder():
    def __init__(self, card = Card()):
        self.newcard = card

    def createCard(self,CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount):
        self.newcard.CreditCardNumber = CreditCardNumber
        self.newcard.CardHolder = CardHolder
        self.newcard.ExpirationDate = ExpirationDate
        self.newcard.SecurityCode = SecurityCode
        self.newcard.Amount = Amount


class paymentVerify():
    def key_verify(self, data):
        mandatory_keys = ['CreditCardNumber','CardHolder','ExpirationDate','Amount']
        if all(key in data for key in mandatory_keys):
            return True
        else:
            return False


def main_module(data):

    if paymentVerify().key_verify(data):
        CreditCardNumberV = data['CreditCardNumber']
        ExpirationDateV = data['ExpirationDate']
        CardHolderV = data['CardHolder']
        AmountV = data['Amount']
        if 'SecurityCode' in data:
            SecurityCodeV = data['SecurityCode']
        else:
            SecurityCodeV = ''
        card_obj = Card_builder()
        card_obj.createCard(CreditCardNumberV,CardHolderV, ExpirationDateV, SecurityCodeV, AmountV)
        print(card_obj.newcard.CreditCardNumber,card_obj.newcard.CardHolder,card_obj.newcard.ExpirationDate,card_obj.newcard.SecurityCode,card_obj.newcard.Amount)

        card_info_verify = [
        CardNumber().verify(card_obj.newcard.CreditCardNumber),
        CardHolder().verify(card_obj.newcard.CardHolder),
        ExpirationDate().verify(card_obj.newcard.ExpirationDate),
        SecurityCode().verify(card_obj.newcard.SecurityCode),
        Amount().verify(card_obj.newcard.Amount)
        ]
        print(card_info_verify)
        if all(cardinfo == True for cardinfo in card_info_verify):
            print("uraaaa")

    else:
        return False


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

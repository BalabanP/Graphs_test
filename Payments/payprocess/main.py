
from payprocess.dataVerify import CardNumber,CardHolder,ExpirationDate,SecurityCode,Amount
from payprocess.Card import Card_builder
from payprocess.payment import Payment

def main_module(data):

    mandatory_keys = ['CreditCardNumber','CardHolder','ExpirationDate','Amount']
    if all(key in data for key in mandatory_keys):
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

        card_info_verify = [
        CardNumber().verify(card_obj.newcard.CreditCardNumber),
        CardHolder().verify(card_obj.newcard.CardHolder),
        ExpirationDate().verify(card_obj.newcard.ExpirationDate),
        SecurityCode().verify(card_obj.newcard.SecurityCode),
        Amount().verify(card_obj.newcard.Amount)
        ]
        print(card_info_verify)
        if all(cardinfo == True for cardinfo in card_info_verify):
            Payment().module_pay(data)
            return True
        else: return False

    else:
        return False

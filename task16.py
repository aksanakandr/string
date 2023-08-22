"""
Task16.

# write class for bank card.
# Class should reflect card lifecycle, card operations etc.
# use CVV, PIN, Name, Surname , end date, card_num as initial params
# class should have in addition to common logic some class attributes,
#as minimum one classmethod and
# as minimum  one staticmethod, two or more getters/setters
# do not forget about block ""if __name__ == '__main__': ""
"""
from datetime import datetime


class BankCard:

    balance = 0
    def __init__(self, cvv, __pin, name, surname, end_date, card_num):
        """
        Create BankCard class.

        Args:
            cvv: str
            __pin: str
            name: str
            surname: str
            end_date: sate
            card_num: str
        """
        self.cvv = cvv
        self.__pin = __pin
        self.name = name
        self.surname = surname
        self.end_date = end_date
        self.card_num = card_num

    @classmethod
    def update_balance(cls, new_balance):
        """
        Update_balance.

        Args:
            new_balance: int

        Returns:new_balance

        """
        cls.balance = new_balance
        print('Balance is updated')

    @property
    def check_pin(self):
        """
        Read the pin.

        Returns:str

        """
        return self.__pin

    @check_pin.setter
    def check_pin(self, value):
        """
        Set new pin.

        Args:
            value: int

        Returns:int or raise Error

        """
        if not value.isdigit():
            raise TypeError
        if not len(value) == 4:
            raise ValueError
        self.__pin = value

    @staticmethod
    def today_data():
        """
        Find today_day.

        Returns:data

        """
        today_day = datetime.date.today()
        return today_day

    def check_cvv(self):
        """
        Check cvv.

        Returns:True or Error

        """
        if not self.cvv.isdigit():
            raise TypeError
        if not len(self.cvv) == 3:
            raise ValueError
        return True

    def check_card_num(self):
        """
        Check card_num.

        Returns:True or False

        """
        return self.card_num.isdigit() and len(self.card_num) == 16
    def  check_end_date(self):
        """
        Check end_date.

        Returns:True or False

        """
        return self.end_date != self.today_data()

    def check_name(self):
        """
        Check_name.

        Returns:True or False

        """
        return self.name.isalpha() and self.name.isascii()
    def check_surname(self):
        """
        Check surname.

        Returns:True or False

        """
        return self.surname.isalpha() and self.surname.isascii()

    def autorization_payment(self, tranzaction_amount):
        """
        Check if card balance > tranzaction_amount.

        Args:
            tranzaction_amount: int

        Returns:str

        """
        self.tranzaction_amount = tranzaction_amount
        if  self.balance >= self.tranzaction_amount:
            print('Payment is proceed')
        else:
           print('Payment is failed')

    def check_card(self):
        """
        Check if card is accepted or not.

        Returns:str

        """
        if (
                self.check_cvv() and
                self.check_card_num() and
                self.check_end_date() and
                self.check_name() and
                self.check_surname() and
                self.check_pin()
        ):
            print('Card is accepted')
        else:
           print('Card is not accepted')


if __name__ == '__main__':
    card = BankCard('234', '1234', 'Aksana', 'Kandr', 12/10/2024, '111111111')
    card.check_card()
    card.autorization_payment(1234)
    card.update_balance(25)
    print('Current pin:', card.check_pin)
    new_pin = '5788'
    card.check_pin = new_pin
    print('Updated pin:', new_pin)
